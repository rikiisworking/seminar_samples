# -*- coding: utf-8 -*-
import requests
import time
import re
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

app_id = #
s_key = #
blog_name = #
title = #
redirect_uri = #
sample_image_path = #

my_id = #
my_pw = #

token_regex_pattern = r'#access_token=(.*)&state'
token_replacer_pattern = r'<replacer>(.*)</replacer>'
#content = 

def setup_driver():
    '''setup selenium driver to connect'''
    options = webdriver.ChromeOptions()
    options.add_argument('disable_infobars')
    options.add_argument('--incognito')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; \
                                Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument('window-size=1080x1920')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument("log-level=3")
    #options.add_argument('--headless') #브라우저 창 숨기기
    chromedriver_path = ChromeDriverManager().install()
 
    return webdriver.Chrome(chromedriver_path, options=options)

def get_token():
    driver = setup_driver()
    address = f"""https://www.tistory.com/oauth/authorize?client_id={app_id}&redirect_uri={redirect_uri}&response_type=token"""
    driver.get(address)
    driver.find_element_by_css_selector("input#loginId").send_keys(my_id)
    driver.find_element_by_css_selector("input#loginPw").send_keys(my_pw)
    driver.find_element_by_css_selector("button.btn_login").click()
    result = re.search(token_regex_pattern, driver.current_url)
    groups = result.group
    return groups(1)

def upload_text(my_text,access_token):
    my_params = {'access_token':access_token,
    'blogName':blog_name,
    'title': title,
    'content':my_text,
    'visibility':0 #발행상태 (0: 비공개 - 기본값, 1: 보호, 3: 발행)
    }
    requests.post('https://www.tistory.com/apis/post/write',params=my_params)

def upload_image(img_path, text, access_token):
    files = {'uploadedfile':open(img_path,'rb')}
    #1st step: image upload & get replacer
    my_params_0 = {
       'access_token':access_token, 
       'blogName':blog_name
    }
    r = requests.post('https://www.tistory.com/apis/post/attach', params=my_params_0, files=files)
    result = re.search(token_replacer_pattern, r.text)
    replacer = result.group(1)

    #2nd step: upload text and image
    my_params_1 = {
        'access_token':access_token,
        'blogName':blog_name,
        'title': title,
        'content':f'<replacer>{replacer}</replacer>{text}',
        'visibility':0 #발행상태 (0: 비공개 - 기본값, 1: 보호, 3: 발행)
    }
    r = requests.post('https://www.tistory.com/apis/post/write',params=my_params_1)

if __name__ == "__main__":
    access_token = get_token()
    upload_text("테스트 문구입니다 ㅠㅠ",access_token)
    upload_image(sample_image_path, "이미지와 함께 올린 테스트 ㅠㅠ",access_token)
