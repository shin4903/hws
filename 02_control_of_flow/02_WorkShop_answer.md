# WorkShop

### 숫자의 입력과 출력

- 입력 받은 데이터를 숫자로 변환하고 덧셈해서 출력하는 프로그램을 작성하시오.
  (힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.)

```markdown
[입력]
숫자를 2번 입력받는다.
[출력]
입력 숫자를 계산하여 값을 출력한다.
[입력 예시]
6374
8729
[출력 예시]
15103
```
```python
num = int(input())
num2 = int(input())

print(num + num2)
```




### Dictionary를 활용하여 평균 구하기

좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
점심메뉴의 평균 값을 출력하시오.

```python
dict = {'차돌김치찌개':7000, '카레면':3500, '버터바지락찜파스타':12000, '잡채밥':6500}
price = 0
count = 0

for key in dict:
    price += dict[key]
    count += 1

print(price/count)
```
