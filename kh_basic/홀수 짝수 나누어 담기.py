# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제

# list_a = list(map(int, input("무작위 수 입력 : ").split()))
#
# c=[]
# d=[]
# for e in range(len(list_a)):
#     if list_a[e]%2 == 0:
#     c.append((list_a[e])
#     else:
#     d.append(list_a[e])
# print(c)
# print(d)

# number = list(map(int, input("입력 : ").split()))
# even = []
# odd = []
#
# for e in number:
#     if e % 2 == 0: even.append(e)
#     else: odd.append(e)
#
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")

number = list(map(int, input("입력 : ").split())) # map -> 정수 변환(?)
odd = list(filter(lambda x: x%2 == 1, number)) #filter -> 걸러냄 (결과가 참인 것만)
even = list(filter(lambda x: x%2 == 0, number)) # lambda -> 짧은 1회성 함수 만들어서 사용 가능한 함수
print(f"홀수 :  {odd}")
print(f"짝수 : {even}")