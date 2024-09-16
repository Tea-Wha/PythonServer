# 재귀 함수 -> 함수내에서 자기 자신을 호출하는 구조
# 알고리즘 구현 시 많이 사용 (정렬, 검색 등)
# 1~n까지의 합을 구하는 여러가지 방법(for,등차수열,재귀)

def for_sum(a):
    sum = 0
    for i in range(1, a+1): # 1부터 a까지
        sum += i
    return sum

def while_sum(n):
    sum = 0
    while n: # n이 0이 될때까지 반복 # n이 0 초과이면 True
        sum += n
        n -= 1
    return sum

def while2_sum(n):
    sum = 0
    while True:
        sum += n
        n -= 1
        if n == 0: break
    return sum

def gaus_sum(a):
    return int(a*(a+1)/2)

def recu_sum(a):
    if a == 1: return 1
    else: return a + recu_sum(a-1)

# a = int(input("정수 입력 : "))
# print(for_sum(a))
# print(while_sum(a))
# print(while2_sum(a))
# print(gaus_sum(a))
# print(recu_sum(a))

# 튜플과 함수
# 튜플은 함수의 리턴에 많이 사용된다.
# 다른 언어에서는 리턴으로 값을 되돌려줄 때 한개의 값만 전달할 수 있지만 파이썬에서는 여러개의 값으로
# 튜플을 이용하여 전달 가능 (패킹/언패킹)

def swap_func(a,b):
    tmp = a # tmp 값에 a 값 저장
    a = b # a 값에 b 저장 (b값으로 변경)
    b = tmp # 기존에 저장한 tmp(=a) 값을 b에 저장
    return (a,b) # 파이썬은 a,b = b,a 로 간단하게 표현 가능
a, b = swap_func(10,20)
print(a,b)

def func_square(x,y):
    return x*x, y*y

x,y = map(int,input("x,y : ").split(":"))
print(func_square(x,y))

# 람다 -> 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현