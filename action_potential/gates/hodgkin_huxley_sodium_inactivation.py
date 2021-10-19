import numpy as np

from action_potential.gates.hodgkin_huxley_gate import HodgkinHuxleyGate


class HodgkinHuxleySodiumInactivation(HodgkinHuxleyGate):
    name = "Sodium inactivation"

    def alpha(self, V):
        return 0.07 * np.exp(-(V + 65) / 20)

    def beta(self, V):
        return 1 / (1 + np.exp(-(V + 35) / 10))
