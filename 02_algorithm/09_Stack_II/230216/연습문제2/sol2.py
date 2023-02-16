def powerset(arr, K, result):
    global count
    if sum(result) > 10:
        return
    count += 1
    # 언제까지 부를거냐
    if K == N:
        # 모든 result를 반환하지 않을것
        if sum(result) == 10:
            print(result)
        return
    # K는 아무튼 증가하는데
    # 그 K번째 쓴 경우
    powerset(arr, K+1, result + [arr[K]])
    # 그 K번째 안 쓴 경우
    powerset(arr, K + 1, result)
arr = list(range(1,11))
N = len(arr)
count = 0
# 원본 배열, 사용한 원소 수, 총합리스트(사용할 원소 담을)
powerset(arr, 0, [])
print(count)