#ALWAYS WRITTEN PART
import PySpice.Logging.Logging as Logging
import numpy as np
import matplotlib.pyplot as plt

logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit('NOT Gate')
circuit.model('mynmos','NMOS', level=1)
circuit.model('mypmos','PMOS', level=1)
#Until here

# Define the DC supply voltage value
HIGH = 3.3@u_V
LOW = 0@u_V
circuit.V(1,'Vdd',circuit.gnd, HIGH)
circuit.V(2,'in',circuit.gnd, LOW)
circuit.MOSFET(1, 'out', 'in', 'Vdd', 'Vdd', model='mypmos')
circuit.MOSFET(2, 'out', 'in', circuit.gnd, circuit.gnd, model='mynmos')
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

print("NETLIST")
print(circuit)
for node in analysis.nodes.values():
    print('Node {}: {:4.3f} V'.format(str(node), float(node)))
for node in analysis.branches.values():
    print("Branch{}: {:4.6f} A".format(str(node), float(node)))











#ALWAYS WRITTEN PIECE BELOW
#figure, ((ax1, ax2)) = plt.subplots(2, 1, figsize=(8, 5))

figure, ax = plt.subplots(figsize=(20, 10))
ax.grid()
#ax2.grid()
ax.set_xlabel('Time [s]')
ax.set_ylabel('Voltage [V]')

ax.plot(analysis['in1'])
ax.plot(analysis['in1c'])
ax.plot(analysis['out2'])
#ax1.plot(analysis['out2'])

#ax.legend(('in1','in2', 'out'), loc=(.05,.1))
#ax.set_ylim(-1,4)
plt.tight_layout()
plt.show()