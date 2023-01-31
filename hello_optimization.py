# This is a short program to illustrate the minimize optimizer in scipy "hello world"-style

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# objective function (f) and constraints (g1, g2)
# with the design variable x, representing [x1, x2]
def f(x):
    return (1-x[0])**2 + (1-x[1])**2 +0.5*(2*x[1]-x[0]**2)**2
def g1(x):
    return 1-x[0]**2-x[1]**2
def g2(x):
    return 5-x[0]-3*x[1]

# initial condition
x0 = [1,1]

# running the optimizer
_bounds = ((-5,5), (-5,5)) # bounds for each design variable, tuple of tuples (each design variable has it's own tuple)
_constraints = [{'type':'ineq', 'fun':g1}, {'type':'ineq', 'fun':g2}] # list of dictionaries
# inequality constraints have to evaluate to be non-negative
res = minimize(f, x0, constraints=_constraints, bounds=_bounds, tol=1e-6) # objective, initial conditions, etc.

print(res)
print("The optimal point x* is", res.x)

# inputs vectors for the contour plot
n1 = 100
n2 = 99
x1 = np.linspace(-5,5,n1)
x2 = np.linspace(-5,5,n2)

fun = np.zeros([n1,n2])
con1 = np.zeros([n1,n2])
con2 = np.zeros([n1,n2])

# function evaluations for the contour plot
for i in range(n1):
    for j in range(n2):
        fun[i,j] = f([x1[i],x2[j]]) 
        con1[i,j] = -g1([x1[i],x2[j]]) 
        con2[i,j] = -g2([x1[i],x2[j]]) 

# plotting
plt.figure()
plt.contour(x1, x2, np.transpose(fun),100)
plt.colorbar()
plt.contourf(x1, x2, np.transpose(con1),[0,1000], alpha=0.2, colors='red')
plt.contourf(x1, x2, np.transpose(con2),[0,1000], alpha=0.2, colors='red')
plt.plot(res.x[0],res.x[1],'r*')
plt.show()