import numpy as np

from action_potential.gates.wang_buzsaki_fast_spiking.gate import WangBuzsakiFastSpikingGate


class WangBuzsakiFastSpikingSodiumActivation(WangBuzsakiFastSpikingGate):
    name = "Wang-Buzsaki fast-spiking Sodium activation"

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 35) / 10)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 1

        return 0.1 * (V + 35) / denom

    def beta(self, V):
        return 4 * np.exp(-(V + 60) / 18)
