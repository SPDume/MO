import numpy as np


a = -1
b = 2

n = 100
x = np.zeros(n+1)
x1 = np.zeros(n+1)
x2 = np.zeros(n+1)
an = np.zeros(n+1)
bn = np.zeros(n+1)

an[0] = a
bn[0] = b


def J(x):
    return x**2


i = 1
for i in range(n):
    i+=1
    x1[i-1] = an[i-1] + ((3-np.sqrt(5))/2)*(bn[i-1] - an[i-1])

    #print(i)
    #print(x1[i - 1])
    x2[i-1] = an[i-1] + ((np.sqrt(5)-1)/2)*(bn[i-1] - an[i-1])

    #print(x2[i - 1])
    if J(x1[i-1]) <= J(x2[i-1]):
        an[i] = an[i-1]
        bn[i] = x2[i-1]
        x[i] = x1[i-1]
    else:
        an[i] = x1[i-1]
        bn[i] = bn[i-1]
        x[i] = x2[i-1]




print(x[i])


