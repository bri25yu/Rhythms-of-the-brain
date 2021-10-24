from action_potential.action_potentials.current_modulated import CurrentModulatedActionPotential


class WangBuzsakiFastSpikingCurrentModulatedActionPotential(CurrentModulatedActionPotential):
    x_0 = -65.0

    g_Na = 35.0
    g_K = 9.0
    g_L = 0.1
    E_Na = 55.0
    E_K = -90.0
    E_L = -65.0
