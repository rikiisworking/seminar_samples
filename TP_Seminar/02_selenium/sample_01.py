# -*- coding: UTF-8 -*-

import http
import time
import random
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date,datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException,NoSuchElementException,StaleElementReferenceException


#네이버 쇼핑 트렌드차트에서 데이터를 가져오는 코드입니다,
#10개월전 코드라 정상작동하지 않습니다, 참고용으로 봐주시기 바랍니다.

def setup_driver():
    '''setup selenium driver to connect'''
    options = webdriver.ChromeOptions()
    options.add_argument('disable_infobars')
    options.add_argument('--incognito')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; \
                          Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/61.0.3163.100 Safari/537.36")
    #options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument("log-level=3")
    chromedriver_path = ChromeDriverManager().install()
 
    return webdriver.Chrome(chromedriver_path, options=options)

def get_trend_page(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://m.naver.com")
    '''wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR,"button.lm_btn_ok"))).click()'''
    wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR,"li[data-shortcut-code='menu.SHOP_VOGUE']"))).\
    find_element_by_tag_name('a').click()
    actions = ActionChains(driver)
    for _ in range(6):
        actions.send_keys(u'\ue00f').perform()
        time.sleep(random.uniform(0.5,2.5))

def fetch(driver):
    actions = ActionChains(driver)
    actions.send_keys(u'\ue00e').perform()

    return_list = []
    wait = WebDriverWait(driver, 10)

    cats = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR,"a.csr_tab.MM_REFRESH_TAB")))

    cats_len = len(cats)

    for i in range(cats_len):
        cat2 = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR,"a.csr_tab.MM_REFRESH_TAB")))[i]
        category = cat2.text
        driver.execute_script("arguments[0].click();", cat2)
        keyword_list = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"ul.csr_keyword_list")))
        keywords = keyword_list.find_elements_by_css_selector('span.title')
        keyword_len = len(keywords)
        for i in range(keyword_len):
            reload_keyword_list = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"ul.csr_keyword_list")))
            keyword_obj = reload_keyword_list.find_elements_by_css_selector('span.title')[i]
            keyword = keyword_obj.text
            rank = i+1
            temp = [keyword,"인기키워드 "+category,rank,datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            print(temp)
            return_list.append(temp)    

        '''for index,keyword in enumerate(keywords):
            product = keyword.text
            rank = index+1
            temp = [product,"인기키워드 "+category,rank,datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            print(temp)
            return_list.append(temp)    '''
    
    return return_list

def run():
    driver = setup_driver()
    get_trend_page(driver)
    upload_list = fetch(driver)
    driver.close()
    return upload_list

def main():
    result_list = run()
    print(result_list)


if __name__ == "__main__":
    main()