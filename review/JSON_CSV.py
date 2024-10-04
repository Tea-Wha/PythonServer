# JSON(JavaScript Object Notation) -> 데이터를 표현하고 전송하기 위한 경량의 데이터 형식
# json 모듈 -> JSON 데이터 파싱 / JSON 객체 생성 / 파이썬 데이터 타입 -> JSON 직렬화 기능 제공
# JSON 데이터를 파싱하여 파이썬 객체로 변환하려면 json 모듈의 loads() 함수 사용

# JSON 인코딩 (직렬화)
# Python Object(Dictionary, List, Tuple 등)를 JSON 문자열로 변경하는 것 

import json

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