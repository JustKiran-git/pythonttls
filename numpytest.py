import numpy as np
'''
print(np.__version__)
np.show_config()

Z = np.zeros(10)
print(Z)

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))

Z = np.zeros(10)
Z[4] = 1
print(Z)

Z = np.arange(10,50)
print(Z)

Z = np.arange(50)
Z = Z[::-1]
print(Z)

Z = np.arange(9).reshape(3, 3)
print(Z)

nz = np.nonzero([1,2,0,0,4,0])
print(nz)

Z = np.eye(3)
print(Z)

Z = np.random.random((3,3,3))
print(Z)

Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

Z = np.random.random(30)
m = Z.mean()
print(m)

Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)'''







































