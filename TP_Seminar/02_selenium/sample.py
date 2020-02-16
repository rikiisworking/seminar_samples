# coding: utf-8
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
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
    #options.add_argument('--headless') 브라우저 창 숨기기
    chromedriver_path = ChromeDriverManager().install()
 
    return webdriver.Chrome(chromedriver_path, options=options)

def test():
    driver = setup_driver()
    driver.get("https://www.naver.com")
    newsstand_element = driver.find_element_by_css_selector(".an_menulist > h3:nth-child(1) > a:nth-child(1)")
    print(newsstand_element.text)
    time.sleep(2)
    driver.close()

if __name__ == "__main__":
    test()