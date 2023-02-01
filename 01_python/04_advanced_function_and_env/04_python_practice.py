# 1. 간단한 N의 약수
N = int(input())
N_list = []
for i in range(1,N+1):
    if N % i == 0:
        N_list.append(i)
print(N_list)

# 2. List의 합 구하기
def list_sum(num):
    result = 0
    for i in num:
        result += i
    return result
print(list_sum([1,2,3,4,5]))

# 3. Dictionary로 이루어진 List의 합 구하기
def dict_list_sum(x):
    ages = 0
    for i in range(len(x)):
        ages += x[i]['age']
    return ages
age_list = [{'name' : 'kim', 'age' : 12}, {'name' : 'Lee', 'age' : 4}] 
print(dict_list_sum(age_list))

# 4. 2차원 List의 전체 합 구하기
def all_list_sum(x):
    result = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            result += x[i][j]
    return result

all_list = [[1], [2,3], [4,5,6], [7,8,9,10]]
print(all_list_sum(all_list))

# 5. 숫자의 의미
def get_secret_word(x):
    word = ' '
    for i in range(len(x)):
        word += chr(x[i])
    return word
get_word = [83, 115, 65, 102, 89]
print(get_secret_word(get_word))

# 6. 내 이름은 몇 일까?
def get_secret_number(x):
    number = 0
    for i in x:
        number += ord(i)
    return number
get_number = 'happy'
print(get_secret_number(get_number))

# 7. 강한 이름
def get_strong_word(x,y):
    if get_secret_number(x) > get_secret_number(y):
        return x
    else:
        return y
print(get_strong_word('delilah','dixon'))


