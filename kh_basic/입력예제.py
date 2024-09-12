# 사용자에게 콘솔로 입력을 받아 변수에 대입
# input() 함수를 사용
# input() 함수는 문자열로 입력을 받음

# print("이름을 입력하세요 : ", end="")
# name = input("이름을 입력 하세요 : ")
# print(f"당신의 이름은 {name} 입니다.")

# 정수 타입으로 변수에 값을 대입하기 위해서는 형 변환이 필요
# age = input ("나이를 입력 하세요 : ")
# age = int(input("나이를 입력 하세요 : "))
# print(f"당신의 현재 나이는 {age} 입니다.")
# print(f"10년 뒤 당신의 나이는 {age+10} 입니다.")

# 이름, 나이, 주소, 직업, 성적(실수 타입)를 입력 받아 출력 하기

#name = input("이름을 입력 하세요 : ")
# print(f"당신의 이름은 {name} 입니다.")
#age = int(input("나이를 입력 하세요 :"))
# print(f"당신의 나이는 {age} 입니다.")
#addr = input("주소를 입력 하세요 :")
# print(f"당신의 주소는 {addr} 입니다.")
#job = input("직업을 입력 하세요 :")
#score = float(input("성적을 입력 하세요 :"))
# print(f"당신의 성적은 {score} 입니다.")

#print(f"안녕하세요? \"{name}\"님")  # 코드 내에서  \"
# print(f'안녕하세요? "{name}"님')  # 코드 내에서  \"
#print(f"당신의 주소는 {addr}이고 직업은 {job}이고 나이는 {age} 입니다.")
#print(f"당신의 성적은 {score:.2f} 입니다.")


# 국어 영어 수학 과학 성적을 공백 기준으로 입력 받아 총점과 평균 구하기
#
# kor, eng, mat, sci = map(int, input("성적 입력 : ").split()) # 띄어쓰기 되면 바로 에러 남
#
# print(f"총점 : {kor + eng + mat + sci}")
# print(f"평균: {(kor+eng+mat+sci)/4}")
#
# score = list(map(int, input("성적 입력 : ").split())) # map -> 입력을 받아서 맞게 저장 / list -> list의 형식으로 저장
# print(f"총점 : {sum(score)}")
# print(f"평균 : {sum(score)/len(score)}") # len -> list의 length 구하는 것
#
# 24시간제로 시간을 : 기준으로 입력 받아서 시, 분, 초로 찍는데 12시간제로 변환

hour, min, sec = map(int, input("시:분:초 :").split(":"))

if hour > 11 :
    hour -= 12 # hour = hour -12
    print(f"오후{hour} 시 {min} 분 {sec} 초")
else :
    print(f"오전 {hour} 시 {min} 분 {sec} 초")


# " " 타입으로 입력한 값을 기본적으로 문자 데이터형이다.
# 바로 수로 나오는 타입은 정수,실수형이며 이는 문자열로 변경 가능하다