# 영식(Y) 요금제 : 30초마다 10원 (over 되자마자 10 원 추가)
# 민식(M) 요금제 : 60초마다 15원
# 입력 : 3 (통화 횟수)
# 40 40 40  <= 각 통화당 통화 시간
#  M 45 -> 더 싼 요금제와 통화 요금
#  Y M 50 -> 두개의 통화 총 금액이 같은 경우
# N < 20
# T <10000

# C =int(input("통화 횟수 입력 : "))
#
# Y = 10 # 30초
# M = 15 # 60초
#
# for T in range(10001):
#     Y_T = (T//30)+1
#     M_T = (T//60)+1
#     Y_M = 10 * Y_T*C
#     M_M = 15*M_T*C
#     if Y_M > M_M:
#         print(f"M {T} {M_M}")
#     elif Y_M<M_M:
#         print(f"Y {T} {Y_M}")
#     else:
#         print(f"M Y {T} {M_M}")

# 문제를 잘못 이해함
# 통화 횟수 입력
cnt = int(input("통화 횟수 : "))
# 각 통화에 대한 통화 시간 입력
call_time = list(map(int, input("각 통화 시간 : ").split()))
y_pay = m_pay = 0
for i in range(cnt):
    y_pay += (call_time[i]//30)*10+10
    m_pay += (call_time[i]//60)*15+15
if y_pay>m_pay:
    print(f"M {m_pay}")
elif y_pay<m_pay:
    print(f"Y {y_pay}")
else:
    print(f"M Y {m_pay}")

