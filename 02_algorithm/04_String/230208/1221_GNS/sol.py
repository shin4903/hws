import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    S, N = map(str,input().split())
    arr = list(map(str, input().split()))
    N = int(N)
    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if num_dict[arr[j]] > num_dict[arr[j+1]]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}')
    print(' '.join(arr))

# T = int(input())
#
# numbers = ['ZRO' , 'ONE', 'TWO','THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#
#
# for tc in range(1, T+1):
#     arr = input().split()
#     a = arr[0]
#     b = int(arr[1])
#     num = list(input().split())
#     result = []
#     for i in range(len(numbers)):
#         for j in num:
#             if j == numbers[i]:
#                 result.append(j)
#
#     print(f'{a}')
#     print(*result)