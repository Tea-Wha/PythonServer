import re

from matplotlib.image import thumbnail
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


# ChromeDriver 경로 설정
service = Service(r'C:\Users\user1\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless") # 헤드리스 모드 활성화
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=chrome_options)

#네이버 로그인 페이지 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(2)

# JavaScript로 직접 입력 필드에 값을 설정하는 방법
driver.execute_script("document.getElementById('id').value='htw7880';")
time.sleep(2)
driver.execute_script("document.getElementById('pw').value='^ghdxoghk18';")
time.sleep(2)

login_button = driver.find_element(By.ID, "log.login")
login_button.click()

# 크롤링할 페이지 URL (여러 페이지) (예시)
urls = [
    "https://comic.naver.com/webtoon?tab=mon",
    "https://comic.naver.com/webtoon?tab=tue",
    "https://comic.naver.com/webtoon?tab=wed",
    "https://comic.naver.com/webtoon?tab=thu",
    "https://comic.naver.com/webtoon?tab=fri",
    "https://comic.naver.com/webtoon?tab=sat",
    "https://comic.naver.com/webtoon?tab=sun"
]

# 크롤링할 데이터 저장 리스트
webtoon_titles = []

for url in urls:
    driver.get(url)
    time.sleep(10)

    # 페이지 로드 후 스크롤을 아래로 내려서 모든 항목 로드
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 페이지 로드 대기 시간 (조정 가능)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # 스크롤 끝까지 도달 시 종료
            break
        last_height = new_height

# 특정 영역에 있는 모든 li 태그를 찾기 (XPath는 해당 웹페이지에 맞게 수정)
    all_items = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[1]/div[1]/ul/li"))
    )

# 모든 li 항목을 반복하여 크롤링
    for item in all_items:
        try:
            # 각 항목의 위치로 스크롤 이동
            driver.execute_script("arguments[0].scrollIntoView();", item)
            time.sleep(1)  # 스크롤 후 잠시 대기 (스크롤과 로딩의 안정성 확보)

            # li 태그 안의 span 요소 찾기 (구조에 맞게 XPath 수정 가능)
            title_element = item.find_element(By.XPATH, "./div/a/span/span").text
            author_element = item.find_element(By.XPATH, "./div/div/a | ./div/a[2]").text
            first_author_element = re.split(r' / |,', author_element)
            first_author = first_author_element[0]
            rating_element = item.find_element(By.XPATH, "./div/div/span/span").text
            url_element = item.find_element(By.XPATH, "./a").get_attribute("href")
            time.sleep(2)
            thumb_element = item.find_element(By.XPATH, "./a/div/img").get_attribute("src")
            time.sleep(2)
            webtoon_titles.append([title_element, first_author, rating_element, url_element, thumb_element])

        except Exception as e:
            print(f"에러 발생: {e}")
            continue

# 결과 출력
for idx, (title, first_author, rating, url, thumb) in enumerate(webtoon_titles, start=1):
    print(f"{idx}: {title} / {first_author} / {rating} / {url} / {thumb}")

# 브라우저 닫기
driver.quit()