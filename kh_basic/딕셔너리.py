# 딕셔너리 : 리스트와 튜플에서는 정수인 인덱스를 가지고 순차적으로 각 요소에 접근할 수 있었다면,
# 딕셔너리는 단어의 뜻 그대로 '사전'과 같이 별도의 키를 통해 각 요소에 접근 할 수 있도록 만들어진
# 데이터 타입 -> 키값으로 찾음
# 리스트 [] / 튜플 () / 딕셔너리 {}
# C++, 자바에서는 Map이라고 부른다

# 딕셔너리? 키로 값을 찾는 것
# {} 중괄호로 딕셔너리 선언
# 각 요소는 ,(쉼표)로 구분
# 키와 값은  콜론(:)으로 구분

# 선언 -> 딕셔너리 / 중괄호{} / 요소 쉼표 구분 -> 각 요소는 키와 값의 한쌍 구성 콜론(:)으로 구분
# 제이슨? -> 키와 벨류로 이루어짐 JSON - JavaScript Object Notation
# bit-O notation

coffee_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte" : 4000, "Moca" : 4500}
food_menu = {"Cake" : 5000, "Bakery" : 6000}

print(coffee_menu)
print(coffee_menu["Americano"]) # 딕셔너리 구조이기 때문에 [] 사이에 key 값을 넣어야 한다.
coffee_menu["ColdBrew"] = 5000
print(coffee_menu)

coffee_menu.update({"Americano" : 3000, "Espresso" : 3000, "Latte" : 4500, "Moca" : 5000})
print(coffee_menu)

del coffee_menu["Latte"] # 해당 명령으로 아이템 삭제
print(coffee_menu)
coffee_menu["Latte"] = 4200
print(coffee_menu)

dict1 = {"자바" : 80, "PHP" : 90, "HTML" : 70}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 값 추가, 삭제, 키 존재 여부 확인
food_menu["IceCream"] = 5000 # 새로운 키와 값 추가 # 추가시 맨 뒤에 붙음
print(food_menu)
print(food_menu.keys())
print(coffee_menu.get("Moca")) # get(키)함수로 값을 가져옴
if "Bakery" in food_menu:
    #print(f"Bakery price : {food_menu.values("Bakery")}")
    print(f"Bakery price : {food_menu["Bakery"]}")
else: print("해당 메뉴가 없습니다.")

# update() 함수 : 딕셔너리 테이터를 한꺼번에 변경할 때 사용

# 정보 얻기 : keys(), values(), items()
dict_lang = {"자바" : 99, "자바스크립트" : 80, "파이썬" : 92, "C++" : 89}
print(dict_lang.keys())
print(dict_lang.values())
print(dict_lang.items()) # 프린트 될 때 튜플 형태로 output 됨