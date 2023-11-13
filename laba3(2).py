import matplotlib.pyplot as plt
import math as m
from laba import functt


yz = []
xz = []
#узловые точки
step = 0.25
eps = 0.000001
x = 0


#чебышевские узлы

n = 50
for i in range(1, n):
    x = 1/2 * 6 + 1/2 * 6 * m.cos(((2 * i - 1) / (2 * n - 2)) * m.pi)
    xz.append(x)
xz.reverse()
xz.pop()

# #узловые точки
# while x < 6:
#    x += step
#    xz.append(x)

#значения узловых точек
for i in range(len(xz)):
    yz.append(functt(xz[i]))

l = []
#ksi - значения в серединах отрезков 
ksi = []

for i in range(len(xz) - 1):
    u = (xz[i + 1] + xz[i]) / 2
    ksi.append(u)


print(len(xz))
print(len(yz))


def coef(xz, yz):
    c = []
    for i in range(len(yz)):
        c.append(yz[i])
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            c[j] = (c[j] - c[j - 1]) / (c[j] - c[j - i])
    return c

c = coef(xz, yz)

def newton(c, ksi, xz):
    y = c[n] + (ksi - xz[n])
    for i in range(len(c) - 1, -1, -1):
        y *= (ksi - xz[i]) + c[i]
    return y

ksiz = []
for i in range(ksi):
    ksiz = newton(c, ksi, xz)






# def newton(ksip, xz):
#     z = 0
#     for i in range(len(xz)):
#         f = functt(xz[i])
#         a = 1
#         b = 1
#         for j in range(len(xz)):
#             if i != j:
#                 a *= ksip - xz[j]
#                 b *= xz[i] - xz[j]
#         z += f * a / b   
#     return z

err = []

newtonfunct = []

for i in range(len(ksi)):
    newtonfunct.append(newton(ksi[i], xz))

def error(num):
    return (abs(functt(num) - newton(num, xz)))

for i in range(1, len(ksi)):
    err.append(error(ksi[i]))


print("----------")
print(xz)
#print(newtonfunct)
plt.plot(ksi, ksiz)
#------------
#ksi.pop()
#plt.plot(ksi, err)
plt.show()