# 날짜와 시간 관련 함수
from datetime import datetime  # datetime 모듈에서 datetime 함수를 가져옴
# import datetime # 내부 메서드로 .datetime 추가해야함

print(datetime.today())
print(datetime.today().month)
print(datetime.today().date())
print(datetime.today().time())
print(datetime.today().hour)
print(datetime.today().day)

# import calendar
# print(calendar.calendar(2024))

# math 모듈 : 수학과 관련 기능을 처리 할 때 사용
import math

print(math.sin(1/2))
print(math.tan(1))
print(math.ceil(1.000000001)) # 무조건 올림
print(math.floor(1.999299999)) # 무조건 내림
print(math.log(100,10))

#