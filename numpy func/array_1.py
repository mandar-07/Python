import numpy as np

print("Array Creation Functions:\n")

a = np.array([1, 2, 3])
print("np.array:", a)

b = np.zeros((2, 3))
print("np.zeros:\n", b)

c = np.ones(4)
print("np.ones:", c)

d = np.arange(0, 10, 1)
print("np.arange:", d)

e = np.linspace(0, 1, 5)
print("np.linspace:", e)

f = np.eye(3)
print("np.eye (identity matrix):\n", f)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("2-d array :\n",array_2d)


array_3d=np.zeros((2,3,4))
print("3d Array:\n",array_3d)