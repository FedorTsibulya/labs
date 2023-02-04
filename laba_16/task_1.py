import numpy as np

#1
vector_1 = np.arange(12, 43, 1)
#2
vector_2 = np.full(12, 0)
vector_2[5] = 1
#3
matrix_3 = np.arange(0, 9).reshape((3,3))
#4
matrix_4 = np.array([1,2,0,0,4,0])
mx_4_pol = matrix_4[matrix_4 > 0]
#5
a_5 = np.arange(1,16).reshape(5,3)
b_5 = np.arange(2, 8).reshape(3,2)
a_na_b = np.dot(a_5, b_5)
#6
matrix_6 = np.zeros((10, 10), dtype=int)
slice_6 = matrix_6[1:9, 1:9]
slice_6[:, :] = 1
#7
vector_7 = np.random.randint(100, size=6)
vector_7 = np.sort(vector_7)
#8
matrix_8 = np.array([[1,2], [3,4]])
np.ndenumerate(matrix_8)
#9*

#10*

#11*
n = 10
vector_11 = np.random.randint(100, size=(10, 10)).reshape(100)
vector_11 = np.sort(vector_11)
vector_11[-n:]