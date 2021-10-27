from action_potential.action_potentials.current_modulated import CurrentModulatedActionPotential


class WangBuzsakiFastSpikingCurrentModulatedActionPotential(CurrentModulatedActionPotential):
    x_0 = -65.0

    g_Na = 35.0
    g_K = 9.0
    g_L = 0.1
    E_Na = 55.0
    E_K = -90.0
    E_L = -65.0

    def _update_state(self, x, t):
        self.m = self.sodium_activation.steady_state(x)
        self.h = self._hodgkin_huxley_update_state(self.sodium_inactivation, self.h, 1.0, x)
        self.n = self._hodgkin_huxley_update_state(self.potassium_activation, self.n, 1.0, x)
