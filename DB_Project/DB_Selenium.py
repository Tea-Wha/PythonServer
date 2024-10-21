from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # chromedriver 경로
driver = webdriver.Chrome(service=service)

# 네이버 웹툰 페이지로 이동
driver.get("https://comic.naver.com/webtoon?tab=mon")

# 명시적 대기 설정: 웹툰 제목이 포함된 요소가 로드될 때까지 최대 10초 대기
try:
    titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "text"))
    )
    # 웹툰 제목 출력
    for title in titles:
        print(title.text)
except Exception as e:
    print("웹툰 제목을 찾을 수 없습니다. 에러:", e)
finally:
    driver.quit()