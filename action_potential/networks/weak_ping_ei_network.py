import numpy as np

from action_potential.synapses import GABABasketSynapse
from action_potential.networks.strong_ping_ei_network import StrongPingEINetwork


class WeakPingEINetwork(StrongPingEINetwork):
    name = "Weak PING E-I network"

    g_stoch_E = 0.1
    tau_D_stoch_E = 3.0
    f_stoch_E = 20.0

    def _deterministic_E_input_current(self):
        return 1.25
