import sys
sys.stdin = open('input.text')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    num_list = [0]*100

    for i in num:
        num_list[i] += 1

    max_value = num_list[0]
    for i in num_list:
        if max_value < i:
            max_value = i
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i] == max_value:
            print(i,max_value)
            break