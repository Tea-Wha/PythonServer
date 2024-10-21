import requests

url = "https://www.google.com"  # 연결을 확인할 외부 URL
try:
    response = requests.get(url, timeout=5)  # 5초 안에 응답을 기다림
    if response.status_code == 200:
        print("성공적으로 URL에 연결되었습니다!")
    else:
        print(f"URL 연결 실패. 상태 코드: {response.status_code}")
except requests.ConnectionError:
    print("URL에 연결할 수 없습니다. 인터넷 연결을 확인하세요.")
except requests.Timeout:
    print("요청이 시간 초과되었습니다.")
