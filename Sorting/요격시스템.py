targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
answer = 0
targets.sort(key=lambda x:x[1])
check = -1

for target in targets:
    if check <= target[0]:
        check = target[1]
        answer +=1 

print(answer)