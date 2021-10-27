import numpy as np

from action_potential.networks.strong_on_weak_ping_ei_network import StrongOnWeakPingBackgroundEINetwork


class AsyncISuppressesENetwork(StrongOnWeakPingBackgroundEINetwork):
    name = "Asynchronous I-cells suppresses E-cells network"

    g_EI = 0.0
    g_II = 0.0

    g_stoch_I = 0.5
    tau_D_stoch_I = 1.0
    f_stoch_I = 38.0
