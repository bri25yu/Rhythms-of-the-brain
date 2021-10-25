import numpy as np

from action_potential.gates.tort_o_lm_interneuron.gate import TortOLMInterneuronGate


class TortOLMInterneuronPotassiumActivation(TortOLMInterneuronGate):
    name = "Tort O-LM Interneuron Potassium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V - 25) / 25)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 0.1

        return 0.018 * (V - 25) / denom

    def beta(self, V):
        denom = np.exp((V - 35) / 12) - 1
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 0.1

        return 0.036 * (V - 35) / denom
