

def average(a1):
    return sum(a1)/len(a1)

def common(a1,a2):
    for i in set(a1):
        if i in a2:
            return True
    return False

def zerooo(a):
    return ['zerooo' if (type(i) == int or type(i) == float) and i == 0  else i for i in a]

