import numpy as np
import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70,80,90,100,110,120,130]
y=[174,216,255,290,325,361,399,433,460,480,495,500,502]

x=np.array(x)
y=np.array(y)

plot=plt.plot(x,y,'b*',label='original values')
fit=np.polyfit(x,y,2)
print(fit)
p1=np.poly1d(fit)
print("拟合曲线：",p1)
yvals=p1(x)
plot2=plt.plot(x,yvals,"r",label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ployfit')
plt.legend()
plt.show()
