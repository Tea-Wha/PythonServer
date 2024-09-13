# 시퀀스 자료형의 값을 모두 더해줌
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4])/5)

# 몫과 나머지를 반환  - divmod
# 파이썬 -> 반환값이 여러개 나올 수 있음 (패킹/언패킹이 비교적 자유로움)
# 몫과 나머지를 반환, 튜플 형태로 반환(unpacking)
# () -> 튜플
# 내부 메서드 와 내장함수는 다름
print(divmod(sum([1,2,3,4,5]),5))

# 정렬
# 정렬과 검색이 중요함
# O(1) / O(logn) ?
my_list = [1, 5, 66, 34, 53, 432, 80, 45, 32, 13, 45, 76]
print(sorted(my_list)) # 오름차순 정렬
print(sorted(my_list, reverse=True)) # 내림차순 정렬
print(len(my_list))

import random
for e in range(0,4):
    print(random.random(),end=" ")
    print()
    
# 실습

# n = list(map(int, input("정수 입력 : ").split()))
# 입력 받은 값에서 제일 큰 값
# 입력 받은 값에서 제일 작은 값
# 총점
# 평균
# 해당 리스트(n)를 5로 나눈 몫과 나머지

# n = list(map(int, input("정수 입력 : ").split()))
# print(max(n))
# print("최대값 :" + str(max(n)))
# print("최대값 :" , str(max(n)))
# print(f"최대값 : {max(n)}")
# print(min(n))
# print(sum(n))
# print(sum(n)/len(n))
# print(divmod(sum(n),5))

# 외장함수는 import 해서 사용하는 함수, 파이썬 기본적으로 제공하는 것, 외부모듈
# 랜덤 함수 : 지정한 범위내에서 임의의 숫자를 만들어 내는 것

import random

# rand = random.randint(0,4) # 0 ~ 4 까지의 임의의 값을 생성 # 미만 개념 포함 X

for i in range(10):
    rand = random.randint(0, 4)
    print(rand, end=" ")
print()


# 중복되지 않는 로또 번호 생성 : 1~45 사이의 임의의 수 6개
#  리스트를 사용하고, 리스트내에 임의로 생성한 번호가 있으면, 추가 하면 안됨
# 몇번의 중복이 발생할지 알 수 없기 때문에

# import random
#
# for i in range(6):
#     rand = random.randint(1,45)
#
#     print(rand, end=" ")
# print()

print("로또 번호 자동 생성 :", end=" ")
# lotto = []
# while True:
#     rand = random.randrange(1,46)
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6: break
# print(lotto)

lotto = set()
while len(lotto) <= 6:
    rand = random.randrange(1,46)
    lotto.add(rand)
print(lotto)

import random
lotto_number = random.sample(range(1,46),6)
print("로또 번호 자동 생성 : ", sorted(lotto_number))

