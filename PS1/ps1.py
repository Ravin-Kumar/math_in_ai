import sympy
import numpy as np

'''
a = np.array([[0, 0, 0, 0, 0, 0, 1/3, 0],
    [0.5, 0, 0.5, 1/3, 0, 0, 0, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.5, 1/3, 0, 0, 1/3, 0],
    [0, 0, 0, 1/3, 1/3, 0, 0, 0.5],
    [0, 0, 0, 0, 1/3, 0, 0, 0.5],
    [0, 0, 0, 0, 1/3, 1, 1/3, 0]], dtype=np.float64)

b= np.array([0,0,0,0,0,0,0,0])
'''

a = np.array([[6,-2,0,-2],[-2,6,-2,0],[0,-2,6,-2],[-2,0,-2,6]])
b = np.array([3,1,1,-1])

print(np.linalg.solve(a, b))
'''
a = np.array([[0,1/3,0,1/3],[1/3,0,1/3,0],[0,1/3,0,1/3],[1/3,0,1/3,0]], dtype=np.float64)

a = sympy.Matrix(a)

print(a.rref())
'''