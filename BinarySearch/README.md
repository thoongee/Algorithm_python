<aside>
💡 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘

</aside>

## 순차 탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드를 이용할 때도 내부에서는 순차 탐색이 수행된다
- 시간 복잡도 : O(N)

## 이진 탐색

### 개념

- 찾으려는 데이터와 중간점에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
- 시간 복잡도 : **O(logN)**
    - 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어듦

### **조건**

- 배열 내부의 데이터가 **정렬**되어 있어야만 쓸 수 있음

### 구현

- 시작 점, 끝 점, 중간 점 지정
- 중간 점에 위치한 데이터가 찾으려는 데이터보다 작을 경우, 시작 점을 중간 점 바로 다음 위치로 변경
- 중간 점에 위치한 데이터가 찾으려는 데이터보다 클 경우, 끝 점을 중간 점 바로 이전 위치로 변경
- 중간 점에 위치한 데이터가 찾으려는 데이터와 동일할 경우, 탐색 종료
1. 재귀 이용

```python
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2 # 중간지점

    if array[mid] == target: # 중간 점에 위치한 데이터가 찾으려는 데이터와 동일할 경우, 탐색 종료
        return mid
    
    elif array[mid] > target: # 중간 점에 위치한 데이터가 찾으려는 데이터보다 클 경우, 끝 점을 중간 점 바로 이전 위치로 변경
        return binary_search(array,target,start,mid-1)
    else: # 중간 점에 위치한 데이터가 찾으려는 데이터보다 작을 경우, 시작 점을 중간 점 바로 다음 위치로 변경
        return binary_search(array,target,mid+1,end)

n = 10 # n : 원소 개수
target = 7 # target : 찾고자 하는 값
array = [1,3,5,7,9,11,13,15,17,19] # array : 전체 원소

result = binary_search(array,target,0,n-1)
if result:
    print(result+1) # 찾고자 하는 값이 몇번째에 존재하는지 출력
else:
    print('원소가 존재하지 않습니다')
```

1. 반복문 이용

```python
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = 10 # n : 원소 개수
target = 7 # target : 찾고자 하는 값
array = [1,3,5,7,9,11,13,15,17,19] # array : 전체 원소

result = binary_search(array,target,0,n-1)
if result:
    print(result+1) # 찾고자 하는 값이 몇번째에 존재하는지 출력
else:
    print('원소가 존재하지 않습니다')
```

### 팁

- 이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 코드를 외우는 것이 좋음
- 어려운 문제에서는 이진 탐색 + 다른 알고리즘 (ex.그리디) 조합으로 나오는 경우가 많음
- 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제에 접근하는 것이 좋음

## 이진 탐색 트리

- 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조

### 조건

- 부모 노드보다 왼쪽 자식 노드가 작다. 부모 노드보다 오른쪽 자식 노드가 크다. (**왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**)

### 알고리즘

1. 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문
    - 루트 노드보다 찾고자 하는 값이 크다면 오른쪽 자식 노드로 이동
    - 루트 노드보다 찾고자 하는 값이 작다면 왼쪽 자식 노드로 이동
2. 자식 노드가 없을때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것
