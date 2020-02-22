import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint

#네이버 제품 상세 카테고리이름과 코드를 가져오는 코드입니다

basic_cats = {50000003: "디지털/가전", 50000008: "생활/건강", 50000001: "패션/잡화",
                 50000007: "스포츠/레저", 50000005: "출산/육아", 50000004: "가구/인테리어",
                 50000000: "패션/의류", 50000002: "화장품/미용", 50000009: "여행/문화",
                 50000006:  "식품"}

def main():
    final = []
    for key in basic_cats.keys():
        r = requests.get("https://search.shopping.naver.com/category/category.nhn?cat_id="+str(key))
        soup = BeautifulSoup(r.text,"lxml")
        cat_lists = soup.select('ul.category_list')
        big_cats = soup.select('div.category_cell > h3 > a')
        cats = []
        for cat_list in cat_lists:
            cats.extend(cat_list.select('a'))
        cats.extend(big_cats)

        for cat in cats:
            cat_code = cat['href'][-8:]
            cat_name = cat.string
            if cat_name is None:
                cat_name = cat.select('strong')[0].text
            if "더보기" in cat_name:
                continue
            print("cat_code: %s, cat_name: %s" %(cat_code,cat_name))
            final.append([cat_code,cat_name])
        time.sleep(1)

    return final

if __name__ == "__main__":
    result = main()
    pprint(result)