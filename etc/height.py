
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get Browser height
chrome_driver = "C:\\Users\\s6xya\\Desktop\\selenium\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

max_height = driver.execute_script("return document.body.scrollHeight")
print(max_height)
# kakaopage
# Monday = 7168
# Tue = 8310
# Wed = 8766
# Thur = 8538
# Fri = 9680
# Sat = 8310
# Sun = 6939
# Fin = 43710
# 완결
# 소년 = 5569  102
# 드라마 = 8538 165
# 로맨스 = 10365 202
# 로판 = 3513 52
# 액션무협 = 9680 189
# BL/GL = 11279 225
# scroll once = 2143

# bufftoon = 16300
