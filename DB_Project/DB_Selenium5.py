from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#네이버 로그인 페이지 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(3)

# JavaScript로 직접 입력 필드에 값을 설정하는 방법
driver.execute_script("document.getElementById('id').value='htw7880';")
time.sleep(3)
driver.execute_script("document.getElementById('pw').value='^ghdxoghk18';")
time.sleep(3)

login_button = driver.find_element(By.ID, "log.login")
login_button.click()

driver.get("https://comic.naver.com/webtoon?tab=mon") # 실제 크롤링할 페이지 URL로 변경

# 특정 영역에 있는 모든 li 태그를 찾기 (XPath는 해당 웹페이지에 맞게 수정)
webtoon_titles = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[1]/div[1]/ul/li"))
)
webtoon_authors = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ContentAuthor__author--CTAAP"))
)


# 크롤링할 데이터 저장 리스트
webtoon_data = []

webtoon_authors_data = []

webtoon_ratings_data = []

# 모든 li 항목을 반복하여 크롤링
for webtoon in all_webtoons:
    try:
        # 웹툰 제목 찾기
        title = webtoon.find_element(By.XPATH, "./div/a/span/span").text

        # 웹툰 평점 찾기 (예시로 div 내부에 평점이 있다고 가정)
        rating = webtoon.find_element(By.XPATH, "./div/div/a").text

        # 웹툰 작가명 찾기 (예시로 div 내부에 작가명이 있다고 가정)
        author = webtoon.find_element(By.XPATH, "./div/div/span/span").text

        # 하나의 웹툰 데이터를 리스트로 저장 (제목, 평점, 작가)
        webtoon_data.append([title, rating, author])

    except Exception as e:
        print(f"웹툰 데이터 수집 실패: {e}")

for idx, title, rating, author in enumerate(webtoon_data, start=1):
    print(f"{idx}: {title} {rating} {author}")

# 브라우저 닫기
driver.quit()
