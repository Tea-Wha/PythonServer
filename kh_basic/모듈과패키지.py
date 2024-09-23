# 모듈 -> 파이썬에서 모듈은 파이썬 코드를 포함하는 파일 (.py)

# 패키지 -> 모듈의 집합 -> 여러 모듈을 포함하는 디렉토리

# import 모듈 이름

# import math #  math 모듈을 import
#
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))

# from math import sin, cos, tan, floor, ceil # math 모듈에서 사용할 부분만 import 하는 방식
# # from math import * (전부 가져옴)
#
# print(sin(1))
# print(cos(1))
# print(tan(1))

# import math as m # 별칭 부여 -> math -> m
# 
# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))

# sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈

# import sys
# 
# print("명령줄 인수 : ", sys.argv) # 해당 path 찍힘
# print("실행 경로 : ", sys.path[0])
# 
# import os
# 
# cwd = os.getcwd()
# print("현재 작업 디렉토리 : ", cwd)
# 
# # 디렉토리 생성 os.mkdir("testtest")
# # 디렉토리 제거 os.rmdir("testtest")
# 
# is_file = os.path.isfile("myfile.txt")
# print(is_file)
# is_file = os.path.isfile("password.txt")
# print(is_file)
# 
# is_dir = os.path.isdir("mydir")
# print(is_dir)

# 모듈 만들기
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password

if __name__ == "__main__": # 같은 지점에서 불려질 당시 다음과 같은 코드가 필요
    print(add(1,4))
    print(sub(4,2))