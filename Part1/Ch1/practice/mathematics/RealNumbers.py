import numpy as np

print(np.pi)
print(np.e)
# np.exp(x) = np.power(np.e, x)
print(np.exp(0), np.exp(1), np.exp(2), np.exp(3))

f = 3.1415
print(f)
print(type(f))  # Python은 내부적으로 double-precision float64를 기본으로 사용

# 수치 오류
x = 0.1 + 0.2
print(x)        # 0.30000000000000004

a = np.float64(1.00000001)
b = np.float64(1.00000000)
print(a - b)    # 9.99999993922529e-09

a = np.float32(1.00000001)
b = np.float32(1.00000000)
print(a - b)    # 0.0

sum1 = 10000000.0
for i in range(10000000):
    # 아주 큰 숫자에 여러 번 더해도 더해지지 않음.
    sum1 += 0.0000000001
print(sum1)     # 10000000.0

# 위의 문제를 해결하기 위해 처음에 아주 작은 수부터 시작함.
sum2 = 0.0
for i in range(10000000):
    # 작은 값들을 더하여 누적함.
    sum2 += 0.0000000001
# 마지막에 큰 값을 더하여 작은 값이 무시되지 않도록 함.
sum2 += 10000000.0
print(sum2)     # 10000000.001

