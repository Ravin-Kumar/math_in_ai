import numpy as np

def generate_transition_matrix(a):

    matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b = {'A':0, 'B':1, 'C':2, 'D':3}

    for idx, val in enumerate(a):
        try:
            matrix[b[a[idx+1]]][b[val]] += 1
        except KeyError:
            matrix[b[a[idx+1]]][b[val]] = 1
        except IndexError:
            pass

    for i in matrix:
        col_sum = sum(i)
        for j in i:
            j /= col_sum
    return np.array(matrix)


b = 'AABAAAABCABCAABCAAABCDABABAABCDAB'

print(generate_transition_matrix(b))