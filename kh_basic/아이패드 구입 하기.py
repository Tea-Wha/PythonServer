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
            return sel # return sel이 의미하는 바는 무엇인가? # sel은 input에 의해 받아지기 때문에 -> 문자열?

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
    make_cnt += 1 # 어떤 조건일 때 1씩 증가하는 것인가? # 구입 대수만큼 증가
    print_screen = ("", "11인치", "12.9인치") # 튜플 -> 인덱스 접근 가능
    print_color = "", "스페이스그레이", "실버"
    print_memory = "", "128", "256", "512", "1024"
    print_network = ("", "Wi-Fi", "Wi-Fi+Cellular")
    serial_screen = (screen == "1") and "11" or "13"
    serial_network = (network == "1") and "W" or "C"
    serial_date = str(datetime.today().year)+str(datetime.today().month)+str(datetime.today().day)
    serial_number = "iPad"+serial_screen+serial_network+serial_date+str(make_cnt)
    print("iPad Pro가 출고 되었습니다.")
    print("="*34)
    print(f"화면 크기 : {print_screen[int(screen)]}") # print_screen 튜플에서 인덱스 표기 방식으로 표현
    print(f"제품 색상 : {print_color[int(color)]}")
    print(f"제품 용량 : {print_memory[int(memory)]}GB")
    print(f"네트워크 : {print_network[int(network)]}")
    print(f"이름 : {name}")
    print(f"시리얼넘버 : {serial_number}")
    print("-"*34)

while True: # 앞쪽에 함수 전부 설정하고 전체 돌리는 과정 # 메인 코드
    is_continue = choice_pad() # choice_pad 함수 run
    if is_continue == "2":
        print("iPad Pro 구입을 종료 합니다.") # choice_pad 함수 종료하기 시 -> 종료
        break
    screen = select_screen() # make_ipad 함수의 screen 설정 / 함수 run # 함수 run 순서에 따라 순차적으로 진행
    color = select_color() # make_ipad 함수의 color 설정 / 함수 run
    memory = select_memory() # make_ipad 함수의 memory 설정 / 함수 run
    network = select_network() # make_ipad 함수의 network 설정 / 함수 run
    name = select_name_service() # make_ipad 함수의 name 설정 / 함수 run
    make_ipad(screen, color, memory, network, name) # make_ipad 함수 run 
    # 앞서 돌린 값들 전부 make_ipad 함수에 적용 
    