# 주석은 인터프리터 (번역) 하지 않는 영역
print("파이썬을 공부하겠습니다.") # 이 부분은 주석 입니다.
print(100) # 정수값 출력
print(33.3333) # 실수값 출력
print(100+200) # 연산자 사용
print(100 < 200) # True

# 정적 언어 -> 값에 따른 데이터형 직접 타이핑 필요
name = "홍태화" # 파이썬은 동적 언어 -> 값이 대입 될 때 데이터형이 알아서 결정
# -> 불리한 점도 있음 -> Error 잡지 못함 (컴파일 시기에) (아무 값이나 들어올 수 있음) -> TypeScript 필요?
# ''  "" 구분하지 않음 -> 둘 다 문자열의 의미, 파이썬 문자를 따로 구분하지 않음
# == 같다, = 값을 변수에 대입한다는 의미
print(name)
# 파이썬은 상수 없음
"""
범위 주석
 * 식별자 생성 규칙
 * 키워드(예약어) 사용 금지
 * 특수문자는 _(언더바)만 사용 가능
 * 숫자는 사용 가능하지만, 맨 앞 불가능
 * snake_case : 스네이크 표기법, 단어와 단어를 연결할 때 _ 사용 (변수 또는 함수 이름) (관습법) (파이썬 사용) (C 사용)
 * camelCase : 첫 단어 소문자, 두번째 단어 대문자 (자바에서 사용) (C 사용)
 * PascalCase : 각 단어 -> 대문자 (클래스 이름)
 * 예약어나 키워드는 주황색
"""
'''
범위 주석
'''

name = "홍태화"
email = "htw7880@gmail.com"
phone = "010-4224-7880"
addr = "서울특별시 중구 동호로 25길 37-5"
position = "student"

# f -> format / format 구간에서 {} 안에는 변수
print(f"""
    이름 : {name}
    이메일 : {email}
    전화번호 : {phone}
    주소 : {addr}
    직책 : {position}
""")

#절차지향언어 -> 위에서 아래로 순차적 진행 (C, 파이썬)
#객체지향언어 -> 실제 세계 모델링화하여 객체를 만드는 것 (병렬?) (자바)
