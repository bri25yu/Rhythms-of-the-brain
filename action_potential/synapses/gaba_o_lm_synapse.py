from action_potential.synapses.synapse import Synapse


class GABAOLMSynapse(Synapse):
    tau_R = 0.2
    tau_D = 20.0
    V_rev = -80.0
