import sys
sys.stdin = open('input.text')

T = int(input()) # 테스트 반복 횟수를 입력받는다.
for tc in range(T): # 테스트 횟수만큼 순환
    num = int(input()) # 카드 6장의 정보를 받음
    C = [0] * 12 # 0번 인덱스와 1번,2번 인덱스를 비교하는데 9번인덱스에서 10번 11번이 없으면
                 # 오류가 발생하기 때문에 11번 인덱스까지 빈 리스트 생성

    for i in range(6): # 6장의 카드를 뽑기때문에 6번 반복
        C[num % 10] += 1 # 각 자리수에 해당하는 숫자의 인덱스에 1을 더해줌
        num //= 10 # 나머지 자리수

    i = 0 # while문 종료조건을 위햏 i = 0을 생성
    tri = run = 0 # triplet과 run을 0으로 초기화
    while i < 10: # 9번 인덱스까지만 필요하기때문에 9보다 커지는 시점에서 while문 종료
        if C[i] >= 3: # triplet인지 확인하기 위해 같은 숫자가 3개 있는 경우 아래 코드실행
            C[i] -= 3 # 중복을 피하기 위해 3을 지워줌
            tri += 1 # triplet에 1을 더해줌
            continue # 같은 숫자가 6개 있을 수 있기때문에 다시 triplet이 있는지 확인하기 위해 반복문 다시수행

        if C[i] >= 1 and C[i+1] >= 1 and C[i+2] >= 1: # 연속하는 숫자가 3개 있는 경우 run이기때문에 아래 코드 실행
            C[i] -= 1 # 중복을 피하기 위해 확인한 값들에서 1을 빼줌
            C[i+1] -= 1
            C[i+2] -= 1
            run += 1 # run에 1을 더해줌
            continue # 연속하는 숫자 3개가 각각 2개씩 있을 경우가 있기때문에 반복문 한번 더 실행
        i += 1 # 다음 인덱스를 기준으로 위 코드를 반복

    if run + tri == 2: # run과 triplet의 합이 2이면 baby-gin
        print(1) # baby-gin인 경우 1을 print
    else:
        print(0) # baby-gin이 아닌 경우 0을 print