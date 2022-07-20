import numpy as np

arg_max = lambda x : x.index(max(x))

soft_max = lambda x : (np.e**x)*(1/(sum(np.e**x)))

select_train = lambda a, n : np.random.choice(a, size=n, replace=False)

def neural_net_4(w, b, xin):

    hidden_layer = np.dot(w, xin) + b
    output = np.dot(hidden_layer, np.array([2.9,1.2]))
    return output

def neural_net(wa, ba, xin):

    output = xin

    for i in range(len(wa)):
        output = np.dot(wa[i], output) + ba[i]

    return np.dot(output,[1.1,0.9])


