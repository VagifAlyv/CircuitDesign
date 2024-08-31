import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

logger = Logging.setup_logging()

circuit = Circuit("Lab 2 exercise 3")

circuit.V('1', 'a', circuit.gnd, 28@u_V)
circuit.V('2', 'd', circuit.gnd, 32@u_V)
circuit.R('1', 'a', 'b', 6@u_Ohm)
circuit.R('2', 'b', 'c', 5@u_Ohm)
circuit.R('3', 'a', 'c', 8@u_Ohm)
R4 = circuit.R('4', 'b', circuit.gnd, 2@u_Ohm)
circuit.R4.plus.add_current_probe(circuit)
circuit.R('5', 'c', 'd', 12@u_Ohm)

simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f" Node {str(node)}: { float(node)}V")

for branch in analysis.branches.values():
    print(f"Branch {str(node)}: {float(node)}A")