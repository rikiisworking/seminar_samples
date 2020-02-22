# -*- coding: UTF-8 -*-
import requests
import json
import time,random
from pprint import pprint
from datetime import datetime
from bs4 import BeautifulSoup

#올리브영에서 제품정보를 가져오는 크롤러입니다

disp_cats = {'900000100100002':'상품평 베스트','900000100100001':'카테고리 베스트'}
olive_cats = {'':'전체',
'10000010001':'스킨케어',
'10000010002':'메이크업',
'10000010003':'바디케어',
'10000010004':'헤어케어',
'10000010005':'향수/디퓨져',
'10000010006':'미용소품',
'10000010007':'남성',
'10000020003':'건강/위생용품',
'10000020001':'건강식품',
'10000020002':'일반식품',
'10000030003':'반려동물',
'10000030004':'베이비',
'10000030002':'잡화'}

def retrieve_olive():
    upload_buffer = []
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for disp_k, disp_v in disp_cats.items():
        for k,v in olive_cats.items():
            if disp_k == '900000100100001':
                params = {'dispCatNo':disp_k,'fltDispCatNo':k,'pageIdx':1,'rowsPerPage':'8'}
                r = requests.get('http://www.oliveyoung.co.kr/store/main/getBestList.do', params=params)

                soup = BeautifulSoup(r.text, 'lxml')
                items = soup.select("div.prd_info")
                standard = disp_v
                cat = v
                for item in items:
                    item_brand = item.select("span.tx_brand")[0].string
                    item_name = item.select("p.tx_name")[0].string
                    item_price = item.select("span.tx_num")[0].string.replace(',','')
                    item_rank = str(int(item.select("span.thumb_flag.best")[0].string))
                    temp_list = [standard,cat,item_brand,item_name,item_price,item_rank,now]
                    print(temp_list)
                    upload_buffer.append(temp_list)
                    if len(upload_buffer)>=500:
                        yield upload_buffer
                        upload_buffer.clear()
                time.sleep(random.uniform(1,3))
            else:
                for i in range(0,10):
                    params = {'dispCatNo':disp_k,'fltDispCatNo':k,'pageIdx':str(i),'rowsPerPage':'8'}
                    r = requests.get('http://www.oliveyoung.co.kr/store/main/getBestList.do', params=params)


                    soup = BeautifulSoup(r.text, 'lxml')
                    items = soup.select("div.prd_info")
                    standard = disp_v
                    cat = v
                    for item in items:
                        item_brand = item.select("span.tx_brand")[0].string
                        item_name = item.select("p.tx_name")[0].string
                        item_price = item.select("span.tx_num")[0].string.replace(',','')
                        item_rank = str(int(item.select("span.thumb_flag.best")[0].string))
                        temp_list = [standard,cat,item_brand,item_name,item_price,item_rank,now]
                        print(temp_list)
                        upload_buffer.append(temp_list)
                        if len(upload_buffer)>=500:
                            yield upload_buffer
                            upload_buffer.clear()
                    time.sleep(random.uniform(1,3))
            

    if len(upload_buffer)>0:
        yield upload_buffer

def main():
    for sample in retrieve_olive():
        pprint(sample)
        break

if __name__ == "__main__":
    main()