# 함수
# 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램
# 함수는 매개변수를 가질 수 있으며, 반환값을 가질 수 있다.
# 일반적으로 식별자 뒤에 () 소괄호가 있으면 함수
# 매개변수와 함수의 호출하는 인자의 갯수는 일치해야 합니다.
# 리턴으로 함수의 결과값을 반환 # 반환을 한다는 것이 어떤 것일까?

# def 함수이름(매개변수) # 매개변수 -> 함수의 괄호 내부에 변수나 값을 넣는 것
# 실행할 코드
# return 변수

# 함수명(인수) -> 호출


# 함수 예제 (반복 호출)
# 매개변수는 넘겨 주지만 리턴이 없는 구조
def name_card(name, addr, phone):
    print(f"주소 : {addr}")
    print(f"전화번호 : {phone}")
    print(f"이름 : {name}")
    print("-"*30)

name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
name_card("가을", "서울시 권선구 권선동", "010-1234-1111")

# 매개변수를 넘겨주고 리턴값을 받는 구조

# def open_account(name):
#     print(f"{name}님의 계좌가 개설 되었습니다.")
#     return name
# def deposit(balance, input):
#     print(f"{input} 입급 되었습니다. 잔액은 {balance+input} 입니다.")
#     return balance+input
# def withdraw(balance, input):
#     if balance >= input:
#         print(f"출금 되었습니다. 잔액은 {balance-input} 입니다.")
#         return balance-input
#     else:
#         print(f"출금이 실패 했습니다. 잔액은{balance}입니다.")
#         return balance
# balance = 0 # 외부에서 선언된 변수 이지만 인수로 넘겨줘서 결과를 리턴 받음
# name = open_account("홍태화")
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}의 잔액은 {balance} 입니다.")

# 순차 검색과 이진 검색
### Pyhon 순차 검색 횟수
def search_list(a, x):
    for i in range(0, len(a)):
        if x == a[i]: return i
    return -1
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v,33))
print(search_list(v,18))
print(search_list(v,900))
print(search_list(v,42))

# 함수 선언 시 매개 변수에 대한 기본값을 정의 할 수 있습니다.
# 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출됩니다.

def profile(name, year = 2, age = 18, school = "태양고"): # year=2, age=18,school="태양고" -> 기본값 정의
    print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")
    return name

profile("나희도")
name = profile("홍태화")
print(name)
profile("고유림")
profile("백이진", None, 22)

# 가변 매개변수
# 함수 function 뒤에 ( ) 사이에는 필요한 매개변수 입력
# 함수의 매개변수 앞에 *(별표)를 붙여주면 함수의 매개 변수를 몇개를 입력하든 함수 내에서 튜플로 인식 한다.

def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}", end= " ") # 우선 이름 나이 입력 후 나머지는 뒤에 계속 붙게끔 입력
    for e in lang: # lang 매개변수가 단일 개수가 아니기 때문에 다음과 같이 입력
        print(e, end=" ") # lang을 받고 그대로 출력 / 줄바꿈 없이 계속 이어지게 end를 다음과 같이 입력 /for 구문 안에
    print() # 하나 끝나면 줄바꿈 위해 다음과 같은 입력 / for 구문 끝나면
profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
profile("조세호", 38, "Python", "Java",)
profile("유재석", 48, "Python", "Java", "C", "C++")

# 지역변수, 전역변수
# 전역변수로 선언된 변수를 함수내에서 사용하고자 할 때는 global 키워드가 필요

knife = 10
def game(player):
    global knife
    knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")
def game2(player, knife):
    knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")

player = int(input("경기에 참여하는 선수가 몇명 입니까? :"))
# game(player) # 함수 선언 -> game 함수
game2(player, knife) # 함수 선언 -> game2 함수

# 키를 입력 받아 표준 체중 구하기
# 반올림 함수에 대해 사용 해보기

def std_weight(height, gender):
    hm = height/100
    if gender == "남성":
        return hm*hm*22
    else:
        return hm*hm*21
height = int(input("키를 입력 : "))
gender = input("성별 입력 남성 / 여성 : ")
weight = round(std_weight(height, gender), 2) #,2 -> 소수점 2자리까지 출력? # round 함수?
print(f"키 : {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
