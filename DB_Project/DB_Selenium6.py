import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#네이버 로그인 페이지 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(5)

# id_box = driver.find_element(By.ID, "id")
# id_box.send_keys("htw7880")
# time.sleep(5)
#
# pw_box = driver.find_element(By.ID, "pw")
# pw_box.send_keys("^ghdxoghk18")
# time.sleep(5)

# JavaScript로 직접 입력 필드에 값을 설정하는 방법
driver.execute_script("document.getElementById('id').value='htw7880';")
time.sleep(2)
driver.execute_script("document.getElementById('pw').value='';")
time.sleep(2)

login_button = driver.find_element(By.ID, "log.login")
login_button.click()

# 크롤링할 페이지 URL
driver.get("https://comic.naver.com/webtoon?tab=mon") # 실제 크롤링할 페이지 URL로 변경
time.sleep(2)

# 특정 영역에 있는 모든 li 태그를 찾기 (XPath는 해당 웹페이지에 맞게 수정)
author_elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ContentAuthor__author--CTAAP" ))
)

# 크롤링할 데이터 저장 리스트
webtoon_authors = []

# 모든 li 항목을 반복하여 크롤링
for author in author_elements:
    try:
        # li 태그 안의 span 요소 찾기 (구조에 맞게 XPath 수정 가능)
        author_element = author.text
        first_author_element = re.split(r' / |,', author_element)
        first_author = first_author_element[0]
        webtoon_authors.append(first_author)  # 텍스트 저장
    except Exception as e:
        print(f"에러 발생: {e}")

# 결과 출력
for idx, title in enumerate(webtoon_authors, start=1):
    print(f"{idx}: {title}")

# 브라우저 닫기
driver.quit()