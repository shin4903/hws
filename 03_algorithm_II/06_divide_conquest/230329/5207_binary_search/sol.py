import sys
sys.stdin = open('input.txt')

def bsearch(n, arr, key):
    global cnt, stack
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            cnt += 1
            return
        elif arr[mid] > key:
            high = mid - 1
            stack.append(1)
        else:
            low = mid + 1
            stack.append(2)
    return


T = int(input())

for tc in range(1, T+1):



    N, M = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt = 0
    for i in B:
        if i in A:
            stack = []
            bsearch(N, A, i)
            print(stack)
            if len(stack) <= 1:
                cnt += 1
            elif len(stack) >= 2:
                if 1 in stack and 2 in stack:
                    cnt += 1

    print(f'#{tc}', cnt)
