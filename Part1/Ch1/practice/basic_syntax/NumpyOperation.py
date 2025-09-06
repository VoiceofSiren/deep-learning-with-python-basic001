import numpy as np

a = np.array([1, 2, 3]) # 1차원 배열 (벡터)
b = np.array([4, 5, 6]) # 1차원 배열 (벡터)

a_mul_b = a * b         # 원소별 곱셈 (Hadamard product)
a_dot_b = np.dot(a, b)  # 벡터 dot 연산
a_at_b = a @ b          # 여기에서는 np.dot(a, b)와 동일함.

print(a_mul_b)
print(a_dot_b)
print(a_at_b)


c = np.array([[1, 2],
             [3, 4]])
d = np.array([[5, 6],
              [7, 8]])
c_mul_d = c * d                 # 원소별 곱셈 (Hadamard product)
c_matmul_d = np.matmul(c, d)    # 행렬 곱셈
c_at_d = c @ d                  # 여기에서는 np.matmul(c, d)와 동일함.

print(c_mul_d)
print(c_matmul_d)
print(c_at_d)


e = np.array([[1, 2, 3],
              [4, 5, 6]])   # 2차원 배열 (2x3 행렬)
f = np.array([[10, 11],
              [20, 21],
              [30, 31]])    # 2차원 배열 (3x2 행렬)

# 원소별 곱셈 e * f는 e와 f의 shape이 동일하지 않아 불가함.
e_matmul_f = np.matmul(e, f)
e_at_f = e @ f

print(e_matmul_f)
print(e_at_f)