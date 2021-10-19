import numpy as np

from action_potential.gates.hodgkin_huxley_gate import HodgkinHuxleyGate


class HodgkinHuxleySodiumActivation(HodgkinHuxleyGate):
    name = "Sodium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 40) / 10)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 1

        return 0.1 * (V + 40) / denom

    def beta(self, V):
        return 4 * np.exp(-(V + 65) / 18)
