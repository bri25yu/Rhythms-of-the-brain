import numpy as np

from action_potential.gates.gate import Gate


class PotassiumActivation(Gate):
    name = "Potassium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 55) / 10)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 0.1

        return 0.01 * (V + 55) / denom

    def beta(self, V):
        return 0.125 * np.exp(-(V + 65) / 80)
