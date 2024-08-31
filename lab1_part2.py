import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

logger = Logging.setup_logging()
circuit = Circuit('Second Circiut')

circuit.V(1, 'node_B', circuit.gnd, 5@u_V)
circuit.R(1, 'node_B', circuit.gnd, 1@u_kΩ)
circuit.R(2, 'node_B', 'node_A', 1@u_kΩ)
circuit.R(3, 'node_A', circuit.gnd,1@u_kΩ)

simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f" Node {str(node)}: { float(node)}V")

for branch in analysis.branches.values():
    print(f" Branch {str(branch)}: { float(branch)}A")

print(circuit)