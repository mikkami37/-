import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math

plot_amount_max=100000
plot_amounts=np.arange(1000,plot_amount_max,1000)
pais=[]
gosa=[]

for plot_amount in plot_amounts:

 naka=0
 soto=0

 xin=[]
 yin=[]
 xout=[]
 yout=[]

 i=0
 while i<=plot_amount:
  
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

 pai=4*naka/plot_amount
 pais.append(pai)
 gosa.append(abs(pai-math.pi))

plt.scatter(plot_amounts,pais)
#plt.scatter(plot_amounts,gosa)
plt.show()