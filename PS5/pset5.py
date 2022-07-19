import numpy as np



def over_ten(a):
    return [idx for idx, val in enumerate(a >= 10) if val]

def ones(n):
    return np.ones((n,n))

def ones_zeros(n):
    a = np.zeros((n,n))
    for idx, val in enumerate(a):
        if idx == 0 or idx == n-1:
            a[idx] = val+1
        else:
            a[idx][0] = 1
            a[idx][-1] = 1

    return a


def mat_to_vect(m):
    result = []
    for i in m:
        result.append(i)
    return np.array(result).flatten()

if __name__ == '__main__':
    #print(over_ten(np.array([1,2,12,3,4,34,5,6,56,7,8,78,9,0,90])))
    #print(ones(4))
    print(ones_zeros(4))
    #print(mat_to_vect(np.array([[1,2],[3,2],[-2,-2]])))