from PySpice.Spice.Netlist import SubCircuit, Circuit

#creating RC circuit that we can reuse
class RC(SubCircuit):
    #naming nodes
    __nodes__ = ('n1', 'n2')
    #creating constructor, name is for subcircuit, then we specify the default values.
    def __init__(self, name, R1 = 1@u_kOhm, C1 = 10@u_uF):
        
        
        #we call the constructor of the class we are inheriting from, and then we pass the name and we then pass all the nodes.
        SubCircuit.__init__(self, name, *self.__nodes__)
        self.R(1, 'n1', 'n2', R1)
        self.C(1, 'n2', 'circuit.gnd', C1)

circuit = Circuit("Second Order RC circuit")

print(circuit)

circuit.subcircuit