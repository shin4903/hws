import sys
sys.stdin = open('input.txt')

def backtracking(i, n, tmp):
    global cnt
    if i == n:
        cnt = min(cnt,tmp)
        return
    if tmp >= cnt:
        return
    elif i < n:
        for _ in range(m[i]): # 2 1 3 3
            i += 1
            tmp += 1
            backtracking(i, n, tmp)
            tmp -= 1



T = int(input())

for tc in range(1,T+1):
    n, *m = list(map(int,input().split()))
    n = n - 1
    cnt = 10000
    backtracking(0,n,0)
    print(f'#{tc}',cnt-1)
