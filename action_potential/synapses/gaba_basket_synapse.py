from action_potential.synapses.synapse import Synapse


class GABABasketSynapse(Synapse):
    tau_R = 0.3
    tau_D = 9.0
    V_rev = -80.0
