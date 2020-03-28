# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Differential equations
def S_dash(t, S, I, transm):
    return - transm * S * I


def I_dash(t, S, I, transm, recov):
    return transm*S*I - recov*I


def R_dash(t, S, I, recov):
    return recov*I


def SIR_model(t, y, transm, recov):
    S, I, R = y
    return [
        S_dash(t, S, I, transm),
        I_dash(t, S, I, transm, recov),
        R_dash(t, S, I, recov)
    ]
# %%
# Setup initial conditions
# Population size, N
population_size = 1
# Number of infected people at the start
infected_start = 0.001
# Number of susceptible people at the start
susceptible_start = population_size - infected_start
# Number of recovered
recovered_start = 0.

# %%
# Variables
basic_reproduction_number = 2.1
recovery_time = 2
recov_rate = recovery_time**-1
transm_rate = basic_reproduction_number * recov_rate / population_size
max_time = 24

# %%
sol = solve_ivp(
    fun=SIR_model,
    t_span=[0, max_time],
    y0=[susceptible_start, infected_start, recovered_start],
    args=(transm_rate, recov_rate),
    dense_output=True
)
t = np.linspace(0, max_time, 300)
y = sol.sol(t).T
labels = ['Susceptible', 'Infected', 'Recovered']
plt.plot(t, y)
plt.xlabel('Time')
plt.title(f'SIR Model $R_0$={basic_reproduction_number}');
for i, label in enumerate(labels):
    plt.text(t[-1] + 0.1, y[-1, i], label, color=f'C{i}')
plt.ylim(0, 1)
_, max_x = plt.xlim()
plt.xlim(0, max_x * 1.2)
sns.despine()
plt.show()
