import numpy as np

from action_potential.gates.hodgkin_huxley.gate import HodgkinHuxleyGate


class OlufsenPyramidalPotassiumActivation(HodgkinHuxleyGate):
    name = "Olufsen Pyramidal Potassium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 52) / 5)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 0.1

        return 0.032 * (V + 52) / denom

    def beta(self, V):
        return 0.5 * np.exp(-(V + 57) / 40)
