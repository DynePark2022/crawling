from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

chrome_driver = "C:\\Users\\s6xya\\Desktop\\crawling\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

url_list = []
count = 0

WB = openpyxl.Workbook()  # 엑셀 파일 생성
WS = WB.active

print("start----------------")
for webtoon in url_list:
    try:
        driver.get(url_list[count])
        driver.implicitly_wait(5)
        driver.find_element_by_class_name(
            "spacing_mb_6__3bL8F").click()
        driver.implicitly_wait(5)
        time.sleep(0.5)
        first_episode_url = driver.current_url
        WS.cell(count+2, 1, first_episode_url)
        count = count+1
        print(first_episode_url)
        print(count)
        print(len(url_list))
    except:
        print("Error! DONE!")
        break

WB.save("kakao.xls")
print("File saved")
