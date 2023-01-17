
# # [입력]
# # 숫자를 2번 입력받는다.
# # [출력]
# # 입력 숫자를 계산하여 값을 출력한다.
# # [입력 예시]
# # 6374
# # 8729
# # [출력 예시]
# # 15103


num = int(input())
num2 = int(input())

print(num + num2)

# # 좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
# # 점심메뉴의 평균 값을 출력하시오.


dict = {'차돌김치찌개':7000, '카레면':3500, '버터바지락찜파스타':12000, '잡채밥':6500}
price = 0
count = 0

for key in dict:
    price += dict[key]
    count += 1

print(price/count)

########## practice2 항구의 배 표시하기

true_port = [4,8,9,15]
ports=[]
for ship in range(1,16):
    if ship in true_port:
        ports.append(1)
    else:
        ports.append(0)
# ports = [0,0,0,1,0,0,0,1,1,0,0,0,0,0,1]
odd_ports = []
count = 0
for ship in ports:
    count += 1
    if ship == True:
        odd_ports.append(count)
print(odd_ports)


######## practice3 로또 당첨 여부 확인하기

ssafy_choice = [1, 12, 27, 33, 38, 42]
lucky_numbers = [7, 15, 27, 33, 37, 42]

for l_n in lucky_numbers:
    ssafy_choice.append(l_n)

number = len(ssafy_choice)
ssafy_lucky = len(set(ssafy_choice))
count = number-ssafy_lucky
print(count)

######## practice4 도시 정보 구조화하기

air_info = [{'name': 'A', 'capital': 'capital', 'o2':3, 'Co2':2},{'name': 'B', 'capital': 'noncapital', 'o2':5, 'Co2':3}]

O2_info = []
for i in range(len(air_info)):
    O2_info.append(air_info[i]['o2'])

print(O2_info)