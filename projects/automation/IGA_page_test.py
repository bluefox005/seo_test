from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WAITING_TIME = 10


def test_search_wine(driver):
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_id("header_0_SearchBox_SearchWithinLink").click()
    driver.find_element_by_xpath("//div[@id='search-box']/div/ul/li[2]/label").click()   #select second item
    driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").send_keys("wine")
    driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").send_keys(Keys.ENTER)
    driver.implicitly_wait(WAITING_TIME)
    # assert "Log into Facebook" in driver.title
    assert "Spanish White Bottle..." in driver.find_element_by_id('body_0_main_1_GrocerySearch_TemplateResult_SearchResultListView_ctrl0_ctl00_0_NavigateTo_0').text

def test_search_recipes(driver):
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_id("header_0_SearchBox_SearchWithinLink").click()
    driver.find_element_by_xpath("//div[@id='search-box']/div/ul/li[3]/label").click()   #select second item
    driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").clear()
    driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").send_keys("wine")
    driver.find_element_by_id("header_0_SearchBox_TxtSearchKeywords").send_keys(Keys.ENTER)
    driver.implicitly_wait(WAITING_TIME)
    # assert "Log into Facebook" in driver.title
    assert "Mulled Wine" in driver.find_element_by_id('body_0_main_1_SiteContentSearch_TemplateResult_SearchResultListView_ctrl0_ctl00_0_RecipeItemTemplate_0_TitleLink_0').text


if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

    driver.get("https://www.iga.net")
    driver.implicitly_wait(WAITING_TIME)
    test_search_wine(driver)
    test_search_recipes(driver)

    driver.close()
    driver.quit()
