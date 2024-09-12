# 자연수 A, B, C
#  모두 곱했을 때 등장하는 숫자의 개수를 세는 문제 :

# A,B,C = map(int, input("세 자연수 입력 : ").split(":"))
#
# Mul = A*B*C
# Mul = str(Mul)
# print(Mul)
#
# print(Mul.count("0"))
# print(Mul.count("1"))
# print(Mul.count("2"))
# print(Mul.count("3"))
# print(Mul.count("4"))
# print(Mul.count("5"))
# print(Mul.count("6"))
# print(Mul.count("7"))
# print(Mul.count("8"))
# print(Mul.count("9"))

# A,B,C = map(int, input("세 자연수 입력 : ").split(":"))
#
# Mul = A*B*C
# Mul = str(Mul)
# print(Mul)
#
# for e in range(0,10): # range(10) ->  0~9까지 범위
#     print(Mul.count(str(e)))


# 실습 2번 : 문자열 반전, 문자열을  입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA

# Input = input("문자열 입력 : ")
# print(Input)
# print(Input[0])
# for e in range(len(Input)-1, -1,-1):
#     print(Input[e])

#in_str = input("문자열 입력 : ")
# for i in range(len(in_str)-1,-1,-1):
#     print(in_str[i], end="")


#reverse_str = in_str[::-1] # 파이썬만 가능
#print(reverse_str)
