# 상근이 알람 : 45분 일찍 알람을 울리도록 하는 문제
# 입력 : 정수 H (시간)
# 입력 : 정수 M (분)
# 불필요한 0 사용 X/ 하루의 시작은 0:0/ 끝은 23:59

# 입력은 h,m ":" 기준으로 입력
# 시간을 분으로 환산 하기
# 분으로 환산한 시간이 45보다 작으면  시간 별도 계산 해야 함
# 계산된 시간에서 45분 빼줌

# H, M = map(int, input("일어날 시:분 입력 : ").split(":"))
#
# if 0<=H<24 and 0<=M<60:
#     if M < 45:
#         W_M = 60 - (45-M)
#         if H < 1:
#             W_H = 23
#         else:
#             W_H = H-1
#     elif 45<=M<60:
#         W_M = M-45
#         W_H = H
#     print(f"알람 예정 시간은 {W_H}시 {W_M}분 입니다.")
# else: print("시간이 잘못 입력 되었습니다.")

h,m = map(int, input("시간 입력 : ").split(":"))
calc_min = h * 60 + m
if calc_min < 45:
    calc_min = 24*60 + m
calc_min -= 45
print(f"{calc_min//60}:{calc_min%60}")
