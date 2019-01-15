import decimal as d
d.getcontext().prec=20
pi=d.Decimal(0)
for n in range(40000000):
    pi+=d.Decimal(4)/d.Decimal((2*n+1)*((-1)**n))
print(pi)
