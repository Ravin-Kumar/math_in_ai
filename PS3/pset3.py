from random import choices
from string import printable

def matrix_vector(m, v):
    result = [0 for _ in v]
    for idx, row in enumerate(m):
        for j_idx, j_val in enumerate(row):
                result[idx] += v[j_idx]*j_val
    return result


def matrix_power(m, t):
    if t == 1:
        return m

    prev_matrix = matrix_power(m, t-1)

    result_matrix = [[None for _ in range(len(m))] for _ in range(len(m))]
    for i in range(len(m[0])):
        cur_col = [m[j][i] for j in range(len(m[0]))]
        part = matrix_vector(prev_matrix, cur_col)
        for idx, val in enumerate(part):
            result_matrix[idx][i] = val

    return result_matrix


def discrete_ds(m,v,t):
    return matrix_vector(matrix_power(m, t), v)


def unique_char(s):
    return len(set(s))

def words(s):
    return len(s.split(' '))

def frequencies(s):
    freqs = [[i,s.count(i)] for i in set(s)]
    freqs.sort()
    return freqs

def transition(s):

    matrix = [[0 for _ in range(len(printable))] for _ in range(len(printable))]

    for idx, val in enumerate(s):
        try:
            matrix[printable.index(val)][printable.index(s[idx+1])] += 1
        except KeyError:
            matrix[printable.index(val)][printable.index(s[idx+1])] = 1/(s.count(val))
        except IndexError:
            pass

    for row_idx, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum:
            for col_idx, val in enumerate(row):
                matrix[row_idx][col_idx] = val / row_sum

    return matrix

def simulate_string(f, l, i):

    result_string = i

    for _ in range(l-1):
        weights = f[printable.index(result_string[-1])]
        result_string += choices(printable, weights)[0]

    return result_string

if __name__ == '__main__':
    #print(matrix_vector([[-5,2],[-7,4]], [2,7]))
    print(matrix_vector(matrix_power([[0.5,0.1,0.1],[0.3,0.3,0.5],[0.2,0.6,0.4]], 100),[1,1,1]))
    '''
    print(discrete_ds([[0,-1],[1,0]], [2,0], 2))
    print(frequencies('123123123456'))
    matrix = transition('abcdeadbacdceade')
    print(simulate_string(matrix, 3, 'a'))
    '''
    