from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#需要先安裝ChromeDriver(chromedriver.chromium.org/downloads)
#cd /usr/local/bin/
#open .

# PATH="/User/ziying/Desktop/github/env/lib/python3.8/site-packages/selenium/webdriver/chrome/chromedriver"
# PATH=r"/usr/ziying/Desktop/github/chromdriver"
PATH='./driver/chromedriver'
driver=webdriver.Chrome(executable_path=PATH)
# driver.get('https://www.google.com')

# driver.find_element_by_css_selector('.buynow').click()
# driver.find_element_by_css_selector('.loginBtn').click()
# driver.find_element_by_css_selector('.checkoutBtn').click()
# driver.find_element_by_css_selector('#payment03').click()
# driver.find_element_by_css_selector('#orderSave')

def autoBuy(url):
    driver.get(url)
    driver.find_element_by_css_selector('.buynow').click()
    time.sleep(2)
    # username=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.NAME,"memId"))
    # password=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.NAME,"passwd_show"))
    username=driver.find_element_by_name('memId')
    password=driver.find_element_by_name('passwd_show')
    username.clear()
    password.clear()
    username.send_keys('0983123456')
    time.sleep(3)
    password.send_keys('12345678')
    driver.find_element_by_css_selector('.loginBtn').click()
    driver.find_element_by_css_selector('.checkoutBtn').click()
    driver.find_element_by_css_selector('#payment03').click()
    driver.find_element_by_css_selector('#orderSave')

autoBuy('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9205468&Area=search&mdiv=403&oid=1_1&cid=index&kw=ps4%20%E9%81%8A%E6%88%B2%20%E5%B9%BD%E9%9D%88%E6%88%B0%E5%A3%AB')

