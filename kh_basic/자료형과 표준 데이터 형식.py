# 자료형 -> 데이터 형태
# 문자열 -> " "  (문자형은 따로 존재 X) -> 문자열로 변환할 때는 : str -> 문자와 문자열 구분 X
# 숫자 -> 정수형, 실수형 -> 정수 : int / 실수 : float
# Boolean -> 참 / 거짓 -> : bool
# 모든 것이 참조 타입이어야만 -> 객체지향? -> 참조 타입은 어떤것?
# 변수에 값을 대입하는 연산자 =

# 정적 -> 미리 데이터 타입 선언해야함
# 동적 -> 데이터 타입이 알아서 결정됨

addr = "서울시 강남구 역삼동" # 문자열
lang = "파이썬" # 문자열
name = "홍태화" # 문자열
age = 29 # 정수형

print("나의 이름은 " + name + "입니다. ") # 이 경우에는 문자열에 문자열 변수를 추가하는 것이기 때문에 
# 자료형의 변환이 필요 없다.
print("나이는" + str(age) + "입니다. ") # 이 경우에는 문자열에 정수형 변수를 추가해야 하기 때문에
# 자료형의 변환이 필요하다 -> str(변수)

# 기존에 선언된 변수는 뒤에서 변경이 가능하다
print(f"{addr} 에서 {lang}을 배우고 있습니다.")

a = b = c = 1
print(a, b, c, sep="")
print(a,b,c)

a, b, c = 1, True, "곰돌이"
print(a,b,c)

# 변수의 타입 확인 : type()
print(type(a))
print(type(b))
print(type(c))
