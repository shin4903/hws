# idx : 조사 시작할 대상
def comb(depth, idx, r):
    if depth == r:
        print(check)
    else:
        for i in range(idx, len(nums)):
            check[depth] = nums[i]
            comb(depth + 1, i + 1, r)
            # i + 1 -> 구간의 시작점을 현재 조사한 대상 i번째 다음 조사부터 시작

nums = [1, 2, 3]
check = [0] * 2
comb(0, 0, 2)

print()

# idx : 조사 시작할 대상
def comb(depth, idx, r):
    if depth == r:
        print(check)
    else:
        for i in range(idx, len(nums)):
            check[depth] = nums[i]
            comb(depth + 1, i, r)
            # i + 1 -> 구간의 시작점을 현재 조사한 대상 i번째 다음 조사부터 시작

nums = [1, 2, 3, 4, 5, 6, 7]
check = [0] * 5
comb(0, 0, 5)