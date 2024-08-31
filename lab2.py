import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

logger = Logging.setup_logging()
circuit = Circuit('Third Circiut')

circuit.V('input', 'a', circuit.gnd, 50@u_V)
circuit.R(1, 'a', 'b', 12@u_Ohm)
circuit.R(2, 'a', 'c', 10@u_Ohm)
circuit.R(3, 'b', 'c', 2@u_Ohm)
R4 = circuit.R(4, 'c', circuit.gnd, 5@u_Ohm)
circuit.R4.plus.add_current_probe(circuit)

circuit.I('input', circuit.gnd, 'b', 3@u_A)

simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f" Node {str(node)}: { float(node)}V")

for branch in analysis.branches.values():
    print(f" Branch{str(branch)}: { float(branch)}A")
