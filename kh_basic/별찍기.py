
Input = input("몇 줄을 만드실 겁니까? : ")

for i in range(int(Input)):
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(int(Input),-1,-1):
    for j in range(0,i):
        print("*", end="")
    print()



n = int(input("정수를 입력 하세요 : "))
for i in range(0,n):
    for j in range(0,n):
        if j%2 == 0: print("@", end=" ")
        else: print("*", end=" ")
    print()
