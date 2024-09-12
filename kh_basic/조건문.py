# 제어문이란? 조건문과 반복문의 의미

# num = int(input("정수값 입력 : "))
# 
# if num > 100:
#     print(f"{num}은 100 보다  큽니다.")
# elif num == 100:
#     print(f"{num}은 100 입니다.")
# else:
#     print(f"{num}은 100 보다 작습니다.")


# 실습문제
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력했다고 표기
# 성적이 0~100 사이, 90 점 이상이면 A
# 80점 이상이면 "B"
# 70점 이상이면 "C"
# 60점 이상이면 "D"
# 나머지는 "F"

#grade = int(input("성적 입력 :"))

# if grade > 100 or grade <0:
#     print("성적을 잘못 입력했습니다.")
# elif 90 <= grade:
#     print("성적은 A 입니다.")
# elif 80 <= grade:
#     print("성적은 B 입니다.")
# elif 70 <= grade:
#     print("성적은 C 입니다.")
# elif 60 <= grade:
#     print("성적은 D 입니다.")
# else:
#     print("성적은 F 입니다.")


# if 0 <= grade <= 100: # 중첩 if 문
#     if grade >= 90: print("A") # 순차적으로 내려오기 때문에 코드를 구성할 때 조건을 잘 살펴보고 코드를
#     elif grade >= 80: print("B") # 짜야 한다
#     elif grade >= 70:  print("C")
#     elif grade >= 60: print("D")
#     else: print("F")
# else:
#     print("성적을 잘못 입력 하셨습니다.")

# 세자리 정수를 입력  받아 100의 자리, 10의 자리, 1의 자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else 값 비교

# 조건 1. 세 자리의 정수는 모두 다른 값을 가집니다.
# n = int(input("세 자리 정수 입력 : "))
# a = n//100 # 100의 자리
# b = (n-(a*100))//10 # 10의 자리
# c = (n-(a*100)-(b*10))//1 # 1의 자리
#
#
# if a > b  > c or a > c > b: print(a)
# elif b > a > c or b > c > a: print(b)
# else: print(c)

# n = int(input("정수 입력 : "))
# a = n//100
# b = (n%100)//10
# c = n%10
#
# if a >b:
#     if a>c : print(a)
#     else : print(c)
# else:
#     if b>c : print(b)
#     else : print(c)



while True:
    grade = int(input("성적 입력 :"))
    if 0 <= grade <= 100: # 중첩 if 문
        if grade >= 90: print("A") # 순차적으로 내려오기 때문에 코드를 구성할 때 조건을 잘 살펴보고 코드를
        elif grade >= 80: print("B") # 짜야 한다
        elif grade >= 70:  print("C")
        elif grade >= 60: print("D")
        else: print("F")
        break
    else: print("성적을 잘못 입력 하셨습니다.")

