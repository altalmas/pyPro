import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-4,4,1)
x = np.linspace(-4,2*np.pi,25)
ysin = np.sin(x)
y = x*x
y2 = x*x + 2
y3 = np.square(x) - 3
plt.grid(True)
plt.xlabel('My X values')
plt.ylabel('My Y values')
plt.title('My title')
#plt.axis([0,5,-1,11])
plt.plot(x,ysin,'g-^',linewidth=3, markersize=16, label='Sin(x)')
plt.plot(x,y,'b-^',linewidth=3, markersize=16)
plt.plot(x,y2,'r-o',linewidth=3, markersize=16)
plt.plot(x,y3,'y-*',linewidth=3, markersize=16)
plt.legend() # not working?
plt.show()
