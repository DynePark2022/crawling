from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "C:\\Users\\s6xya\\Desktop\\selenium\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


driver.get('https://comic.naver.com/webtoon/weekdayList?week=mon')
driver.implicitly_wait(5)


day = driver.find_elements_by_css_selector(
    ".thumb a")[0].get_attribute("title")

print(day)
