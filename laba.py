import matplotlib.pyplot as plt
import math as m
yz = []
step = 0.25
eps = 0.000001
x = 0
xz = []
while x < 6:
    x += step
    xz.append(x)
print(xz)
x = 0
def functt(x):
    funct = 1
    n = 0
    q = (-1) * x**2 / ((n + 1)**2 * 4)
    while abs(q) >= eps:
        funct += q
        n += 1
        q *= (-1) * x**2 / ((n + 1)**2 * 4)
    return funct


for i in range(len(xz)):
    yz.append(functt(xz[i]))



print(yz)
print(xz)


plt.plot(xz, yz)
plt.show()

