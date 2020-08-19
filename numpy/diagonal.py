import numpy as np
a = np.array([1, 2, 3, 4])
d = np.diag(a)
print("First MAtrix : \n", d)
x = np.arange(8).reshape(4,2)
print("Second Matrix : \n", x)
z = np.matmul(d,x)
print("Dot product of two matrixs : \n", z)


# 333333333333
