import numpy as np

arr1d = np.array([1, 2, 3])

print(arr1d.dtype)
print(arr1d.shape)
print(arr1d)


arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2d.dtype)
print(arr2d.shape)
print(arr2d)


l = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
arrl = np.array(l)

print(l[1][2])
print(arrl[1][2])   # 인덱싱 두 번 수행
print(arrl[1,2])    # 인덱싱 한 번 수행 -> 권장됨

