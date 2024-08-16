import matplotlib.pyplot as plt

h=0.001
tmax=30 
nsteps=int(tmax/h)
m=1 #質量
k=1 #ばね定数
a=1

#初期条件
t=[0]
x=[5]
v=[0]

#修正オイラー法
i=0
while i<=nsteps:

 d2x=-(k/m)*x[i] #運動方程式

 vhalf=v[i]+0.5*d2x*h
 xhalf=x[i]+0.5*v[i]*h
 d2xhalf=-(k/m)*xhalf

 v.append(v[i]+d2xhalf*h)
 x.append(x[i]+vhalf*h )

 t.append(t[i]+h)
 i+=1


plt.scatter(t,x)
plt.show()