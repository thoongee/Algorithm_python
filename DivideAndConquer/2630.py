import sys
input = sys.stdin.read

def count_papers(x, y, size):
    if size == 1:
        if grid[x][y] == 0:
            counts[0] += 1
        else:
            counts[1] += 1
        return
    
    first_color = grid[x][y]
    same_color = True
    for i in range(x, x + size):
        if not same_color:
            break
        for j in range(y, y + size):
            if grid[i][j] != first_color:
                same_color = False
                break
    
    if same_color:
        if first_color == 0:
            counts[0] += 1
        else:
            counts[1] += 1
    else:
        half_size = size // 2
        count_papers(x, y, half_size)
        count_papers(x, y + half_size, half_size)
        count_papers(x + half_size, y, half_size)
        count_papers(x + half_size, y + half_size, half_size)

# 입력 처리
data = sys.stdin.read().strip().split()
N = int(data[0])
grid = []
index = 1
for i in range(N):
    row = list(map(int, data[index:index+N]))
    grid.append(row)
    index += N

# 하얀색(0)과 파란색(1) 색종이의 개수를 저장할 리스트
counts = [0, 0]

# 전체 종이에 대해 함수 호출
count_papers(0, 0, N)

# 결과 출력
print(counts[0])
print(counts[1])