# 아이패드 구입 하기
# 현재 시간 및 날짜 가져오는 내장 함수 사용
# 전역 변수 사용
# 함수 리턴값 사용
# 시리얼넘버란? -> 제품의 고유번호이며 유일한 값 -> 아래의 코드의 예제와 같이 만들어짐

# 아이패드 만들기
from datetime import datetime # 날짜와 시간을 사용하기 위해서
make_cnt = 0 # -> 전역 변수

def choice_pad():
    while True:
        print("<< iPad Pro 구입하기 >>")
        print("[1]구입하기 [2]종료하기")
        sel = input("메뉴를 선택하세요 : ")
        if sel == "1" or sel == "2":
            return sel # return sel이 의미하는 바는 무엇인가?

def select_screen():
    while True:
        print("[1]11인치 [2]12.9인치")
        sel = input("디스플레이를 선택 하세요 : ")
        if sel == "1" or sel == "2":
            return sel # return sel이 의미하는 바는 무엇인가?

def select_color():
    while True:
        print("[1]스페이스그레이, [2]실버")
        sel = input("컬러를 선택 하세요 : ")
        if sel == "1" or sel == "2":
            return sel # return sel이 의미하는 바는 무엇인가? # 함수의 결과값 반환

def select_memory():
    while True:
        print("[1]128GB, [2]256GB, [3]512GB, [4]1TB")
        sel = input("용량을 선택 하세요 : ")
        if sel == "1" or sel == "2" or sel == "3" or sel == "4":
            return sel

def select_network():
    while True:
        print("[1]Wi-Fi, [2]Wi-Fi+Cellular")
        sel = input("네트워크를 선택 하세요 : ")
        if sel == "1" or sel == "2":
            return sel

def select_name_service():
    print("[1]각인 서비스 신청, [2]신청 안함")
    sel = input("각인 서비스를 선택 하세요 : ")
    if sel == "1": name = input("이름을 입력 하세요 : ")
    else: name = "NONE"
    return name

def make_ipad(screen, color, memory, network, name):
    global make_cnt
    make_cnt += 1
