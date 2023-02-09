import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    target, pattern = map(str, input().split())
    count = target.count(pattern) # target안의 pattern의 수 카운팅
    typing = len(target) - len(pattern) * count + count # 타이핑 횟수 계산
    print(f'#{tc}', typing)