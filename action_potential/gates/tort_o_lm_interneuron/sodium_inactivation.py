import numpy as np

from action_potential.gates.tort_o_lm_interneuron.gate import TortOLMInterneuronGate


class TortOLMInterneuronSodiumInactivation(TortOLMInterneuronGate):
    name = "Tort O-LM Interneuron Sodium inactivation"

    def alpha(self, V):
        return 0.07 * np.exp(-(V + 63) / 20)

    def beta(self, V):
        return 1 / (1 + np.exp(-(V + 33) / 10))
