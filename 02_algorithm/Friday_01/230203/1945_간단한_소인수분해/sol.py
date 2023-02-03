import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    N_dict = {'2':0, '3':0, '5':0 , '7':0, '11':0}
    while N > 2:

        if N % 2 == 0:
            N_dict['2'] += 1
            N = N // 2

        elif N % 3 == 0:
            N_dict['3'] += 1
            N = N // 3

        elif N % 5 == 0:
            N_dict['5'] += 1
            N = N // 5

        elif N % 7 == 0:
            N_dict['7'] += 1
            N = N // 7

        elif N % 11 == 0:
            N_dict['11'] += 1
            N = N // 11


    print(f'#{tc+1} {N_dict["2"]} {N_dict["3"]} {N_dict["5"]} {N_dict["7"]} {N_dict["11"]} ' )

