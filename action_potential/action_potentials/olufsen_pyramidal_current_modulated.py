from action_potential.action_potentials.current_modulated import CurrentModulatedActionPotential


class OlufsenPyramidalCurrentModulatedActionPotential(CurrentModulatedActionPotential):
    x_0 = -65.0

    g_Na = 100.0
    g_K = 80.0
    g_L = 0.1
    E_Na = 50.0
    E_K = -100.0
    E_L = -67.0

    def _update_state(self, x, t):
        self.m = self.sodium_activation.steady_state(x)
        self.h = self._hodgkin_huxley_update_state(self.sodium_inactivation, self.h, 1.0, x)
        self.n = self._hodgkin_huxley_update_state(self.potassium_activation, self.n, 1.0, x)
