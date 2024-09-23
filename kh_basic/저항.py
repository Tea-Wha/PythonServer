# color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
#
# black = [0, 1]
# brown = [1, 10]
# red = [2, 100]
# orange = [3, 1000]
# yellow = [4, 10000]
# green = [5, 100000]
# blue = [6, 1000000]
# violet = [7, 10000000]
# grey = [8, 100000000]
# white = [9, 1000000000]
#
#
#
# x, y, z = list(map(str, input("저항의 색을 입력하세요 :").split()))
#
# if x == "black":
#     x = list(black)
#
# for e in color[0:11]:
#     if y == color[e]:
#         y =  list[e]
#
# print(y)
#
# print(black)
# print(black[0])
#
# print(x)
# print(x[0])

color = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
print(type(color))
f_name = color.index(input("첫 번째 저항 입력 : "))
s_name = color.index(input("두 번째 저항 입력 : "))
t_name = color.index(input("세 번째 저항 입력 : "))
print(int(str(f_name)+str(s_name))*(10**t_name))
print(int(f_name)*(10**(t_name+1))+int(s_name)*(10**(t_name)))


