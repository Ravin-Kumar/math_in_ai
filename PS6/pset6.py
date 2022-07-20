import numpy as np

paraboloid = lambda x, y : x**2 + y**2
sigmoid = lambda x : 1/(1+np.e**(-x))
relu = lambda x : x if x >=0 else 0
neural_net_1 = lambda x1, x2 : 0.3*(0.1*x1 + 0.1*x2) + 0.7*(0.5*x1 + 0.2*x2)
neural_net_2 = lambda x1, x2 : (0.1*x1 + 0.1*x2 + 1.5) + 0.7*(0.5*x1 + 0.2*x2 + 2.1)
neural_net_3 = lambda x1, x2 : sigmoid(0.1*x1 + 0.1*x2 + 1.5) + 0.7*relu(0.5*x1 + 0.2*x2 + 2.1)

