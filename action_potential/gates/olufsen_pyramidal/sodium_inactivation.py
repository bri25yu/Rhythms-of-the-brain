import numpy as np

from action_potential.gates.hodgkin_huxley.gate import HodgkinHuxleyGate


class OlufsenPyramidalSodiumInactivation(HodgkinHuxleyGate):
    name = "Olufsen Pyramidal Sodium inactivation"

    def alpha(self, V):
        return 0.128 * np.exp(-(V + 50) / 18)

    def beta(self, V):
        return 4 / (1 + np.exp(-(V + 27) / 5))
