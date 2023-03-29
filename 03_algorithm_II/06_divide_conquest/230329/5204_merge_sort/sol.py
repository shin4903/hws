import sys
sys.stdin = open('input.txt')\

def merge_sort(m):
    if len(m) == 1:
        return m
    left = []
    right = m[]
    middle = len(m) // 2

    for i in m[:middle]:
        left.append(i)
    for i in m[middle:]:
        right.append(i)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    l, r = 0, 0
    while len(left) > l or len(right) > r:
        if len(left) > l and len(right) > r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            elif right[r] < left[l]:
                result.append(right[r])
                r += 1
        elif len(left) > l:
            result.append(left[l])
            l += 1
        elif len(right) > r:
            result.append(right[r])
            r += 1
    return result

T = int(input())

for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int,input().split()))

    print(f'#{tc}',merge_sort(arr)[N//2], cnt)

# def msort(start,end):
#     if start == end:
#         return
#     middle = (start+end)//2
#     msort(start,middle)
#     msort(middle+1,end)
#
#     k = 0
#     left, right = start, middle +1
#
#     while left <= middle or right <= end:
#         if left <= middle and right <= end:
#             if arr[left] <= arr[right]:
#                 tmp[k] = arr[left]
#                 left += 1
#             else:
#                 tmp[k] = arr[right]
#                 right +=1
#             k += 1
#         elif left <= middle:
#             while left <= middle:
#                 tmp[k] = arr[left]
#                 left += 1
#                 k += 1
#         elif right <= end:
#             while right <= middle:
#                 tmp[k] = arr[right]
#                 right += 1
#                 k += 1
#     i = 0
#     while i < k:
#         arr[start + i] = tmp[i]
#         i += 1
#     return
# T = int(input())
#
# for tc in range(1,T+1):
#     cnt = 0
#     N = int(input())
#     arr = list(map(int,input().split()))
#     tmp = [0]*N
#     msort(0, N-1)
#     print(tmp)