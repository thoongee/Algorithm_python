### 개념

- **큰 문제**를 **작은 부분 문제로 분할**하고, 각각의 작은 **부분 문제를 해결하여 전체 문제의 해답**을 구하는 알고리즘
- 문제의 크기가 커서 직접적인 해결이 어려운 경우 유용
- 분할된 문제의 개수가 지수적으로 증가하거나 분할된 문제들이 크기가 일정하지 않은 경우 → 분할 정복 말고, 다른 접근방식을 고려해야 함

### 예시

정렬 알고리즘인 병합 정렬(Merge Sort)과 퀵 정렬(Quick Sort)

### 동작 방식

1. 문제를 작은 부분 문제들로 분할한다.
2. 분할된 부분 문제들을 각각 재귀적으로 해결한다.
3. 부분 문제들의 해답을 결합하여 전체 문제의 해답을 얻는다.

### 시간 복잡도

- 대부분의 경우, 분할 정복 알고리즘은 재귀적인 방법으로 문제를 해결하므로, **재귀 호출의 깊이**에 따라 시간 복잡도가 결정된다.
- **분할된 문제의 개수가 N**이라면, **시간 복잡도는 O(N*logN)**

### 구현

1. **병합정렬 (merge sort)**

<p align="center"><img src="https://github.com/thoongee/algorithm-python/assets/94193480/21ef0cb7-8c1c-455d-ac9f-cd4e4c848e2f" width="40%">

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left) # 재귀 사용!
    right_sorted = merge_sort(right)
    
    # Combine
    return merge(left_sorted, right_sorted)
    
    
def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    return result
```

- 알고리즘 설계
    1. 분할: 입력 리스트를 반으로 나눕니다.
    2. 정복: 각각의 부분 리스트를 재귀적으로 병합 정렬합니다.
    3. 결합: 정렬된 부분 리스트를 합쳐 전체 리스트를 정렬합니다.
    - merge_sort 함수 :
        - 입력 리스트를 반으로 나누고 재귀적으로 호출하여 각각을 정렬
        - 마지막으로 merge 함수를 사용하여 두 정렬된 리스트를 합병하여 전체 리스트를 정렬
    - merge 함수 :
        - 두 개의 정렬된 리스트를 인수로 받아, 두 리스트를 비교하여 작은 순서대로 result 리스트에 삽입하고, 남은 요소를 추가하여 반환
1. **quick sort**

<p align="center"><img src="https://github.com/thoongee/algorithm-python/assets/94193480/99619236-29b4-434c-a03e-29f4f2294b20" width="70%">

<p align="center"><img src="https://github.com/thoongee/algorithm-python/assets/94193480/f88df678-5953-4bd9-a81c-16b0bb170312" width="30%">

- 특징 :
    - 정렬을 위해 별도의 저장 공간을 필요로 하지 않아 메모리 사용량이 적다
    - **최악의 경우(이미 정렬된 리스트, 피벗이 가장 작거나 큰 수 등)**에는 분할이 제대로 이루어지지 않아 시간 복잡도가 **O(n^2)**에 근접

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Conquer
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    
    # Combine
    return left_sorted + [pivot] + right_sorted
```

- 알고리즘 설계
    1. 기준점(**pivot**) 선택: 리스트에서 하나의 원소를 기준점으로 선택한다.
    2. 분할: 기준점을 기준으로 리스트를 두 개로 분할한다. 분할된 두 개의 리스트는 각각 기준점보다 작은 값과 큰 값으로 이루어져 있다.
    3. 정복: 각각의 부분 리스트를 재귀적으로 퀵 정렬한다.
    4. 결합: 정렬된 부분 리스트를 합쳐 전체 리스트를 정렬한다.
