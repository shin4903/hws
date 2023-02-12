import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    A, B = map(str, input().split())
    arr = list(map(str, input().split()))
    # num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    arr.sort(key = lambda x : num_dict[x])
    print(f'#{tc}')
    print(' '.join(arr))

