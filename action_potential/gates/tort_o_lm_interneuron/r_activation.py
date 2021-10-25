import numpy as np

from action_potential.gates.gate import Gate


class TortOLMInterneuronRActivation(Gate):
    name = "Tort O-LM Interneuron r activation"

    def steady_state(self, V):
        return 1 / (1 + np.exp((V + 84) / 10.2))

    def time_constant(self, V):
        return 1 / (np.exp(-14.59 - 0.086 * V) + np.exp(-1.87 + 0.0701 * V))
