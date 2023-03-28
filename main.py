from add import add_func  # 리더가 코딩
from sub import sub_func  # 서브가 코딩
## 함수 선언부

## 전역 변수부
num1, num2, res = 100, 200, 0

## 메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)

res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)


input()
