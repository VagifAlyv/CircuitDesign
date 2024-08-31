import PySpice.Logging.Logging as Logging
import numpy as np
import matplotlib.pyplot as plt

logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit('Seventh Week')

source = circuit.PulseVoltageSource('input', 'in', circuit.gnd, initial_value=0@u_V, pulsed_value=10@u_V, pulse_width=100@u_ms, period=200@u_ms)
circuit.L(1, "a", "out", 10@u_mH)
circuit.C(1, "out", circuit.gnd, 0.1@u_uF)
circuit.R(1, "in", "a", 50@u_Ohm)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=0.1@u_us, end_time=1000@u_us)

plt.plot(analysis["out"], label = "Voltage")

plt.grid()
plt.legend()
plt.show()
