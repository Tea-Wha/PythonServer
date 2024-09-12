# 각 사이트 비밀번호 만들기
# 규칙1 : http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 + 글자에 포함된 'k' 갯수 + '!' +
# 자신의 이니셜

# url = input("사이트 : ")
#
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) +str(my_str.count("o"))+str(my_str.count("k"))+"i"+"htw"
# # str이 붙는 이유는 -> my_str[:3]이 문자열이기도 하고, 비밀번호는 문자열로 구성되어야 하기 때문에?
# print("비밀번호 : " + password)

file_name = "password.txt"
f = open(file_name, "wt")
while True:
    url = input("사이트 : ")
    if url == "exit": break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o"))\
               + str(my_str.count("k")) + "i" + "htw"
    print("비밀번호 : " + password)
    f.write(password + "\n")
f.close()