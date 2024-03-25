import sys
input = sys.stdin.readline

n = input().strip()
nums = [int(x) for x in n]


if len(n)%2==1:
    print('READY')
else:
    half = int(len(n)//2)
    left = nums[:half]
    right = nums[half:]
    left_sum = sum(left)
    right_sum = sum(right)
    if left_sum == right_sum:
        print('LUCKY')
    else:
        print('READY')

