import numpy as np
eps = 0.00001
a = -1
b = 3
n = 0
#Ищем число шагов
while (((2 / (np.sqrt(5) + 1)) ** (n + 1)) * (b - a) * np.sqrt(5)) >= eps:
    n += 1
#print(n)
x = np.zeros(n+2)
x1 = np.zeros(n+2)
x2 = np.zeros(n+2)
an = np.zeros(n+2)
bn = np.zeros(n+2)
an[0] = a
bn[0] = b

def J(x):
    return x**2

#Задаём число Фибоначчи
Fib = np.zeros(n+2)
for i in range(n+2):

    if i==0 or i==1:
        Fib[i] = 1
    else:
        Fib[i] = Fib[i-1] + Fib[i-2]
    #print(Fib[i])

k=0
for k in range(n+1):
    if k < n:
        x1[k] = an[k] + (b - a) * Fib[n - k]/Fib[n + 1]
        x2[k] = an[k] + (b - a) * Fib[n - k + 1]/Fib[n + 1]
        if J(x1[k]) <= J(x2[k]):
            an[k+1] = an[k]
            bn[k+1] = x2[k]
        else:
            an[k+1] = x1[k]
            bn[k+1] = bn[k]
    else:
        break

print((an[n]+bn[n])/2)
