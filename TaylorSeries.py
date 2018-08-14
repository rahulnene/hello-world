from sympy import *
import numpy as np
from math import factorial
from time import clock
import matplotlib.pyplot as plt
from sympy.functions import sin,cos

x = Symbol('x')

f = x*sin(x+(pi/3))

def taylor(f,x0,order):
    n = 0
    approx = 0
    while n <= order:

        approx += (f.diff(x,n).subs(x,x0))/(factorial(n))*(x-x0)**n
        n += 1

    return approx


# print(taylor(f,0,10))

def plot():

    x_lims = [-5,5]

    x1 = np.linspace(x_lims[0],x_lims[1],800)

    y1 = []

    # Approximate up until 10 starting from 1 and using steps of 2

    for j in range(1,10,1):

        func = taylor(f,0,j)

        # print('Taylor expansion at n='+str(j),func)

        for k in x1:

            y1.append(func.subs(x,k))

        plt.plot(x1,y1,label='order '+str(j))

        y1 = []

    # Plot the function to approximate

    plt.plot(x1,x1*np.sin(x1+(np.pi/3)),label='function of x')

    plt.xlim(x_lims)

    plt.ylim([-5,5])

    plt.xlabel('x')

    plt.ylabel('y')

    plt.legend()

    plt.grid(True)

    plt.title('Taylor series approximation')

    plt.show()


startTime = clock()
plot()
print(clock()-startTime, "s")