#Code to generate distribution following an arbitrary function. Here the function is x=exp(t)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

#Funtion returns f(t)-x 
def Fy(t):
    return np.exp(t)-x
    

Y=[]
N=10000

for i in range(N): 
    #random number generated from uniform distribution
    x=np.random.uniform()
    #Newton-Raphson method solves for value of t for given value of x.  
    Y.append(newton(Fy,0.5))

fig, ax = plt.subplots()

ax.tick_params(axis='both', labelsize=14)
ax.tick_params(axis='both', length=8, width=2)  # `length` controls tick size

# 🔹 Increase Spine Thickness
for spine in ax.spines.values():
    spine.set_linewidth(2)  # Increase thickness of all spines

# Labels and Title
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel(r"${exp(x)}$", fontsize=18)
ax.set_title(r"$\exp(x)\ Distribution$", fontsize=18)

ax.hist(np.array(Y),bins=100)

plt.show()
