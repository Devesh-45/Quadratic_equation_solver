j=str(input("Enter a equation: "))
j1=j.find("x^2")
a=int(j[0:j1])
print("a=",a)

d=j[::-1]
e=d.find("x")
e1=d.find("2^x")
b=int(d[e+1:e1][::-1])
print("b=",b)

g=j[::-1]
g1=g.find("=")
g2=g.find("x")
c=int(g[g1+1:g2][::-1])
print("c=",c)

y=((b**2)-(4*a*c))**0.5
x1=(-(b)+y)/(2*a)
x2=(-(b)-y)/(2*a)
print("x1=",round(x1,3))
print("x2=",round(x2,3))
