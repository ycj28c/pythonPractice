import numpy as np
import matplotlib.pyplot as plt

'''http://matplotlib.org/api/pyplot_api.html'''

x = np.arange(6)
print x
print "\n"
x = x.reshape((2,3))
print x
print "\n"
print(np.ones_like(x))
print "\n"
y = np.sin(x)
plt.plot(x,y)
print y
print "\n"
plt.show()
