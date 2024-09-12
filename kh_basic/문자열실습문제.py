# 2개의 문자열을 포인터 변수 s와 k에, 양의 정수를 정수형 변수
# n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k 문자열 앞에 끼워 넣는 코드 작성
# 예) s : seoul
#       k : korea
#       n : 2
#       result : ulkorea

# s = input("s : ")
# k = input("k : ")
# n = int(input("n : "))
#
# l = len(s)
# print(l)
# print(type(l))
# h = s[l-n:l+1]
# print(h)
# print(type(h))
#
# result = h+k
# print(result)
# print(type(result))


s = input("s : ")
k = input("k : ")
n = int(input("n :"))
# print(s[-n:]+k)
pos = len(s) - n
print(s[pos:]+k)