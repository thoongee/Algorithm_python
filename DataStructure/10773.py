import sys
input = sys.stdin.readline

money=[]
K = int(input())

for _ in range(K):
    num = int(input())
    if num==0:
        del money[len(money)-1]
    else:
        money.append(num)

total =0
for i in range(len(money)):
    total += money[i]

print(total)
