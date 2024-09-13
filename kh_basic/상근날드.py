# 세트메뉴 구성시 -> 50원 뺌 
# 상덕, 중덕, 하덕 버거
# 콜라, 사이다
# 입력 다섯줄
# 첫째 줄 : 상덕 / 둘째 줄 : 중덕 / 셋째 줄 : 하덕

money = list(map(int, input("상덕, 중덕, 하덕, 콜라, 사이다 가격 입력 :").split()))

# ls = list(map(int, input("입력 : ").split()))
# min_berger = min(ls[3])
# min_drink = min(ls[3:5])
#print(f"세트 가격 : {min_berger+min_drink-50} 원 입니다.")

#min_berger = ls[0] # 기준값 정하기 -> 기준값을 정해야 되는 언어도 있다는 것을 인지해야함
#min_drink = ls[3]
# for i in range(len(ls)):
#   if i <3 and min_berger > ls[i]:
#       min_berger = ls[i]
#   if i >2 and min_drink > ls[i]:
#       min_drink = ls[i]
# print(f"세트 가격 : {min_berger + min_drink - 50}")

a = min(money[0:3])
b = min(money[3:5])

c = max(money[0:3])
d = max(money[3:5])

c_set = a+b-50
e_set = c+d-50

print("가장 싼 세트 메뉴는 ", str(c_set), " 원 입니다.")
print("가장 비싼 세트 메뉴는", str(e_set), " 원 입니다.")