import sys
sys.stdin = open('input.text')

for tc in range(10): # 테스트 케이스만큼 반복
    Dump = int(input()) # 덤프 횟수를 받음
    arr = list(map(int, input().split())) # 각 상자의 높이를 리스트로 받음

    for i in range(len(arr)-1, 0, -1): # 리스트의 요소가 834개면 인덱스는 833까지 이므로
        for j in range(0, i):          # 버블 정렬을 위해 리스트 요소의 개수 -1을 해주고
            if arr[j] > arr[j+1]:      # 1번 인덱스 까지 반복문 실행하여 버블 정렬
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for k in range(Dump): # 입력받은 덤프의 횟수만큼 반복문 실행
        arr[-1] = arr[-1] - 1 # 1) 정렬했던 리스트의 마지막 요소 -1
        arr[0] = arr[0] + 1 # 2) 정렬했던 리스트의 첫 번째 요소 +1

        for l in range(len(arr) - 1, 0, -1): # 3) 리스트를 다시 버블정렬한 후 1) 2) 3)을 덤프횟수 만큼 반복
            for m in range(0, l):
                if arr[m] > arr[m + 1]:
                    arr[m], arr[m + 1] = arr[m + 1], arr[m]
                else:
                    break
            for m in range(l, 0, -1):
                if arr[m] < arr[m - 1]:
                    arr[m], arr[m - 1] = arr[m - 1], arr[m]
                else:
                    break

    print(f'#{tc+1} {arr[-1] - arr[0]}') # 덤프 횟수만큼 반복한 후 가장 마지막의 요소에서 첫 번째 요소의 값을 빼줌