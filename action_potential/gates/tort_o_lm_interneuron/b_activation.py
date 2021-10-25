import numpy as np

from action_potential.gates.gate import Gate


class TortOLMInterneuronBActivation(Gate):
    name = "Tort O-LM Interneuron b activation"

    def steady_state(self, V):
        return 1 / (1 + np.exp((V + 71) / 7.3))

    def time_constant(self, V):
        lower = 0.000009 / np.exp((V - 26) / 18.5)
        upper = 0.014 / (0.2 + np.exp(-(V + 70) / 11))
        return 1 / (lower + upper)
