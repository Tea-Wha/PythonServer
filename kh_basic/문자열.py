from astropy.io.fits.scripts.fitsheader import print_headers_traditional

s_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 시퀀스 자료형
print(s_list)
# sequence[start:end:step] step -> 기본값 = 1 start는 0부터

# 자료형 -> 데이터 형태
# 문자열 -> " "  (문자형은 따로 존재 X) -> 문자열로 변환할 때는 : str
# 숫자 -> 정수형, 실수형 -> 정수 : int / 실수 : float
# Boolean -> 참 / 거짓 -> : bool

# 문자열이란? 문자로 이루어진 데이터의 집합
#  " ", ' ', """ """, ''' '''
# 인덱싱 : 시퀀스(리스트, 튜플, 문자열, input()) 자료형에서 특정 위치 요소를 선택하는 작업
# 슬라이싱 : 시퀀스 자료형에서 일부 데이터를 추출하는 것

# #jumin = input("주민등록번호 입력 : ")  # 991120-1234567
#
# gender = jumin[7]
# if gender == "1" or gender == "3":
#     print("남성 입니다.")
# else:
#     print("여성 입니다.")
# # 태어난 년도를 구하기 위해서 슬라이싱
# year = jumin[0:2]
# year = int(year)
# # if year < "24":
# #     print("태어난 년도는 20" + year + "년 입니다.")
# # else:
# #     print("태어난 년도는 19" + year + "년 입니다. ")
# if gender == "1" or gender == "2":
#     year += 1900
# else :
#     year += 2000
# print(f"태어난 년도 : {year}")
#
# # 생일 출력
#
# # print(f"생년월일 : {jumin[2:4]}월 {jumin[4:6]}일")
# month = jumin[2:4]
# print(month)
# print(type(month))
# month = int(month)
# print(month)
# print(type(month))
#
# print("생년월일 : " + jumin[:6]) # 이것이 되는 이유는 input이 문자열로 인식되고 지금 대입되는 곳이 문자열이기 때문에
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 : " +jumin[-7:]) # -1은 맨 뒤자리

life = "Life is too short, You need Python"
tmp = life[0] + life[1] + life[2] + life[3]
print(tmp)

# 메모리 저장 공간 -> Static/Heap/Stack
# 동적 영역 -> Heap
# 변수에 저장된 문자열 -> Static에 저장 및 박제되어 있음 -> 변경 불가능
# life (변수) -> Stack에 저장 -> 참조되는 부분은 static에 있음


# 대소문자 바꾸기 : upper(), lower()
a = "Hello Python Program."
print(a.upper())
print(a.lower())
print(a[0:4].upper()+a[4:])

# 대문자는 소문자로 소문자는 대문자로 변경
print(a[0].lower())

# 문자열 변경 : replace("기존 문자열", "바꿀 문자열")
# 문자열 변경 : replace("기존 문자열", "") -> 기존 문자열 삭제
# 기본적으로 바꿀 변수의 뒤에 .함수 를 통해 사용

input_str = "Hello Python Program"
new_str = input_str.replace("Python", "JavaScript")
print(new_str)
print(input_str)


# 문자열에 포함된 문자 갯수 세기 및 문자열 길이 구하기
# count() : 문자열 내장 함수로 문자열에 포함된 문자의 갯수 확인 및 반환  -> 내장 함수 -> 메서드
# __len__() : 문자열 내장 함수로 문자열의 길이 반환 -> down slash 두번 
# 내장 함수는 변수.(함수) 형태로 나타내지는 것을 의미하는 것 같음
# len() : 길이 반환 함수
print(input_str.count("1"))
print(input_str.count("l"))
print(len(input_str))
print(input_str.__len__())

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 부분 문자열의 시작 인덱스 반환 -> 찾지 못하면 -1 반환
# index() : 찾은 부분 문자열의 시작 인덱스 반환 -> 찾지 못하면 ValueError 발생하고 종료됨
# rfind() : 뒤에서 부터 문자열을 찾음 -> 찾은 문자열의 인덱스는 앞에서 부터 계산

p = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(p.find("가장")) # 가장 (가) 첫번째 인덱스 출력
print(p.rfind("가장"))
print(p.index("포기"))

print(p.find("나에게"))
#print(p.index("나에게"))

new_p = p.replace("가장","나에게")
print(new_p)

# 문자열 연산자 : +, *
# def sum_ex(x, y):
#     return x+y
# 
# print(sum_ex(100,200))
# print(sum_ex(3.14,5.88))
# print(sum_ex("KOREA","SEOUL"))

print("태양고" + "나희도")
print("!"*10)
list_1 = [0] * 10
print(list_1)

# 문자열 양옆의 공백제거 : strip()

d ="""
    안녕하세요,
    문자열의 공백을 제거 하겠습니다.
    ㅇㅇㅇ...
"""
# 로그인 창에서 사용 -> 공백 때문에 -> 공백 제거에 사용 가능
print(d)
print(d.strip())