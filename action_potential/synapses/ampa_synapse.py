from action_potential.synapses.synapse import Synapse


class AMPASynapse(Synapse):
    tau_R = 0.1
    tau_D = 3.0
    V_rev = 0.0
