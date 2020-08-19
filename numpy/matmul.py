import numpy as np
x = np.arange(8).reshape(4, 2)
a = x.transpose()
y = np.random.randint(low = 9, size = (4, 2))
b = y.transpose()
print("First Transposed matrix is : \n", a,"\n Second Transposed matrix is : \n", b)
c = np.add(a, b)
print("Addition of \n{0}\n and \n{1} is \n{2} : \n".format(a,b,c))
d = np.subtract(a, b)
print("Subtraction of \n{0}\n and \n{1} is \n{2} : \n".format(a,b,d))
e = np.multiply(a, b)
print("Multiplication of \n{0}\n and \n{1} is \n{2} : \n".format(a,b,e))
f = np.divide(a, b)
print("Multiplication of \n{0}\n and \n{1} is \n{2} : \n".format(a,b,f))


# 44444444444444444