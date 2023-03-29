import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    # 분할 정복
    if len(arr) <= 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left, right = [], []

        for i in range(1,len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])
        return [*quick_sort(left), pivot, *quick_sort(right)]


T = int(input())

for tc in range(1,T+1):
    num = list(map(int,input().split()))
    print(quick_sort(num))