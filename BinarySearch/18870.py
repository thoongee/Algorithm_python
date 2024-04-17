import sys
input=sys.stdin.readline

n = int(input().strip())
coords = list(map(int, input().split()))

unique_sorted_coords = sorted(set(coords)) # [-10, -9, 2, 4]
    
# coord : unique한 coord 값, idx : 각 좌표가 몇 번째로 작은지
coord_index_map = {coord: idx for idx, coord in enumerate(unique_sorted_coords)} # {-10: 0, -9: 1, 2: 2, 4: 3}

# 원본 좌표 리스트에서 각 좌표에 대응하는 압축된 값(인덱스)을 추출하여 새 리스트 생성
compressed_coords = [coord_index_map[coord] for coord in coords]
print(' '.join(map(str,compressed_coords)))