import numpy as np

from action_potential.approximations.approximation import Approximation


class Synapse:
    tau_R = None
    tau_D = None
    V_rev = None

    def __init__(self, conductance, neuron1, neuron2):
        self.conductance = conductance
        self.neuron1 = neuron1
        self.neuron2 = neuron2

        self.s = 0.0

    def fire(self):
        heaviside = (1 + np.tanh(self.neuron1.voltage / 4)) / 2
        ds = (heaviside * (1 - self.s) / self.tau_R) - self.s / self.tau_D
        self.s += ds * Approximation.EPS

        input_current = np.sum(self.conductance * self.s) * (self.V_rev - self.neuron2.voltage)
        self.neuron2.integrate(input_current)
