import numpy as np

from action_potential.synapses import GABABasketSynapse
from action_potential.networks.small_e_i_network import SmallEINetwork


class StrongPingEINetwork(SmallEINetwork):
    name = "Strong PING E-I network"
    g_II = 0.5

    def __init__(self):
        super().__init__(fast=True)

    def _init_ei_ie_synapses_fast(self):
        super()._init_ei_ie_synapses_fast()

        ii_g = np.random.binomial(1, self.P_II, size=(self.NUM_I, self.NUM_I))
        ii_g = ii_g * self.g_II / (self.P_II * self.NUM_I)
        i_synapse = GABABasketSynapse(ii_g, self.i_neurons, self.i_neurons)
        self.i_neurons.add_synapses((i_synapse,))
