import sys
input = sys.stdin.readline

n = int(input().strip())
levels = list(map(int,input().strip().split()))
levels.sort(reverse=True)
 
gold = 0
for i in range(len(levels)-1):
    i = 0
    gold += levels[i] + levels[i+1]
    del levels[i+1]
 
print(gold)
