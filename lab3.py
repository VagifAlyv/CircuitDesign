import numpy as np
import matplotlib.pyplot as plt

import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

logger = Logging.setup_logging()

circuit = Circuit("Circuit")

circuit.SinusoidalVoltageSource("voltageSource1", "A", circuit.gnd, amplitude= 2@u_V, frequency= 50@u_Hz)
circuit.SinusoidalVoltageSource("voltageSource2", "B", circuit.gnd, amplitude= 5@u_V, frequency= 50@u_Hz)
circuit.SinusoidalVoltageSource("voltageSource3", "C", circuit.gnd, amplitude= 8@u_V, frequency= 50@u_Hz)

circuit.R(1, "A", "D" , 1@u_kOhm)
circuit.R(2, "B", "D" , 1@u_kOhm)   
circuit.R(3, "C", "D" , 1@u_kOhm)


simulator = circuit.simulator(temperature = 25 , nominal_temperature = 25)
analysis = simulator.transient(step_time = 100@u_us, end_time = 100@u_ms)


plt.plot(analysis["A"])
plt.plot(analysis["B"])
plt.plot(analysis["C"])
plt.plot(analysis["D"])

plt.show()
