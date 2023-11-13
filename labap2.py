import matplotlib.pyplot as plt
import math as m
y1z = []
x1z = []
step1 = 0.25
eps = 0.000001
x1 = 0
while x1 < 6:
    x1 += step1
    n1 = 0
    funct1 = 1
    q1 = (-1) * m.cos(m.pi)**2 * x1**2 / ((2 * n1 + 2)* (2 * n1 + 1))
    while abs(q1) >= eps:
        funct1 += q1
        n1 += 1
        q1 *= (-1) * m.cos(m.pi)**2 * x1**2 / ((2 * n1 + 2) * (2 * n1 + 1))
    y1z.append(x1)
    print(funct1)
    x1z.append(funct1)
print(x1z)
print(y1z)

plt.plot(y1z, x1z)
plt.show()