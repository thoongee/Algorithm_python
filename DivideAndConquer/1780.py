import sys
input = sys.stdin.read

def count_paper(x, y, n):
    if n == 1:
        counts[grid[x][y]] += 1
        return

    # 현재 종이가 모두 같은 수로 이루어져 있는지 확인
    init_val = grid[x][y]
    all_same = True
    for i in range(x, x + n):
        if not all_same:
            break
        for j in range(y, y + n):
            if grid[i][j] != init_val:
                all_same = False
                break

    # 모두 같은 수로 이루어져 있다면 해당 숫자의 카운트를 증가
    if all_same:
        counts[init_val] += 1
    else:
        # 같은 수로만 이루어져 있지 않다면 9개로 분할하여 각각 재귀적으로 처리
        new_size = n // 3
        for i in range(3):
            for j in range(3):
                count_paper(x + i * new_size, y + j * new_size, new_size)

# 입력 받기
data = sys.stdin.read().split()
N = int(data[0])
grid = [list(map(int, data[i * N + 1: (i + 1) * N + 1])) for i in range(N)]

# 각 숫자 카운트를 저장할 딕셔너리
counts = {-1: 0, 0: 0, 1: 0}

# 전체 종이에 대해 함수 호출
count_paper(0, 0, N)

# 결과 출력
print(counts[-1])
print(counts[0])
print(counts[1])