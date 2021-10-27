import numpy as np

from action_potential.networks.strong_ping_with_distractor_network import StrongPingWithDistractorEINetwork


class WeakPingWithDistractorEINetwork(StrongPingWithDistractorEINetwork):
    name = "Weak PING with distractor E-I network"

    g_IE = 0.0
