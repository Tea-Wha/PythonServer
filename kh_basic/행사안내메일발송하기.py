# 한파의 연속인 1월 입니다.
# 봄을 기다리는 2월 입니다.
# 봄의 기운이 느껴지는 3월 입니다.
# 새싹이 피어나는 4월 입니다.
# 계절의 여왕 5월 입니다.
# 활동하기 좋은 6월 입니다.
# 휴가가 기다려지는 7월 입니다.
# 무더운 8월 입니다.
# 선선한 9월 입니다.
# 천고마비의 계절 10월 입니다.
# 쓸쓸한 늦가을 11월 입니다.
# 올 한해의 마무리 12월 입니다.

name = input("이름 : ")
event = input("제목 : ")
date = input("날짜 : ")  # 20220301
time = input("시간 : ") # 24시간제 입력

# 입력 받은 date에서 월 정보 추출
month = date[4:6]
month = int(month)
greeting = ""
if month == 1:
    greeting = "한파의 연속인 1월 입니다."
elif month == 2:
    greeting = "봄을 기다리는 2월 입니다."
elif month == 3:
    greeting = "봄의 기운이 느껴지는 3월 입니다."
elif month == 4:
    greeting = "새싹이 피어나는 4월 입니다."
elif month == 5:
    greeting = "계절의 여왕 5월 입니다."
elif month == 6:
    greeting = "활동하기 좋은 6월 입니다."
elif month == 7:
    greeting = "휴가가 기다려지는 7월 입니다."
elif month == 8:
    greeting = "무더운 8월 입니다."
elif month == 9:
    greeting = "선선한 9월 입니다."
elif month == 10:
    greeting = "천고마비의 계절 10월 입니다."
elif month == 11:
    greeting = "쓸쓸한 늦가을 11월 입니다."
elif month == 12:
    greeting = "올 한해의 마무리 12월 입니다."
else:
    print("월 정보가 잘못 입력 되었습니다.")

print(f"{name}님.")
print(greeting)
print(f"""아래의 일정으로 {event}를 진행하고자 하오니
자리를 빛내 주시기 바랍니다.
""")
print(f"="*7, "행사 안내", "="*7)
print("내용 : " + event)
print(f"날짜 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
time = int(time)
if time > 11:
    time-= 12
    print(f"시간 : 오후 {time}시")
else:
    print(f"시간 : 오전 {time}시")

