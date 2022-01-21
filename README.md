# Crawling webtoon platforms

## How to connect Selenium to an existing browser

-   cmd
-   cd "C:\Program Files\Google\Chrome\Application"
-   chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\s6xya\Desktop\chromefile"
-   Chrome driver opens

## file setting(for existing browser)

```
chrome_driver = "C:\\Users\\s6xya\\Desktop\\selenium\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
```

## file setting(for new browser)

```
driver = webdriver.Chrome('chromedriver.exe')
```

### FYI

-   chromedriver.exe and .py must be in same directory
-   KakaoWebtoon crawling limit: around 50. (403 Error)

### platforms crawled

-   [x] Naver
-   [x] Kakao
-   [x] Kakaopage
-   [x] Bufftoon
-   [ ] LezhinComics
-   [ ] TopToon
-   [ ] BomToon
-   [ ] Toomics
-   [ ] Comico
