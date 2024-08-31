import matplotlib.pyplot as plt
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit('CMOS Logic Circuit')

# Define the DC supply voltage value
VDD = 5 @ u_V

# Input signals
a = circuit.PulseVoltageSource('in1', 'a', circuit.gnd,
                               initial_value=0 @ u_V, pulsed_value=5 @ u_V,
                               pulse_width=100 @ u_ms, period=200 @ u_ms, delay_time=0 @ u_ms)

b = circuit.PulseVoltageSource('in2', 'b', circuit.gnd,
                               initial_value=0 @ u_V, pulsed_value=5 @ u_V,
                               pulse_width=50 @ u_ms, period=100 @ u_ms, delay_time=0 @ u_ms)

c = circuit.PulseVoltageSource('in3', 'c', circuit.gnd,
                               initial_value=0 @ u_V, pulsed_value=5 @ u_V,
                               pulse_width=25 @ u_ms, period=50 @ u_ms, delay_time=0 @ u_ms)

# PMOS transistors for pull-up network
circuit.MOSFET(1, 'p1', 'a', 'Vdd', 'Vdd', model='mypmos')
circuit.MOSFET(2, 'p2', 'b', 'Vdd', 'Vdd', model='mypmos')
circuit.MOSFET(3, 'p3', 'c', 'Vdd', 'Vdd', model='mypmos')

# NMOS transistors for pull-down network
circuit.MOSFET(4, 'n1', 'b', 'out', circuit.gnd, model='mynmos')
circuit.MOSFET(5, 'n2', 'c', 'out', circuit.gnd, model='mynmos')

# Connect the pull-up and pull-down networks
circuit.R(1, 'Vdd', 'out', 10 @ u_Ohm)
circuit.R(2, 'out', circuit.gnd, 10 @ u_Ohm)



simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=a.period/5000, end_time=a.period*1)

figure, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(6, 4))

ax1.plot(analysis['a'])
ax2.plot(analysis['b'])
ax3.plot(analysis['c'])
ax4.plot(analysis['out'])

plt.tight_layout()
plt.show()
