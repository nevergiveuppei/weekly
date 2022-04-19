
# Purpose1: expand a step function based on the fourier series basis set: {1,sp.cos(2*n*(sp.pi)*x/ll),sp.sin(2*n*(sp.pi)*x/ll)}
# Purpose2: plot the expanded fourier series 

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# N: the number of terms in fouries series
# xx: the x vector in x_axis

def series(N,ll,nx,xx):
    x = sp.symbols('x', commutative=True)
    x0, x1 = -ll/2, +ll/2
    a0= (2/ll)*sp.integrate((-1), (x, x0, 0), manual=True).evalf()+(2/ll)*sp.integrate((1), (x, 0, x1), manual=True).evalf()
    a0=float(a0)
    f = np.zeros(nx)
    for n in range (1,N+1,1):
        an= (2/ll)*sp.integrate((-sp.cos(2*n*sp.pi*x/ll)), (x, x0, 0), manual=True).evalf()+(2/ll)*sp.integrate(sp.cos(2*n*(sp.pi)*x/ll), (x, 0, x1), manual=True).evalf()
        bn= (2/ll)*sp.integrate((-sp.sin(2*n*sp.pi*x/ll)), (x, x0, 0), manual=True).evalf()+(2/ll)*sp.integrate(sp.sin(2*n*(sp.pi)*x/ll), (x, 0, x1), manual=True).evalf()
        f = f+ 0.5*a0 + float(an)*np.cos(2*n*np.pi*xx/ll) + float(bn)*np.sin(2*n*np.pi*xx/ll)        
    return f

# plot
def subplot(plot_index, x, f , xlabel, ylabel):
    plt.subplot( plot_index )
    plt.plot( x, f )
    plt.xlabel( xlabel )
    plt.ylabel( ylabel )

ll=2
nx=100
xx = np.linspace(-ll/2,ll/2,nx)  # define the x vector in x_axis

# plot the step function
yy=np.zeros(nx,dtype=float)
for ii in range(0,nx//2,1):
    yy[ii]=float(-1.0)
for ii in range(nx//2,nx,1):
    yy[ii]=float(1.0)

plt.figure( 1 )
subplot(511, xx, yy, 'x', "step function" )


# plot the fourier series
N = 1
function=series(N,ll,nx,xx)
subplot(512, xx, function, 'x', 'FS'+" N="+str(N) )

N = 10
function=series(N,ll,nx,xx)
plt.figure( 1 )
subplot(513, xx, function, 'x', 'FS'+" N="+str(N) )

N = 100
function=series(N,ll,nx,xx)
subplot(514, xx, function, 'x', 'FS'+" N="+str(N) )

N = 1000
function=series(N,ll,nx,xx)
subplot(515, xx, function, 'x', 'FS'+" N="+str(N) )

plt.show()


