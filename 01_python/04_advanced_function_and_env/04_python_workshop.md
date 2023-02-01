# WorkShop

### 간단한 N의 약수 (SWEA #1933)

```python
N = int(input())

# 입력받은 정수 N을 1부터 (0은 나눌 수 없으므로 제외) N까지
# 나누어 떨어지는 값들만 출력한다.
# 오름차순이므로 1부터 시작
for i in range(1, N+1):
    if N % i == 0:
        # 가로로 출력하기 위해 end (print의 default argument)의 값을 변
        print(i, end=' ')
```

### List의 합 구하기

```python
list_sum([1, 2, 3, 4, 5]) # => 15
```

```python
# list_sum 함수를 호출 할 때, 1부터 5까지의 수를 가진 `list`를 넘겨준다.
# 즉, list_sum 함수를 정의할 때, parameter는 리스트 하나를 넘겨 받는다고 가정
# 정의한 numbers parameter는 list 하나를 가지고 있다.
# 이를 순회하여 각 요소들의 값의 합을 구한다.
def list_sum(numbers):
    sum_value = 0
    for number in numbers:
            sum_value += number
    return sum_value
```

### Dictionary로 이루어진 List의 합 구하기

```python
dict_list_sum([{’name’: ’kim’, ’age’: 12},
{’name’: ‘lee’, ’age’: 4}]) # => 16
```

```python
# list_sum과 마찬가지로 dict_list_sum 역시 리스트 하나를 argument로 넘겨받는다.
# 단, 이번에는 해당 리스트 내부에 dict가 담겨 있고,
# 리스트를 순회시 info 변수에는 각 dict가 하나씩 담기게 된다.
# 이를 활용하여 첫 순회시 info에는 infos의 첫번째 dict {’name’: ’kim’, ’age’: 12}가 담겨있다.
# 이때, info['age']를 조회시 12의 값을 얻을 수 있다.
# 이 값을 모두 더해 반환한다.
def dict_list_sum(infos):
    age_sum = 0
    for info in infos:
            age_sum += info['age']
    return age_sum
```

### 2차원 List의 전체 합 구하기

```python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) # => 55
```

```python
# 이번에도 마찬가지로, all_list_sum 함수는 argument로 리스트 하나를 전달받는다.
# 이 리스트가 요소를 가지고 있는 각 리스트들 ([1], [2,3] 등)을 순회하여
# 모든 요소들이 가진 각 정수를 더하도록 한다.
# 이를 위해 num_lists를 한번 순회하여 num_list 변수에 담은 각 리스트들을 다시 순회한다.
# num_list를 순회하면 각 요소들을 하나씩 가져와 값을 더할 수 있다.
# 단, 이때 주의할 점은, 각 값들을 더해나갈 변수의 정의를 모든 반복문 밖에 정의하여야 한다.
def all_list_sum(num_lists):
    lists_sum = 0
    for num_list in num_lists:
            for num in num_list:
                    lists_sum += num
    return lists_sum
```

```python
# 만약, 각 값들을 더할 변수를 첫번째 반복문 안에 정의하면 어떻게 될까?
def all_list_sum(num_lists): # [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    # num_lists를 순회하여 num_list에 [1], [2, 3]이 순차적으로 들어간다.
    for num_list in num_lists:
        # 각 요소들 ([1], [2, 3]...)을 순회할 때 마다 lists_sum이 초기
        lists_sum = 0
        # num_list의 각 요소를 순회
        # num에는 첫번째 순회([1]) 1 | 2번째 순회([2, 3]) 2, 3이 할당
        for num in num_list:
            # lists_sum에 각 값들을 더하고
            lists_sum += num
        print(lists_sum) 
        # [1] : 1 
        # [2, 3] : 5
        # [4, 5, 6] : 15
        # [7, 8, 9, 10] : 34
        # num_list를 순회하고 나면, num_list의 각 요소의 합이 구해지고,
        # 다음 순회로 넘어가면서 lists_sum이 0으로 다시 초기화된다.
        # 그 후, num_list가 다음 요소로 바뀌고 다시 순회를 시작한다.
        # 즉, 만약 lists_sum을 첫번째 순회 안에서 선언하게 되면
        # num_lists의 각 요소들([1], [2, 3] ...)의 개별 합을 구할 수 있다.
    return lists_sum
```

### 숫자의 의미

```python
get_secret_word([83, 115, 65, 102, 89]) # => 'SsAfY'
```

```python
# 파이썬은 각 정수에 해당하는 ASCII 코드를 반환해주는 내장함수 chr
# 이를 활용하여 넘겨받은 리스트의 각 요소를 ASCII 문자로 변환,
# 문자열은 문자열과 덧셈이 가능하고, 이를 사용해 단어를 완성하고 제출한다.
def get_secret_word(numbers):
    # 최종 제출할 word 변수를 빈 문자열로 초기화
    # 이곳에 변환된 문자열을 더해나갈 것이므로 처음부터 문자열로 생성
    word = ''
    # number가 가진 각 숫자들을 number에 할당하며 순회
    for number in numbers:
        # 각 숫자 (83, 115...)를 내장함수 chr() 을 사용해 ASCII코드로 변환
        # 위에서 생성해둔 변수 word에 각 값들을 순서대로 더 한후,
        word += chr(number)
    # 결과 반
    return word

print(get_secret_word([83, 115, 65, 102, 89]))
```

### 내 이름은 몇일까

```python
get_secret_number(’happy’) # => 546
```

```python
# chr()과는 반대로, 문자열을 문자열에 해당하는 ASCII 숫자로 변환해주는
# ord()를 사용하여 각 알파벳을 숫자로 변환하여 더한다.
def get_secret_number(word):
    # 이번에는 정수를 더해 나갈 것이므로, total 변수의 초기값을 0으로 설정
    total = 0
    # 순회하고,
    for char in word:
        # 변환하여 더한 후
        total += ord(char)
    # 결과 반
    return total

get_secret_number('happy') # => 546
```

### 강한 이름

```python
get_strong_word(’z’, ’a’) # => ‘z’
get_strong_word(’delilah’, ’dixon’) # => ‘delilah
```

```markdown
- 함수 정의시 주의해야 할 점은, 인자로 넘겨받을 자료형이 지켜진다는 가정하에
해당 문제를 해결하기 위한 모든 경우에 동일하게 실행될 코드를 작성하여야 한다는 점이다
예를들어, 첫번째 함수 호출시에는 `word1`과 `word2`에 각각 `z`, `a`가 할당된다.
이에따라, ASCII숫자로 변환하기 위해 `ord(word1)` `ord(word2)` 같은 형태로 코드를 작성하게 되면
두번째 함수 호출시에는, `ord('delilah')` 형태가 되어 오류가 발생하게 된다.
- 따라서, 하나의 문자열이라고 하더라도 반복문을 사용하여 순회하도록 한다.
    - 덧붙여, for문은 순회대상인 iterable 객체가 비어있어도 오류를 발생시키지 않는다.
    - 단, 순회할 대상이 없으므로, 내부 코드가 실행되지 않고 종료된다.
    - ex) 비어 있는 리스를 순회할 시, for문 내부 코드는 실행되지 않음.
    ```python
    for _ in []:
        print('A 구역 출력')
    print('B 구역 출력')

    # 실행 결과
    # >>> B 구역 출력
    ```
```

```python
# 두 개의 argument를 넘겨 받을 것이므로 2개의 parameter 작성
def get_strong_word(word1, word2):
    # 각 단어들을 ASCII 숫자로 변환하여 값들을 저장할 것이므로 변수 2개 선언
    word1_total = 0
    word2_total = 0

    # word1과 word2 모두 순회하여야 하므로 반복문 역시 2개 작성
    for char in word1:
        word1_total += ord(char)

    for char in word2:
        word2_total += ord(char)

    # word1과 word2의 결과를 비교하여 둘중 더 큰 값이 있을때 값을 반환하고 함수 종료
    if word1_total > word2_total:
        return word1
    elif word1_total < word2_total:
        return word2
    else:
        # 만약 두 값이 같다면 두 단어 모두 반환
        return word1, word2

print(get_strong_word('delilah', 'dixon')) # delilah
```
