# depth = 현재 조사 중인 위치
# r = 최대 조사하려는 대상의 수

def perm(depth, r):
    if depth == r:
        print(check)
    else: # check에 아직 r개 만큼의 대상이 채워지지 않았음
        # nums가 가진 모든 대상을 조사
        for i in range(len(nums)):
            if not visited[i]: # nums의 i번쨰를 아직 사용 안했다만
                visited[i] = True
                check[depth] = nums[i] # check[0] = nums[0]
                perm(depth + 1, r)
                visited[i] = False

nums = [1, 2, 3]

visited = [0] * len(nums)

check = [0] * 2

print(visited, check)
perm(0,2)