import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

logger = Logging.setup_logging()
circuit = Circuit('Third Circiut')



circuit.R(1, 'b','a', 20@u_Ohm)
circuit.R(2, 'c', 'd', 5@u_Ohm)
circuit.R(3, 'b', circuit.gnd, 10@u_Ohm)
circuit.R(4, circuit.gnd, 'a', 3@u_Ohm)
circuit.R(5, 'c', circuit.gnd, 2@u_Ohm)
circuit.I(1, 'a', 'c', 12@u_A)
circuit.I(2, 'd', 'b', 3@u_A)



simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

analysis = simulator.operating_point()

voltage_node_a = analysis.nodes['a']
voltage_node_b = analysis.nodes['b']
voltage_R1 = float(voltage_node_b) - float(voltage_node_a)

print(f"Voltage across Resistor 1: {voltage_R1}V")


