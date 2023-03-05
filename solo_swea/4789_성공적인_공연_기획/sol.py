import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    num = list(map(int,input()))
    count = 0
    result = 0
    for i in range(len(num)):
        if num[i] != 0:
            if count < i:
                result += i - count
                count += i -count
        count += num[i]

    print(f'#{tc}',result)