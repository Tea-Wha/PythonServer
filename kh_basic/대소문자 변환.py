# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
# for 문을 사용
# islower() : 소문자이면 True, 아니면 False 반환

# s  = input("입력 : ")
#
# i=""
# for n in s:
#     if n.islower() == 1:
#         i += n.upper()
#     else:
#         i += n.lower()
# print(i)

# s  = input("입력 : ")
#
# i=""
# if s.islower() == 1:
#         i += s.upper()
# elif s.islower() == 0:
#         i += s.lower()
# print(i)


# input을 입력받는 것도 하나씩 순차적으로 들어가도 되는 것이라고 봐야되는가?
# 이는 s가 순차적으로 들어가는 동시에 n이라는 변수를 잡고 동시에 같이 스캔한다는 의미?

# rst = ""
# for e in input("입력 : "):
#     if e.islower():
#         rst += e.upper()
#     else:
#         rst += e.lower()
#
# print(rst)

s = input("입력 : ")
i = s.swapcase()
print(i)
