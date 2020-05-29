import numpy as np
import matplotlib.pyplot as plt

'''https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html'''
'''https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones_like.html'''

x = np.arange(6)
print x
print "\n"
x = x.reshape((2,3))
print x
print "\n"
print(np.ones_like(x))
print "\n"
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(np.vstack((a,b)))



