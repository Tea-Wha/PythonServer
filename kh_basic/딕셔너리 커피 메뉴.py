# 시퀀스 -> 순서 보장 / list -> index
# Hash function -> 임의의 값이 정해지지만 순서는 일정하지 않다 
# 딕셔너리의 경우 -> 순서는 보장하지 않는다? -> Key와 Value는 보장된다
# 커피 메뉴 만들기
# [1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 불러오기 [6] 저장하기[7] 종료하기
# 기본 메뉴 만들기
# 카테고리별 조회 추가하기
import json


menu = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."], # 리스트 형태로 추가?
    "Espresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}
file_name = "menu.json"

# 파일에서 매뉴를 읽어오는  함수
def load_menu():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 없습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")
        
 # 파일에 저장하는 함수
def save_menu():
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)

# [1] 메뉴 보기
def print_menu() :
    #for key in menu:
            #print(f"{key} : {menu[key]}")
    for key, value in menu.items():
        print(f"{key} : {value}")

# [7] 카테고리 메뉴 보기
def print_category_menu(cate):
    for key,value in menu.items():
        if value[0] == cate:
            print(f"{key} : {value}")

# [2] 개별 메뉴 조회
def get_menu(key):
    if key in menu:
        print(menu[key])
    else:
        print("찾는 메뉴가 없습니다.")
print(get_menu)

# [3] 메뉴 추가
def add_menu(key, category, price, desc): #key, 분류, 가격, 설명
    if key not in menu: # 해당 키에 대한 메뉴가 없음
        menu[key] = [category, price, desc]
        print(f"{key} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재 합니다.")
        
# [4] 메뉴 삭제
def del_menu(key):
    if key in menu:
        del menu[key]
        print(f"{key} 메뉴가 삭제 되었습니다.")
    else:
        print("삭제할 메뉴가 없습니다.")

while True:
    print("메뉴를 선택 하세요 : ")
    sel = input("""[1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 불러 오기 [6] 저장 하기 
                [7] 분류별 보기 [8] 종료 하기 : """)
    if sel == "1":
        print_menu()
    elif sel == "2":
        key = input("조회 할 메뉴를 입력 하세요 : ")
        get_menu(key)
    elif sel == "3":
        key = input("추가 할 메뉴를 입력 하세요 : ")
        cate = input("카테고리 입력 : ")
        price = int(input("가격 입력 :  "))
        desc = input("제품 설명 : ")
        add_menu(key, cate, price, desc)
    elif sel == "4":
        key = input("삭제할 메뉴를 입력 하세요 : ")
        del_menu(key)
    elif sel == "5":
        menu = load_menu()
    elif sel == "6":
        save_menu()
    elif sel == "7":
        cate = input("조회 할 카테고리를 입력 하세요 : ")
        print_category_menu(cate)
    elif sel == "8":
        print("초기 화면으로 돌아갑니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")