# 리스트 -> 원소들이 연속적으로 저장되는 형태의 자료형 (크기 지정 필요 X)
# 배열과 다르게 크기를 지정할 필요가 없음
# 읽고 쓰기 가능 (뮤터블)
# 같은 자료형일 필요가 없음
# [] 대괄호로 표시


# 저장되는 요소들이 모두 같은 자료형일 필요 없음
# 뮤터블 객체 (읽고 쓰기 가능)
# 튜플 -> 읽기만 가능 (이뮤터블 객체)

# 파이썬은 기본적으로 배열이 없는 언어 -> 하지만 배열이 필요한 경우가 존재
# 1. 고정된 크기의 데이터를 다루어야 할 때
# 2. 수치 연산
# 3. 다차원 배열
# 4. 속도가 중요한 경우

numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'apple', True, 3.14, 200, ['seoul', 'city'], ['1', 2, False]]

print(numbers)
print(fruits)
print(mixed)
print(mixed[6])
print(((mixed[5])[1]))
print(mixed[6][2])
print(mixed[5][1][3]) # bool 타입은 안됨 # 정수 타입도 안됨 # 문자열만 가능
print(mixed[6][:2])
print(mixed[0:5])

# 리스트 연산자 : +, *
# 연산자 overloading
a = [1, 2, 3]
b = [4, 5, 6]

print(a+b)
print(a*3)

# 리스트 요소 추가하기 : apped(), insert() - 내부 메서드
# append(값) : 리스트의 마지막에 값을 추가
# insert(인덱스, 값) : 해당 인덱스(위치)에 값을 추가 / 기존의 값을 뒤로 민다.

list_a = [1, 2, 3, 5, 4, 5, 5, 5]
list_a.insert(1,10)
print(list_a)
list_a.append(6)
print(list_a)

# 리스트 제거 : pop, remove, clear - 내부 메서드 / del -> 함수
#  pop() : 인덱스를 쓰지 않으면, 마지막 인덱스를 값 반환(print 시에만) 하고 값을 삭제
# 인덱스 입력시 해당 인덱스의 값 반환(print 시에만)하고 값을 삭제 (print 찍을 시 삭제할 값 반환)
print(list_a.pop())
print(list_a)
print(list_a.pop(2))
print(list_a)

# remove(값) : 해당하는 값을 지움, 값이 여러개인 경우는 인덱스가 낮은 것을 지움
list_a.remove(5)
print(list_a)

del list_a[0] #인덱스로 값을 제거
print(list_a)

list_a.clear() # 모든 값 제거
print(list_a)

# 중복 제거 하기
list_double = ["A", "B", "C", "D", "A", "D"]
list_new = []
for e in list_double:
    if e not in list_new:
        list_new.append(e)
print(list_new)

# 리스트의 순회
names = ["A", "B", "C", "D", "E"]
for name in names:
    print("아이브 멤버 : ", name, end=" ")
print()
print(type(name))
for i in range(len(names)):
    print("아이브 멤버 : ",names[i], end=" ")
print()
print(type(i))
for e in range(5):
    print("아이브 멤버 : ",names[e], end=" ")
print()
print(type(e))
