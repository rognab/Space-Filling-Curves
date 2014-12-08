import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py

plt.rcParams['figure.figsize'] = (10,10)

# defining a geneneric linear function...
def f(a,b,c):
    return lambda x: a*x + b*x.conjugate() + c


# defining variables and constants for the triangulated space-filling curve 
# via complex values...
w = np.exp(2.0j*np.pi/3)

x = np.array([ w**(-k) for k in range(4) ])
y = 1.0/np.sqrt(3)*x[1:4]


# maps...
B = f( 0, w**1/2, w**2/2)
C = f( w**3/2, 0, w**1/2)
D = f( 0, -w**1*1.0/2, 0)
E = f( w**3/2, 0, w**0/2)


# construcing the space-filling curves for different steps...
# n0 = y
# for k in range(0):
#     n0 = np.concatenate((B(n0), C(n0), D(n0), E(n0)))
# n1 = y
# for k in range(1):
#     n1 = np.concatenate((B(n1), C(n1), D(n1), E(n1)))
# n2 = y
# for k in range(2):
#     n2 = np.concatenate((B(n2), C(n2), D(n2), E(n2)))
# n3 = y
# for k in range(3):
#     n3 = np.concatenate((B(n3), C(n3), D(n3), E(n3)))
# n4 = y
# for k in range(4):
#     n4 = np.concatenate((B(n4), C(n4), D(n4), E(n4)))
n5 = y
for k in range(5):
    n5 = np.concatenate((B(n5), C(n5), D(n5), E(n5)))


# ploting...
fig, ax = plt.subplots()

# functions for rotating and playing around with the complex values..
g = lambda z: z**3

n5_1 = g(n5)

h = lambda z: z**3*np.exp(-2.0j*np.pi/3)

n5_2 = h(n5)

j = lambda z: z**3*np.exp(2.0j*np.pi/3)

n5_3 = j(n5)

# just an outline of the triangle shape...
ax.plot(x.real, x.imag , 'k-', linewidth = 2)
ax.plot((0.5*w**0.5*x).real, (0.5*w**0.5*x).imag , 'k-', linewidth = 2)

# ax.plot( n0.real, n0.imag , 'k-')

# ax.plot( n1.real, n1.imag , 'g-')

# ax.plot( n2.real, n2.imag , 'y-', linewidth=4)

# ax.plot( n3.real, n3.imag , 'g-', linewidth=3)

ax.plot( n5_3.real, n5_3.imag , 'g-', linewidth=1.5)

ax.plot( n5_2.real, n5_2.imag , 'b-', linewidth=1.5)

ax.plot( n5_1.real, n5_1.imag , 'r-', linewidth=1.5)

# ploting the start and end points...
# ax.plot( n5[0].real, n5[0].imag , 'go', markersize=8)
# ax.plot( n5[-1].real, n5[-1].imag , 'ro', markersize=8)

# just a plot of the origin for reference...
# plt.plot( [0], [0], 'bo')

plt.axis('Equal')
# plt.grid(True)
# plt.show()

# sending it to plotly...
plot_url = py.plot_mpl(fig)