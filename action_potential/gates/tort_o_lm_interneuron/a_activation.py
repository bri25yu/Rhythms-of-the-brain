import numpy as np

from action_potential.gates.gate import Gate


class TortOLMInterneuronAActivation(Gate):
    name = "Tort O-LM Interneuron a activation"

    def steady_state(self, V):
        return 1 / (1 + np.exp(-(V + 14) / 16.6))

    def time_constant(self, V):
        return 5.0
