import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

import matplotlib.pyplot as plt


circuit = Circuit("Circuit")

for i in range(1, 51):
    circuit.SinusoidalVoltageSource(i, i, circuit.gnd, amplitude = (i+1)@u_V, frequency = 50*(i+1)@u_Hz)
    circuit.R(i, i, "A", 1@u_kOhm)


simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)
analysis = simulator.transient(step_time = 100@u_us, end_time = 100@u_ms)

plt.plot(analysis["A"])

plt.show()