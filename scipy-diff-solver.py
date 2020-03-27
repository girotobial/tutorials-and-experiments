# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# %%
# Example 1: exponential decay
def exponential_decay(t, y):
    return -0.5 * y


# %%
sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
# %%
for i in range(3):
    plt.plot(sol.t, sol.y[i])
