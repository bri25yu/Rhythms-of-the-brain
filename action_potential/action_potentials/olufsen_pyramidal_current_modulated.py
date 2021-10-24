from action_potential.action_potentials.current_modulated import CurrentModulatedActionPotential


class OlufsenPyramidalCurrentModulatedActionPotential(CurrentModulatedActionPotential):
    x_0 = -65.0

    g_Na = 100.0
    g_K = 80.0
    g_L = 0.1
    E_Na = 50.0
    E_K = -100.0
    E_L = -67.0
