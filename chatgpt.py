#chatgpt가 준 코드
import sympy as sp

# 변수 선언
x = sp.Symbol('x')

# 함수 정의
f = 4*x + 2

# 함수를 x에 대해 적분
integral = sp.integrate(f, x)

# 결과 출력
print("적분 결과:", integral)
