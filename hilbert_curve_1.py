import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import plotly.plotly as py

plt.rcParams['figure.figsize'] = (20,20)

# defining a geneneric linear function...
def f(a,b,c):
    return lambda x: a*x + b*x.conjugate() + c

# symmetries of the Hilbert space-filling curve...
A = [f(0, -0.5j, 0.5 +  1j), f(0.5, 0, 0), f(0.5, 0, 0.5), f(0, 0.5j, 0.5 + 0.5j)]

# initializing the inputs
n = np.array([  0.25 + 0.75j , 0.25 + 0.25j  , 0.75 + 0.25j , 0.75 + 0.75j ])
x = np.array([  0.25 + 0.75j , 0.25 + 0.25j  , 0.75 + 0.25j , 0.75 + 0.75j ])
y = np.array([  0.25 + 0.75j , 0.25 + 0.25j  , 0.75 + 0.25j , 0.75 + 0.75j ])
z = np.array([  0.25 + 0.75j , 0.25 + 0.25j  , 0.75 + 0.25j , 0.75 + 0.75j ])
m = np.array([  0.25 + 0.75j , 0.25 + 0.25j  , 0.75 + 0.25j , 0.75 + 0.75j ])

# construcing the space-filling curves for different steps...
for k in range(0):
    n = np.concatenate([a(n) for a in A])
for k in range(1):
    x = np.concatenate([a(x) for a in A])
for k in range(2):
    y = np.concatenate([a(y) for a in A])
for k in range(3):
    z = np.concatenate([a(z) for a in A])
for k in range(4):
    m = np.concatenate([a(m) for a in A])

# ploting...
fig, ax = plt.subplots()

ax.plot(n.real, n.imag , 'k-', linewidth=7)
ax.plot(x.real, x.imag , 'g-', linewidth=5)
ax.plot(y.real, y.imag , 'b-', linewidth=3)
ax.plot(z.real, z.imag , 'r-', linewidth=1.5)
ax.plot(m.real, m.imag , 'y-')

# matplotlib stufff...
# plt.grid(True)
# plt.axis('equal')
# plt.xlim([-0.5,1.5])
# plt.ylim([-0.5,1.5])
# plt.show()

# plotly stuff...
plot_url = py.plot_mpl(fig)