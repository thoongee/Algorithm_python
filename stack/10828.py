import sys
input = sys.stdin.readline

N = int(input())
dat = []
pos = 0
for _ in range(N):
    # push number
    #여전히 띄어쓰기 구분해서 입력받는게 바로 떠오르지 않는다.
    #https://hkim-data.tistory.com/32#:~:text=split%20%ED%99%9C%EC%9A%A9%20%EC%AA%BC%EA%B0%9C%EC%84%9C%20%EC%9E%85%EB%A0%A5%EB%B0%9B%EA%B8%B0&text=split%EC%9D%98%20%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0%EB%A5%BC%20%EA%B8%B0%EB%B3%B8,%EB%B3%B4%EB%A9%B4%20%EC%9D%B4%ED%95%B4%EA%B0%80%20%EC%9E%98%20%EB%90%9C%EB%8B%A4.&text=%EC%9D%B4%20split%20%ED%95%A8%EC%88%98%EB%A5%BC%20%EC%9D%B4%EC%9A%A9,%ED%95%98%EC%97%AC%20%EC%9E%85%EB%A0%A5%20%EB%B0%9B%EC%9D%84%20%EC%88%98%20%EC%9E%88%EB%8B%A4.
    command = list(input().split())

    if command[0]== 'push':
        dat.append(int(command[1]))
        pos += 1
        # print('dat',dat)
        # print('pos',pos)

    if command[0]=='pop':
        if pos == 0:
            print(-1)
        else:
            pos -= 1
            print(dat[pos])
            del dat[pos] # pos만 옮겨주면 되는줄

    if command[0]=='size':
        print(pos)

    if command[0]=='empty':
        if pos == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'top':
        if pos== 0:
            print(-1)
        else:
            print(dat[pos-1]) #IndexError


