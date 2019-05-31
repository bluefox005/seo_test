from datetime import time
import time as t
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

WAITING_TIME = 1000
LOADING_TIME = 3000
STATE_TIME = 40000

def login(driver, user, pwd):
    driver.get("https://www.google.ca/")
    t.sleep(5)
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_id("gb_70").click()
    t.sleep(5)
    driver.find_element_by_id("identifierId").send_keys(user)
    t.sleep(5)
    driver.find_element_by_id("identifierNext").click()

    t.sleep(5)
    driver.find_element_by_name("password").send_keys(pwd)
    t.sleep(5)
    driver.find_element_by_id("passwordNext").click()
    t.sleep(5)
    # driver.implicitly_wait(WAITING_TIME)
    # assert "Log into Facebook" in driver.title

def isAdsExist(element):
    flag = True
    try:
        driver.find_element_by_id(element)
        return flag
    except:
        flag = False
        return flag

def isBonaventureAds(element):
    flag = True
    try:
        url_link=driver.find_element_by_class_name(element).text
        if url_link=="www.ubreakifix.com/ca/bonaventure":
            return flag
        else:
            flag = False
            return flag
    except:
        flag = False
        return flag

def break_ad_keyword(driver,keyword):
    # driver.implicitly_wait(WAITING_TIME)
    t.sleep(10)
    driver.find_element_by_name("q").send_keys(keyword)
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    t.sleep(10)
    # driver.implicitly_wait(LOADING_TIME)
    has_ads=isAdsExist("tads")
    is_store = isBonaventureAds("UdQCqe")
    if has_ads:
       if not is_store:
            driver.find_element_by_id("vn1s0p1c0").click()
            t.sleep(10)
            # driver.implicitly_wait(STATE_TIME)

def improve_seo_by_keyword(driver,keyword):
    # driver.implicitly_wait(WAITING_TIME)
    # for i in range(2):            # 循环60次，从0至59
    #     if i >= 1 :               # 当i大于等于59时，打印提示时间超时
    #         print("timeout")
    #         break
    #     try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
    #         driver.get("https://www.google.ca/")
    #         t.sleep(10)
    #         driver.find_element_by_name("q").send_keys(keyword)
    #         t.sleep(3)
    #         driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    #         t.sleep(10)
    #         url=driver.find_element_by_xpath('//a[contains(@href,"locations/bonaventure")]')
    #         if len(url)!=0: # 如果能查找到特定的元素id就提前退出循环
    #             url.click()
    #             break
    #     except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
    #         print("wait for find element")
    #     time.sleep(2)

    t.sleep(10)
    driver.find_element_by_name("q").send_keys(keyword)
    t.sleep(3)
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    t.sleep(10)
    # driver.implicitly_wait(60)
    try:
        driver.find_element_by_xpath('//a[contains(@href,"locations/bonaventure")]').click()
    except NoSuchElementException:
        return


if __name__ == "__main__":
    user = "h"
    pwd = "hw"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    login(driver,user,pwd)

    try:
        for i in range(10):
            # driver.get("https://www.google.ca/")
            # driver.implicitly_wait(WAITING_TIME)
            # break_ad_keyword(driver,"ubreakifix montreal")
            print(i)
            x = datetime.now()
            print(x.strftime("%X"))

            driver.get("https://www.google.ca/")
            driver.implicitly_wait(WAITING_TIME)
            break_ad_keyword(driver, "ubreakifix")
            # improve_seo_by_keyword(driver,"ubreakifix")

            t.sleep(10)
            # driver.get("https://www.google.ca/")
            # driver.implicitly_wait(WAITING_TIME)
            # break_ad_keyword(driver,"u break i fix montreal")

            # driver.get("https://www.google.ca/")
            # driver.implicitly_wait(WAITING_TIME)
            # improve_seo_by_keyword(driver,"u break i fix montreal")
            # t.sleep(10)
    finally:
        driver.close()

    driver.close()

    driver.quit()
