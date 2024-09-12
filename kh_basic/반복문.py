# While 문 -> 조건이 참인 동안 반복 수행 / 탈출 조건 -> 수행 종료
# 실수 표현은 Switch case 문과 같은 조건 비교를 할 때 사용 불가능 하다?
# 횟수가 정해지지 않은 부분 -> while 문
# 횟수가 정해진 부분 -> for 문

# n = int(input("정수를 입력 하세요 : "))
# sum = 0 # 초기값 설정 /  값을 누적하기 위한 변수 (초기값 필요)
# while n:  # 0을 제외한 모든 것을 다 참으로 받아들임  -> 0 은 거짓/나머지는 참
# # 자바에서는 조건식이 필요하다 (참 거짓 조건식)
#     sum += n
#     n -=1
# print(sum)

# 탈출 조건 -> n이 0이 될 때

# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n+1): # 범위 기반의 for 문 # 범위 지정 시 종료 값은 항상 미만의 개념이 있음
#     sum += i
# print(sum)

# while문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용

# while True:
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200: break # 정상적인 입력이므로 반복문 탈출 (break)
#     else : print("나이 입력 범위를 벗어 났습니다.") #True일 때 까지 작동
# 
# print(f"당신의 나이는 {age} 입니다.")
# break가 걸려서 else를 굳이 안넣어도 됨

# while True: -> 변수가 바뀔 일이 없음 (변수가 아님) -> 무한 반복이 걸리는중 (조건식으로 빠져나가지 못함)
# while 1:  -> 변수가 바뀔 일이 없음 -> 반복문 탈출 -> break 
# 위의 2 case는 반복문 내에 탈출 조건이 있어야 함 -> 이상 조건이 계속 들어온다면 정상 조건이 들어올 때까지
# 계속 반복해야 한다 -> while -> 정상 조건이 들어왔을 때 -> break -> 즉 추가 조건이 필요하다?

# while True: # 추가 조건 필요
#     energy = 0
#     print("1. 다른 누군가에게 발상, 지식이나 감정을 표현함으로써 에너지를 얻고 활동적이며 적극적입니다.")
#     print("2. 지식이나 감정에 대한 자각의 깊이를 늘려감으로써 에너지를 얻고 깊이 있는 대인 관계를 가집니다.")
#     print("[에너지 방향] : 1, 2중에 선택 하세요 : ", end=" ")
#     energy = input()
#     if (energy == '1') :
#         mbti = "E"
#         break
#     elif (energy == '2') :
#         mbti = "I" # 문자열
#         break
#     else: print("입력 오류 다시 입력 하세요.")

# for 문 : 정해진 범위 만큼을 반복 수행 할 때 효과적
# for 요소 in 시퀀스 : 시퀀스 자료에  대한 자동 순회

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits :
#     print(fruit, end="\n")
#
# name = "asdasdasd"
# for e in name:
#         print(e, end="-")
#
# for e in input("문자열 입력 : "):
#     print(e, end="-")


# for 인덱스 in range (시작값, 종료값, 증감값) :

# n = int(input("정수 값 입력 : "))
# sum = 0
# for i in range(1, n+1): # 시작값이 0인 경우 생략 가능, 증감값이 1인 경우 생략 가능
#     sum +=i
# print(sum)

# 이중 for 문 사용 하기
# n = int(input("정수 입력 :"))
# for i in range(0,n):
#     print(f"i={i} |", end="")
#     for j in range(0,n):
#         print("*", end=" ")
#     print()

# 이중 for문 구구단 찍기
# for i in range(2, 10): # 2단 ~ 9단
#     for j in range(1, 10):
#         print(f"{i} x {j} ={i*j}")
#     print("-"*20)

# n = int(input("정수 입력 :"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()
#
# n = int(input("정수 입력 :"))
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*", end=" ")
#     print()

# n = int(input("정수 입력 :"))
# for i in range(n, 0-1, -1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()



# 제어문 : break, continue
# break : 반복문을 탈출 할 때 사용
# continue : 아래의 문자를 수행하지 않고 반복문의 조건식으로 이동, (해당 루틴은 수행된걸로 간주)
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: continue # 짝수이면 아래의 문장을 수행하지 않음
#     print(i)
# 
# 반복문을 반대로 수행하기
# n = int(input("정수 입력 : "))
# for i in range(n, 0-1, -1): # 다음과 같이 역순이 가능하다?
#     print(f"인덱스 : {i}")

# for문으로 알파벳 출력 하기
# ASCII code
# chr() : 유니코드를 입력받아 그 코드에 해당하는 문자를 출력
# ord() : 문자의 유니코드 값을 돌려주는 함수

for i in range(ord("A"), ord("z")+1):
    print(chr(i), end= " ")
print()

for i in range(65,91):
    print(chr(i), end= " ")
print()

