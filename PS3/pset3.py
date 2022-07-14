import numpy as np
from string import ascii_letters

def matrix_vector(m, v):
    return np.dot(m, v)


def matrix_power(m, t):
    if t == 1:
        return m
    return np.dot(m,matrix_power(m, t-1))


def discrete_ds(m,v,t):
    return matrix_vector(matrix_power(m, t), v)


def unique_char(s):
    return sum(set(s))

def words(s):
    return len(s.split(' '))

def frequencies(s):
    return [[i,s.count(i)] for i in set(s)]

def transition(s):

    matrix = np.zeros((48,48))


    for idx, val in enumerate(s):
        try:
            matrix[ascii_letters.index(s[idx+1])][ascii_letters.index(val)] += 1
        except KeyError:
            matrix[ascii_letters.index(s[idx+1])][ascii_letters.index(val)] = 1/(s.count(val))
        except IndexError:
            pass

    for i in matrix:
        col_sum = sum(i)
        i /= col_sum
    return np.array(matrix)

if __name__ == '__main__':
    print(matrix_vector([[-5,2],[-7,4]], [[2],[7]]))
    print(matrix_power([[0,-1],[1,0]], 2))
    print(discrete_ds([[0,-1],[1,0]], [[2],[0]], 2))
    print(frequencies('123123123456'))