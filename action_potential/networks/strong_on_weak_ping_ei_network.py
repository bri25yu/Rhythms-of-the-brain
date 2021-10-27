import numpy as np

from action_potential.networks.weak_ping_ei_network import WeakPingEINetwork


class StrongOnWeakPingBackgroundEINetwork(WeakPingEINetwork):
    name = "Strong PING on Weak PING background E-I network"

    def _deterministic_E_input_current(self):
        input_current = super()._deterministic_E_input_current()
        additional_input_current = np.zeros((self.NUM_E,))
        additional_input_current[:20] = 3.25
        return input_current + additional_input_current
