from action_potential.approximations.approximation import Approximation


class Neuron:
    V_0 = -65.0  # in mV

    def __init__(self, action_potential, synapses=None):
        self.action_potential = action_potential
        if synapses is None:
            self.synapses = []
        else:
            self.synapses = synapses

        self.voltage = self.V_0
        self.input_current = 0.0

    def integrate(self, additional_input_current):
        self.input_current += additional_input_current

    def fire(self):
        for synapse in self.synapses:
            synapse.fire()

    def update(self):
        self.action_potential.input_current.set_input_current(self.input_current)
        self.input_current = 0.0

        dv = self.action_potential.f(self.voltage, None)
        self.voltage += Approximation.EPS * dv

    def add_synapses(self, synapses):
        self.synapses.extend(synapses)
