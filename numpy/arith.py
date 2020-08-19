import numpy as np
x = np.arange(6).reshape(1,2,3)
print("First array: \n", x)
y = np.arange(6).reshape(1,3,2)
print("Second array : \n", y)
z = np.dot(x, y)
print("Dot product of two arrays : \n", z)
# a = np.array(([1,2], [3,4], [5,6]))
# b = np.array([[1,2,3], [4,5,6]])
# c = np.subtract(a, b)
# print(c)

# 222222222222222222