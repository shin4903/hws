import sys
sys.stdin = open('input.txt')

for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    for i in range(100):
        sum_value = 0
        for j in range(100):
            sum_value += arr[i][j]
            result.append(sum_value)

    sum_value_2 = 0
    for i in range(100):
        sum_value_2 += arr[i][i]
        result.append(sum_value_2)

    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(100):
        sum_value = 0
        for j in range(100):
            sum_value += arr[i][j]
            result.append(sum_value)

    sum_value_2 = 0
    for i in range(100):
        sum_value_2 += arr[i][i]
        result.append(sum_value_2)

    max_value = result[0]
    for i in range(1,len(result)):
        if max_value < result[i]:
            max_value = result[i]

    print(f'#{tc}',max_value)