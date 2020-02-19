# coding: utf-8
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def test_get():
    #get 요청
    result = requests.get("https://tenping.kr/")
    print(f'status code is:{result.status_code}')
    #print(result.text)
    return result.text

def test_parsing(pg_txt):
    #beautifulsoup 라이브러리 이용한 페이지 파싱
    soup = BeautifulSoup(pg_txt, 'lxml')
    print(soup.prettify())
    #콘텐츠 제목만
    print([element.string for element in soup.select('dd.txt-name')])

def test_post():
    header = {
        "Host": "uuumall.kr",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "67",
        "Origin": "http://uuumall.kr",
        "Connection": "keep-alive",
        "Referer": "http://uuumall.kr/Product/1523",
        "DNT": "1",
    }

    param = {"ProductID":"1523","CurrentPage":"3","PageSize":"20","IsPhotoReview":"","OrderType":"0"}
    result = requests.post("http://uuumall.kr/Detail/GetProductReviewByProductIDList",headers=header,data=param)
    pprint(result.json())

if __name__ == "__main__":
    result_text = test_get()
    test_parsing(result_text)
    #test_post()

