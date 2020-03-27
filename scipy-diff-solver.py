# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from seaborn import set_style

set_style('whitegrid')
# %%
# Example 1: exponential decay
def exponential_decay(t, y):
    return -0.5 * y


# %%
sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
# %%
for i in range(3):
    plt.plot(sol.t, sol.y[i])

plt.xlabel(r'$t$')
plt.ylabel(r'$y$')
# %%
# Example 2: Cannon fired upwards
def upward_cannon(t, y):
    return [y[1], -0.5]


def hit_ground(t, y):
    return y[0]


def apex(t, y):
    return y[1]


hit_ground.terminal = True
hit_ground.direction = -1
# %%
sol = solve_ivp(
    fun=upward_cannon,
    t_span=[0, 100],
    y0=[0, 10],
    events=(hit_ground, apex),
    dense_output=True,
)
# %%
t = np.linspace(0, *sol.t_events[0], 100)
pos = sol.sol(t)
fig, ax = plt.subplots(2, 1,)
ax[0].plot(t, pos[0])
ax[0].set_title('Cannon Launch Example')
ax[0].set_ylabel(r'$y$', rotation='horizontal')
_, ymax = ax[0].get_ylim()
ax[0].set_ylim(0, ymax)
ax[0].annotate(
    s='apex',
    xy=[sol.t_events[1], sol.y_events[1].ravel()[0]],
    xytext=(-10, -50),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='k')
)
ax[1].plot(t, pos[1])
ax[1].set_ylabel(r"$y'$", rotation='horizontal')

for i in range(2):
    _, xmax = ax[i].get_xlim()
    ax[i].set_xlim(0, xmax)

# %%
# Example 3: Lotka-Volterra equations


def lotkavolterra(t, z, a, b, c, d):
    x, y = z
    return [a*x - b*x*y, -c*y + d*x*y]


# %%
sol = solve_ivp(
    fun=lotkavolterra,
    t_span=[0, 15],
    y0=[10, 5],
    args=(1.5, 1, 3, 1),
    dense_output=True
)
# %%
t = np.linspace(0, 15, 300)
z = sol.sol(t)
# %%
plt.plot(t, z.T);
plt.xlabel('t')
plt.legend(['prey', 'predators'], shadow=True)
plt.title('Lotka-Volterra System')
