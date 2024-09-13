# 튜플은 시퀀스 자료형
# 이뮤터블(immutable) : 읽기만 가능
# () 또는 괄호가 없으면 튜플
# 패킹과 언패킹 동작을 지원함

person = "ㅎㅌㅎ", 28, "서울시 강남구 역삼동" # Packing 이라고 한다. # 괄호가 있든 없든 똑같음
print(type(person))

num = 1, # tuple
num = 1 # int

name, age, addr = person # Unpacking 이라고 한다.
print(addr)

def get_person():
    name = "ㅎㅌㅎ"
    age = 21
    addr = "서울시 강남구 역삼동"
    return name, age, addr # Packing

info = get_person()
print(info)

# 집합 -> 중복 제거할때만 사용

s1 =set([1,2,3,4,5])
print(s1)
print(type(s1))

s2 = {1,2,3,4,5} # 최근 집합 표시
s3 = {4,5,6,7,8,9,10}

# 합집합
print(s2.union(s3))
print(s2|s3)
# 교집합
print(s2.intersection(s3))
print(s2&s3)
# 차집합
print(s2.difference(s3))
print(s3.difference(s2))
print(s2-s3)
print(s3-s2)