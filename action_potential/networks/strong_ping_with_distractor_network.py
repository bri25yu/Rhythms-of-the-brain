import numpy as np

from action_potential.networks.strong_ping_ei_network import StrongPingEINetwork


class StrongPingWithDistractorEINetwork(StrongPingEINetwork):
    name = "Strong PING with distractor E-I network"

    def __init__(self):
        super().__init__()

        self.t = 0

    def _deterministic_E_input_current(self):
        hz40 = 4 * (np.sin(40 * np.pi * self.t / 1000)) ** 8
        hz56 = 4 * (np.sin(56 * np.pi * self.t / 1000)) ** 8
        self.t += 1
        return hz40 + hz56
