# JSON(JavaScript Object Notation) -> 데이터를 표현하고 전송하기 위한 경량의 데이터 형식
# json 모듈 -> JSON 데이터 파싱 / JSON 객체 생성 / 파이썬 데이터 타입 -> JSON 직렬화 기능 제공
# JSON 데이터를 파싱하여 파이썬 객체로 변환하려면 json 모듈의 loads() 함수 사용

# JSON 인코딩 (직렬화)
# Python Object(Dictionary, List, Tuple 등)를 JSON 문자열로 변경하는 것 

import json
import os
import csv
import requests

print(os.getcwd())
customer = {
    "id" : 123456,
    "name" : "My Phone",
    "history" : [
        {"date" : "2023-05-05", "product" : "iPhone 14 Pro"},
        {"date" : "2023-05-10", "product" : "Galaxy S23 Ultra"}
    ]
}

jsonString = json.dumps(customer)
print(jsonString)

jsonString1 = '''{"name" : "KH", "id" : 123456, "history" : [
    {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
    {"date" : "2023-05-24", "item" : "Galaxy S23 Ultra"}
]}'''

dict = json.loads(jsonString1)

print(dict["name"], dict["id"])
for h in dict["history"]:
    print(h["date"], h["item"])

customer1 = {
    "id" : 123456,
    "name" : "홍태화",
    "history" : [
        {"date" : "2024-10-07", "product" : "iPhone 16 Pro"},
        {"date" : "2024-10-14", "product" : "Galaxy S24 Ultra"}
    ]
}
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(customer1, json_file, ensure_ascii=False, indent=4)

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "안유진", False])
wr.writerow([2, "장원영", True])
f.close()

dd = {
    "id" : "Hyauu",
    "pwd" : "^ghdxoghk18"
}

url = "http://localhost:8111/login"
headers = {"Content-Type" : "application/json"}

response = requests.post(url,data=json.dumps(dd),headers=headers)

if response.status_code == 200:
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print("데이터 전송에 실패했습니다. 응답 코드 : ", response.status_code)