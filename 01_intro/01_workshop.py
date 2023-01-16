# 문자열 내부에 작은 따옴표가 있어
# 큰 따옴표로 감싸 주었다.

print("it's SAFFY9")

# escape sequence를 사용하여
# 작은 따옴표로 작성하였다.
print('It\'s SSAFY9')


a = 458345 
b = 623576
print(a+b)

answer = 458345 + 623576
print(answer)

greeting = 'Hello'
month = 'July'
print(greeting, month)
print(f'{greeting} {month}')
answer = greeting + ' ' + month
print(answer)

hello = input()
hi = input()
print(hello + hi)
# '3' + '2' == '32'
# 문자열을 정수로 형변환 한 후에 계산한다.
hello = int(input())
hi = int(input())
print(hello + hi)