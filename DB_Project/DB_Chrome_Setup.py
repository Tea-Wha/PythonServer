from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chrome-win64\chrome-win64\chrome.exe')

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")  # 브라우저 최대화

# ChromeDriver 실행
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 웹툰 페이지로 이동
driver.get("https://comic.naver.com/webtoon?tab=mon")