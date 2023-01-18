### 세로로 출력하기
number = int(input())
for num in range(1,number+1):
    print(num)

### 가로로 출력하기
for num in range(1,number+1):
    print(num,end=' ')

###  거꾸로 세로로 출력하기
for num in range(number,0,-1):
    print(num)

### 거꾸로 가로로 출력하기
for num in range(number,-1,-1):
    print(num,end=' ')

### N줄 덧셈
result = 0
for num in range(1,number+1):
    result += num
print(result)

### 삼각형 출력하기
number = int(input())
for num in range(1,number+1):
    print((number-num)*' ',num*'*')

number = int(input())
for star in range(1,number+1):
    for space in range(number-star-1, -1, -1):
        print(' ',end='')
    print(star*'*')

### extra 문제
arr = [[i for i in range(4)] for j in range(4)]

for i in range(number):
    for j in range(number):
        print(arr[i][j])

numbers = [
85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
numbers.sort()
print(numbers[len(numbers)//2])