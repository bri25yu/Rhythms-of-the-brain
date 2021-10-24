import numpy as np

from action_potential.gates.hodgkin_huxley.gate import HodgkinHuxleyGate


class OlufsenPyramidalSodiumActivation(HodgkinHuxleyGate):
    name = "Olufsen Pyramidal Sodium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 54) / 4)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 1

        return 0.32 * (V + 54) / denom

    def beta(self, V):
        denom = np.exp((V + 27) / 5) - 1
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 1

        return 0.28 * (V + 27) / denom
