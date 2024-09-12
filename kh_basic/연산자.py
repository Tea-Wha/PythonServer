# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술연산자 : +, -, *, /, //(몫), %(나머지), **(제곱연산자)

# i = 10
# j = 3
# print(i+j)
# print(i-j)
# print(i*j)
# print(i/j)
# print(i//j)
# print(i%j) # 나머지, 알고리즘 문제를 풀기 위해서 많이 사용
# print(i**j)
#
# TAX_RATE =0.10
# income = int(input("당신의 수입은 얼마 입니까?"))
# print(f"당신이 내야 할 세금은 {income * TAX_RATE}")

# 대입 연산자 : 값을 변수에 대입
# 대입 연산자의 종류 : =, +=, -=, *=, /=, %=

num1 = 10
num1 += 2 # num1 = num1 + 2
print(num1)
num1 -= 10
print(num1)
num1 *= 14
print(num1)


# 비교 연산자 : 두개의 값을 비교해서 참/거짓을 만들어 냄
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, <, <=
print(10>4)
print(10==4)

a = 10
b = 20
c = a>b
d = a<b
e = a==b
f = a>=b
g = a<=b
h = a!=b
print(c,d,e,f,g,h)

# 관계 연산자 :  and, or, not

x = 10
y = 20
z = 30

result1 = (x>0) and (x<y)
result2 = (x>0) or (x>y)
result3 = not((x>0) or (x>y))

print(result1, result2, result3, sep="^_^")

# 삼항 연산자는 -> 조건문이다
# 1. 삼항 연산자 2. switch/case 3. If

num = 100
flag = (num % 2 == 0) and '짝수' or '홀수' # and 앞에가 맞다면 (True) -> 뒤쪽의 연산자를 진행한다
print(flag)
# or 앞에가 맞다면 (True) -> 뒤쪽의 연산자를 진행하지 않는다
# 해석하자면 맨 처음이 맞고 2 번째가 맞다면 2 번째다
# 1이 맞다면 2 -> 3 순으로 넘어간다.
# 1이 맞고 2가 맞으면 True다
# 1이 맞고 2가 틀리고 3이 맞으면 True다.
# 1이 맞고 2가 틀리고 3이 틀리면 False다.
# 1이 틀리고 2가 맞고 3이 틀리면 False다.
# 1이 틀리면 -> 바로 3으로 넘어간다.
# 활용 방법은?
# 1을 비교 연산자 사용 -> True라면 바로 2로 출력하게끔 조정 가능?
# 1을 비교 연산자 사용 -> False라면 바로 3으로 출력하게끔 조정 가능?

num = 100
flag = (num%2 == 0 ) and (num%4 == 0 ) or (num%8 == 0)
print(flag)

num = 100
flag = (num%2 == 0 ) and (num%7 == 0 ) or (num%8 == 0)
print(flag)


num = 101
flag = (num%2 == 1) and '홀수' or '짝수'
print(flag)

# age = int(input("나이를 입력 하세요 : "))
# is_adult = age > 19 and "성인" or "미성년자"
# print(f"당신은 {is_adult} 입니다.")

print(bin(42))
print(oct(42))
print(hex(42))

# 비트 연산자 : 각 비트 끼리 연산
#

a = 10
b = a<<1
c = b<<1
print(a<<1)
print(f"b = {b}")
print("|{:5}|".format(10))
print("{:5}".format(10))
print("{:5}".format(b))
print(f"c = " "{:5}".format(c))
print(f"c = {c}")
print(bin(b))
print(bin(c))

a = 10 # 00001010
b = 12 # 00001100
c = (a&b) # 00001000
d = (a|b) # 00010110
e = (a^b) # 00000110
f = ~a  # 11110101  11110100  00001011
g = a<<1 # 00010100
h = a>>1 # 00000101

print(c,d,e,f,g,h)

#year = int(input("년도를 입력하세요 : "))
# flag =((year%4 ==0) and (year%400 ==0) and (year%100 !=0)) and "윤년이다." or "윤년이 아니다."
# flag = ((year%4 ==0) and ((year%400 ==0) or (year%100 !=0))) and "윤년이다." or "윤년이 아니다."

# year = int(input("년도를 입력 하세요 : "))
#
# if year % 4 == 0 and (year & 100 !=0 or year % 400 ==0):
#     print(f"{year}년은 윤년 입니다.")
# else :
#     print(f"{year}년은 윤년이 아닙니다.")