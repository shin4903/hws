import sys
sys.stdin = open('input.txt')

def backtracking(i, n, s, c):
    global result, tmp
    if i == n and c <= cal:
        if tmp > c:
            result = max(result,s)
        return
    elif c > cal:
        return
    else:
        backtracking(i + 1, n, s, c)
        backtracking(i + 1, n, s+Ti[i], c+Ki[i])

T = int(input())

for tc in range(1,T+1):
    Ti = []
    Ki = []

    N, cal = map(int,input().split())
    for _ in range(N):
        t, k = map(int,input().split())
        Ti.append(t)
        Ki.append(k)
    result = 0
    tmp = cal
    backtracking(0,N,0,0)
    print(result)