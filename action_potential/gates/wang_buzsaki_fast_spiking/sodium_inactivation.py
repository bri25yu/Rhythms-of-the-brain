import numpy as np

from action_potential.gates.wang_buzsaki_fast_spiking.gate import WangBuzsakiFastSpikingGate


class WangBuzsakiFastSpikingSodiumInactivation(WangBuzsakiFastSpikingGate):
    name = "Wang-Buzsaki fast-spiking Sodium inactivation"
    time_constant_multiplier = 0.2

    def alpha(self, V):
        return 0.07 * np.exp(-(V + 58) / 20)

    def beta(self, V):
        return 1 / (1 + np.exp(-(V + 28) / 10))
