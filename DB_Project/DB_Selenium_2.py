from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 크롤링할 페이지 URL
driver.get("https://comic.naver.com/webtoon?tab=mon")  # 실제 크롤링할 페이지 URL로 변경

# 크롤링할 데이터 저장 리스트
webtoon_titles = []

# Full XPath의 첫 번째와 마지막 범위
for i in range(1, 102):  # li[1]부터 li[101]까지
    try:
        # 각 항목의 Full XPath 생성
        full_xpath = f'/html/body/div[1]/div/div[2]/div[3]/div[1]/div[1]/ul/li[{i}]/div/a/span/span'

        # XPath로 요소 찾기
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, full_xpath))
        )

        # 찾은 요소의 텍스트를 리스트에 저장
        webtoon_titles.append(title_element.text)

    except Exception as e:
        print(f"XPath {i} 에러: {e}")

# 결과 출력
for idx, title in enumerate(webtoon_titles, start=1):
    print(f"{idx}: {title}")

# 브라우저 닫기
driver.quit()