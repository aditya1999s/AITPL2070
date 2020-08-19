import numpy as np
x = np.random.randint(low = 9, size = (4, 2))
y = np.random.randint(low = 9, size = (2, 4))
z = np.random.randint(low = 9, size = (2, 2))
# a = np.matmul(x, y)
# b = np.matmul(a, z)
# print(b)
# a = (x*y*z)+(y*z)+x
a = np.matmul(x,y)
print(a)
print(x)
print(y)
print(z)