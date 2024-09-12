# 회원 가입을 위한 아이디 패스워드 입력 받기
# 정규식?

id = input("아이디 입력 : ")

if len(id) >= 8:
    pw = input("비밀번호 입력 : ")
    if len(pw) < 8 or len(pw) > 16:   # if pw.__len__()
        print("비밀번호는 8 자리 16 자리 사이어야 합니다.")
    elif pw.find(id) >= 0: # 비밀번호 만들 때 ide의 문자열을 포함한 경우
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print("아이디 : {}".format(id))
        print("비밀번호 : {}".format(pw))
else:
    print("아이디는 반드시 8자리 이상이어야 합니다.")