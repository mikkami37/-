import matplotlib.pyplot as plt
import random as rd
max=10000
naka=0
soto=0

xin=[]
yin=[]
xout=[]
yout=[]

i=0
while i<=max:
  
  num1=rd.uniform(0,1)
  num2=rd.uniform(0,1)

  if num1**2+num2**2 <= 1:
      xin.append(num1)
      yin.append(num2)
      naka+=1
  else:
      xout.append(num1)
      yout.append(num2)
      soto+=1
  
  i+=1

pai=4*naka/max
print(pai)
plt.scatter(xin,yin)
plt.scatter(xout,yout)
plt.show()