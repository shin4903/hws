# idx = 조사 시작할 대상
def comb(depth, idx, r):
    if depth == r:
        print(check)
    else:
        for i in range(idx, len(nums)):
            check[depth] = nums[i]
            comb(depth + 1, i +1, r)
            # i + 1 -> 구간의 시작점을 현재 조사한 대상 i번쨰 다음 조사부터 시작
            # i + 1 -> i 로 바꾸면 중복있는 조합
nums = [1, 2, 3]
check = [0] * 2
comb(0, 0, 2)
