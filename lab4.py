
import PySpice.Logging.Logging as Logging
import numpy as np
import matplotlib.pyplot as plt

logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("RC Circuit")

# Define circuit components

circuit.R(1, "a", "b", 100@u_kOhm)

source = circuit.PieceWiseLinearVoltageSource(1, "a", circuit.gnd, values=[(0, 0), (0, 10@u_V)])

circuit.C(1, "b", circuit.gnd, 0.1@u_nF)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)

# Perform transient analysis from t=0s to t=1ms with a time step of 1μs
analysis = simulator.transient(step_time=100@u_us, end_time=1@u_ms)

# Extract node voltages during the transient analysis
node_voltages = analysis.nodes

# Extract voltage at node "b"
voltage_at_b = node_voltages["b"]

# Create a plot of voltage at node "b" over time
plt.plot(analysis.time, voltage_at_b)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Transient Analysis of Voltage at Node 'b'")
plt.grid(True)

# Display the plot
plt.show()
