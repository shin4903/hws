import sys
sys.stdin = open('input.text')

tc = int(input()) # 테스트 케이스의 개수
for i in range(tc): # 테스트 케이스의 수 만큼 반복
    N = int(input()) # 주어지는 카드의 장수
    a = input() # for문을 순환하기 쉽게 문자열로 숫자를 받음 # 49679
    C = [0] * 10 # 입력가능한 숫자는 0~9 까지이므로 10개의 요소를 가진 리스트 생성
    cnt = 0 # 최대 장수와 비교하기 위해 생성한 cnt
    for j in a: # 입력받은 문자열을 순환
        C[int(j)] += 1 # 입력받은 문자를 숫자로 형변환하여 그 숫자에 해당하는 인덱스를 이용해 C 리스트에 +1
    # print(C) # >>> [0, 0, 0, 0, 1, 0, 1, 1, 0, 2] (각 인덱스에 해당하는 숫자가 가지고 있는 카드의 수) # 49679
    for k in range(len(C)): # 리스트의 인덱스 수 만큼 순환하며
        if C[k] >= cnt: # cnt 보다 큰 C[k]가 있으면
            cnt = C[k] # 그 값을 cnt로 설정
    # print(cnt) # >>> 2
    for l in range(9,-1,-1): # 카드의 수가 가장 많고 '가장 큰 숫자'를 찾으면 되므로 뒤쪽 인덱스부터 순환
        if C[l] == cnt: # cnt와 값이 같은 요소가 있다면
            # print(l) # >>> 9
            print(f'#{i+1} {l} {cnt}') # 그 인덱스에 해당하는 숫자를 print
            break


