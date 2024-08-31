
import PySpice.Logging.Logging as Logging
import numpy as np
import matplotlib.pyplot as plt

logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("RC Circuit")

# Define circuit components

circuit.PieceWiseLinearVoltageSource(1, "n_in", circuit.gnd, values = [(0, 0), (0, 10@u_V)])
circuit.R(1, "n_in", "a", 1000@u_kOhm)
circuit.R(2, "a", "b", 1000@u_kOhm)
circuit.R(3, 'b', 'n_out', 1000@u_kOhm)
circuit.C(1, 'a', circuit.gnd, 0.1@u_uF)
circuit.C(2, 'b', circuit.gnd, 0.1@u_uF)
circuit.C(3, 'n_out', circuit.gnd, 0.1@u_uF)

simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)
analysis = simulator.transient(step_time=1@u_us, end_time=125@u_ms)

dict1 = analysis.nodes

plt.style.use("ggplot")

plt.plot(dict1["n_in"], label = "Vin")
plt.plot(dict1["a"], label = "Va")
plt.plot(dict1["b"], label = "Vb")
plt.plot(dict1["n_out"], label = "Vout")
plt.legend()
plt.show()