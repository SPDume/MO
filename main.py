import numpy as np

e =0.00001
a = -2
b = 3
d = 2*e

n = 100
x1 = np.zeros(n+1)
x2 = np.zeros(n+1)
an = np.zeros(n+1)
bn = np.zeros(n+1)
en = np.zeros(n+1)



an[0] = a
bn[0] = b


def J(x):
    return x**2


#for i in range(n-1) :
#    en=(b[i]-a[i]-d)/2**(n+1)+d/2
i = 1


for i in range(n+1):
    x1[i-1] = (an[i-1] + bn[i-1] - d)/2
    x2[i-1] = (an[i-1]+bn[i-1]+d)/2
    en = (bn[i-1] - an[i-1] - d) / 2 ** (i + 1) + d / 2
    if J(x1[i-1]) <= J(x2[i-1]):
        an[i] = an[i-1]
        bn[i] = x2[i-1]
    else:
        an[i] = x1[i-1]
        bn[i] = bn[i-1]
    i+=1
    #print(i)

xans = (an[n]+bn[n])/2
print(xans)


