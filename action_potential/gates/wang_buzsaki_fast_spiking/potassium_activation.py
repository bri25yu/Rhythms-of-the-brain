import numpy as np

from action_potential.gates.wang_buzsaki_fast_spiking.gate import WangBuzsakiFastSpikingGate


class WangBuzsakiFastSpikingPotassiumActivation(WangBuzsakiFastSpikingGate):
    name = "Wang-Buzsaki fast-spiking Potassium activation"
    time_constant_multiplier = 0.2

    def alpha(self, V):
        denom = 1 - np.exp(-(V + 34) / 10)
        if not isinstance(denom, np.ndarray) and np.isclose(denom, 0):
            return 0.1

        return 0.01 * (V + 34) / denom

    def beta(self, V):
        return 0.125 * np.exp(-(V + 44) / 80)
