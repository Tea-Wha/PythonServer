# 예외 처리 -> 오류 1. 문법 오류 2. 예외 상황
# 기본 예외 처리 -> 1. 조건문을 사용하는 방법 2. try 구문을 사용하는 방법

# exception (예외 상황) : 프로그램 작성 후 실행 도중에 발생하는 여러가지 상황에 대한 것 (죽거나, 상이한 결과 등)
# 예외 처리란? 예외 상황이 발생할 가능성이 높은 코드에서 try ~ exception을 통해 흐름을 변경 하는 것

# while True:
#     try:
#         file_name = input("파일 이름 입력 : ")
#         score_file = open(file_name,"r",encoding="utf-8")
#         print(score_file.read())
#         score_file.close()
#         break
#     except FileNotFoundError:
#         print("파일이 없습니다. 파일 확인 후 다시 진행 하세요.")

# 예외상황이 발생할 때 이 부분은 잡기 쉽게 바꿔야 한다

# try:
#     print("나눗셈 계산기")
#     num1 = int(input("첫 번째 숫자 입력 : "))
#     num2 = int(input("두 번째 숫자 입력 : "))
#     print(f"{num1} / {num2} = {(num1/num2):.2f}")
# except ValueError:
#     print("숫자만 입력 하세요.")
# except ZeroDivisionError:
#     print("나눗셈은 0으로 할 수 없습니다.")
# else: # 예외가 발생하지 않았을 때 불려짐
#     print("정상 처리 되었습니다.")
# finally: # 예외 여부에 상관없이 호출
#     print("프로그램 종료.")

while True:
    try:
        print("나눗셈 계산기")
        num1 = int(input("첫 번째 숫자 입력 : "))
        num2 = int(input("두 번째 숫자 입력 : "))
        print(f"{num1} / {num2} = {(num1/num2):.2f}")
        break
    except ValueError:
        print("숫자만 입력 하세요.")
    except ZeroDivisionError:
        print("나눗셈은 0으로 할 수 없습니다.")

    print("프로그램 종료.")
