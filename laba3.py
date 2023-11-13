import matplotlib.pyplot as plt
import math as m
from laba import functt
yz = []
xz = []
step = 0.25
eps = 0.000001
x = 0

z = 30
#xz - узловые точки
# while x < 16:
#     x += step
#     xz.append(x)

n = 250
for i in range(1, n):
    x = 1/2 * 6 + 1/2 * 6 * m.cos(((2 * i - 1) / (2 * n - 2)) * m.pi)
    xz.append(x)
xz.reverse()



#значения узловых точек
for i in range(len(xz)):
    yz.append(functt(xz[i]))


l = []
ksi = []

#xz - узловые точки
for i in range(len(xz) - 1):
    u = (xz[i + 1] + xz[i]) / 2
    #u = xz[i]
    ksi.append(u)
#ksi - середины отрезков х

#вычисление членов полинома лагранжа
def lagranzh(ksi, xz):
    q = functt(ksi)
    lz = 0
    for i in range(len(xz)):
        sum1 = 1
        for j in range(len(xz)):
            if(i != j):
                sum1 *= ((ksi - xz[j]) / (xz[i] - xz[j]))
        lz += q * sum1 
    return lz

#вычисление погрешности
def error(num):
    return (abs(functt(num) - lagranzh(num, xz)))

#вычисление членов лагранжа от кси
for i in range (len(ksi)):
    l.append(lagranzh(ksi[i], xz))

#print("ksi \n")
#print(ksi)

err = []
for i in range(len(ksi)- 1):
    err.append(error(ksi[i]))

err1 = []

#проверка вычислений
for i in range(1, len(xz)):
    err1.append(error(xz[i]))
#print(err1)
#print('\n')
#print(err)
#print(len(ksi))
print("--------------")
print(len(ksi))

ksi.remove(ksi[0])

print(ksi)
print("-------------")
print(err)

#plt.plot(ksi, l)
plt.plot(ksi, err)
plt.show()
