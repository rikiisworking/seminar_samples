# -*- coding: utf-8 -*-
import time
import tweepy
import requests
import os
from PIL import Image
from resizeimage import resizeimage

twitter_consumer_key = ''
twitter_consumer_secret = ' '
twitter_access_token = ''
twitter_token_secret = ''

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_token_secret)
api = tweepy.API(auth)
user = api.me()

def tweet_msg(msg):
    api.update_status(msg)

def tweet_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        with open(filename,'r+b') as f:
            with Image.open(f) as image:
                w,h = image.size
                if w < 440 and h < 220:
                    api.update_with_media(filename, status=message)
                    os.remove(filename)
                    return
                cover = resizeimage.resize_cover(image,[440,220])
                cover.save('resized.jpeg',image.format)
        api.update_with_media('resized.jpeg', status=message)
        os.remove(filename)
        os.remove('resized.jpeg')
    else:
        print("Unable to download image")

def main():
    tweet_msg("hello twitter!")
    tweet_image('http://www.petsworld.in/blog/wp-content/uploads/2014/09/cute-kittens.jpg','this is image upload test')

if __name__ == "__main__":
    main()