
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

N = 50000 
T = 15 * 10 ** (-9)

l = 5 * 10 ** (-6)
r = 2 * 10**3
#v = 5

dt = T / N

t = np.empty(N)
Il = np.empty(N)
vR = np.empty(N)
Vi = np.empty(N)

Il[0] = 0
vR[0] = 0

for k in range(N - 1):
    Vi[k] = 5
    Il[k + 1] = Il[k] + dt * Vi[k] / l - (r/l) * Il[k] * dt
    vR[k + 1] = Vi[k] - (l*(Il[k+1] - Il[k]) / dt)
    t[k + 1] = t[k] + dt
  

plt.plot(t, Il, label="Inductor current")
plt.plot(t, vR, label="Resistor voltage")

plt.xlabel("Time (s)")
plt.title("RL circuit simulation")
plt.legend()
plt.show()
