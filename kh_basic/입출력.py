# 표준 입출력 : 콘솔 입출력을 의미
# [] 대괄호 : 리스트를 표시
# {} 중괄호 : 딕셔너리 표시
# () 소괄호 : 함수의 input, 튜플
from time import sleep

# print() : 화면출력을 위한 함수
print(36)
print("문자열")
print([1,2,3]) # 리스트 출력
print("파"+"이"+"썬") # + 문자열을 이어주는 연산자
print("파","이","썬", sep=" ") # , separator -> 구분자 의미 -> 구분자의 기본 값은 공백
# separator는 따로 설정이 가능 (위와 같이) [sep=""]
print("파""이""썬""\b")

# 이스케이프 문자 : 출력 구간의 흐름을 제어
# \n(줄바꿈), \t(탭을 의미), \b(백스페이스), \r(커서를 맨 앞으로 돌림)
# end의 기본 의미는 "\n" (줄바꿈)

print("Banana")
print("", sep=" ", end="\n") # 기본 설정
print("\n")
print(34)

print(35)
print(36, sep="", end="")
print(37)

print("Banana\b")
print("Banana\rApple")
print("Banana","Apple","Mango", sep="$")

year = 2024
month = 9
day = 10
print(f"{year}",f"{month}",f"{day}", sep="-")
print(year,month,day,sep="-")
# sep="" -> , 에 들어가는 의미 부여 기본은 " "


# import time
# for i in range(1, 101):
#    time.sleep(1)
#    print(f"\r{i}%", end="")

# 출력 스타일 정리
name = "홍태화"
age = 29
gender = "남성"
job = "개발자"
addr = "서울 특별시"

# 서식지정자 스타일 (C언어 방법)
print("========서식 지정자 스타일========")
print("이름 : %s 성별 : %s"%(name, gender)) # C언어
print("나이 : %d"%age) # C언어
print("주소 : %s"%addr)

print("이름 : {} {}".format(name, addr)) # 파이썬 예전 방식
print(f"이름 : {name}") # 파이썬 최근 방식
print(f"이름 : {name}", f"주소 : {addr}")
print(f"이름 : {name} 성별 : {gender} ")

# 문자열 연결 연산자 사용 방식
print("이름 : " + name)
print("나이 : " + str(age))

# 정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.141592

print(num1)
print(num2)
print(num3)
print(num4)

print("{:3}".format(num1)) # print만 찍을 때 뒤쪽에 .format()

print(f"{num1:5}")
print(f"{num2:5}")
print(f"{num3:5}")
print(f"{num4:5}")

print(f"{num1:<5}")
print(f"{num2:<5}")
print(f"{num3:<5}")
print(f"{num4:<5}")

print(f"{num5:.2f}") # 반올림
