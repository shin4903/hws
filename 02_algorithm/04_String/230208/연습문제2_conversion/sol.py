import sys
sys.stdin = open('input.txt')

def itoa(integer):

    if integer < 0 :
        negative_num = []
        integer = abs(integer)
        negative_num.append(chr(45))
        negative_num.append(chr(integer+48))
        negative = ''
        for i in negative_num:
            negative += i
        return negative, type(negative)


    int_list = []
    while integer != 0:
        int_list.append(integer % 10)
        integer = integer // 10
    int_list.reverse()

    int2_list = []
    for i in int_list:
        int2_list.append(chr(i+48))

    integer_num = ''
    for i in int2_list:
        integer_num += i

    return integer_num, type(integer_num)

T = 6
for tc in range(T):
    integer = int(input())
    print(*itoa(integer))
