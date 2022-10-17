import pylab as pl


a = []

for i in range(2000):
    a.append(i)
    c = a * 3
    b = pl.plot(a)
    d = pl.plot(c)

pl.show()
pl.show()