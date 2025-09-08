i = 123

print(i)
print(type(i))
print(123 + 456)

import numpy as np

j = np.int32(123)

print(j)
print(type(j))

k = np.uint32(123)  # unsigned integer 32bit = 4bytes
# k = np.uint32(-123) -> OverflowError: Python integer -123 out of bounds for uint32

print(k)
print(type(k))
