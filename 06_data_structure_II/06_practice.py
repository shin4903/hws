# # 아래에 코드를 작성하세요. (for문 활용하여 풀기)
# def sum_list(numbers):
#     result = 0
#     for num in numbers:
#         for i in num:
#             result += i
#     return result      

# print(sum_list([[1, 4], [10, 5], [20, 30]]))


# # 아래에 코드를 작성하세요. (인덱스를 이용하여 풀기)
# def sum_list_index(numbers):
#     result = 0
#     for elem in range(len(numbers)):
#         for i in range(len(numbers[elem])):
#             result += numbers[elem][i]
#     return result
# print(sum_list_index([[1, 4], [10, 5], [20, 30]]))

# # 아래에 코드를 작성하세요. (while이용해서 풀기)
# def sum_list_while(numbers):
#     cnt = 0
#     result = 0
#     while len(numbers) > cnt:
#         for i in range(len(numbers[cnt])):
#             result += numbers[cnt][i]
#         cnt += 1
#     return result

# print(sum_list_while([[1, 4], [10, 5], [20, 30]]))

# # 아래에 풀이를 작성하세요. 함수 정의는 필요없습니다. (학생별 점수 총합)
# students = [
#  [100, 80, 100],
#  [90, 90, 60],
#  [80, 80, 80]
# ]
# for i in students:
#     result = 0
#     for j in i:
#         result += j
#     print(result)

# # 아래에 풀이를 작성하세요. 함수 정의는 필요없습니다. (과목별 점수 총합)
# students = [
#  [100, 80, 100],
#  [90, 90, 60],
#  [80, 80, 80]
# ]
# for i in range(len(students)):
#     result = 0
#     for j in students:
#         result += j[i]
#     print(result)

# 주어진 문자열에서 제시된 알파벳의 등장 위치를 리스트로 반환
def my_find(text, alphabet):
    pass


print(my_find('apple', 'p'))
print(my_find('a', 'p')