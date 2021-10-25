import numpy as np

from action_potential.gates.tort_o_lm_interneuron.gate import TortOLMInterneuronGate


class TortOLMInterneuronSodiumActivation(TortOLMInterneuronGate):
    name = "Tort O-LM Interneuron Sodium activation"

    def alpha(self, V):
        denom = np.exp(-(V + 38) / 10) - 1
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 1

        return -0.1 * (V + 38) / denom

    def beta(self, V):
        return 4 * np.exp(-(V + 65) / 18)
