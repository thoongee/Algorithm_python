import sys
input = sys.stdin.read

def compress(x, y, n):
    if n == 1:
        return str(grid[x][y])

    # 첫 번째 원소를 기준으로 모든 원소가 같은지 확인
    initial = grid[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != initial:
                # 사분면으로 나누기
                next_n = n // 2
                top_left = compress(x, y, next_n)
                top_right = compress(x, y + next_n, next_n)
                bottom_left = compress(x + next_n, y, next_n)
                bottom_right = compress(x + next_n, y + next_n, next_n)
                return f"({top_left}{top_right}{bottom_left}{bottom_right})"
    
    # 모든 원소가 같은 경우
    return str(initial)

# 입력 처리
data = input().strip().split()
N = int(data[0])
grid = [list(map(int, list(data[i + 1]))) for i in range(N)]

# 압축 결과 출력
result = compress(0, 0, N)
print(result)
