from action_potential.approximations.approximation import Approximation

from action_potential.action_potentials.current_modulated import CurrentModulatedActionPotential


class TortOLMInterneuronCurrentModulatedActionPotential(CurrentModulatedActionPotential):
    name = "Tort O-LM Interneuron Current Modulated Action potential"

    g_Na = 30.0
    g_K = 23.0
    g_L = 0.05
    g_A = 16.0
    g_h = 12.0
    E_Na = 90.0
    E_K = -100.0
    E_L = -70.0
    E_A = -90.0
    E_h = -32.9

    C = 1.3

    def __init__(
        self,
        sodium_activation,
        sodium_inactivation,
        potassium_activation,
        a_activation,
        b_activation,
        r_activation,
        input_current,
    ):
        self.a_activation = a_activation
        self.b_activation = b_activation
        self.r_activation = r_activation

        super().__init__(sodium_activation, sodium_inactivation, potassium_activation, input_current)

    def f(self, x, t):
        self._update_state(x, t)

        g_Na = self.g_Na * (self.m ** 3) * self.h
        g_K = self.g_K * (self.n ** 4)
        g_L = self.g_L
        g_A = self.g_A * self.a * self.b
        g_h = self.g_h * self.r

        I_current = self.input_current.F(t)

        return (
            - g_Na * (x - self.E_Na)\
            - g_K * (x - self.E_K)\
            - g_L * (x - self.E_L)\
            - g_A * (x - self.E_A)\
            - g_h * (x - self.E_h)\
            + I_current
        ) / self.C

    def set_V_0(self, V_0):
        self.m = self.sodium_activation.steady_state(V_0)
        self.h = self.sodium_inactivation.steady_state(V_0)
        self.n = self.potassium_activation.steady_state(V_0)
        self.a = self.a_activation.steady_state(V_0)
        self.b = self.b_activation.steady_state(V_0)
        self.r = self.r_activation.steady_state(V_0)
    
    def _update_state(self, x, t):
        phi = self._hodgkin_huxley_temperature_constant()

        self.m = self._hodgkin_huxley_update_state(self.sodium_activation, self.m, phi, x)
        self.h = self._hodgkin_huxley_update_state(self.sodium_inactivation, self.h, phi, x)
        self.n = self._hodgkin_huxley_update_state(self.potassium_activation, self.n, phi, x)
        self.a = self._tort_o_lm_update_state(self.a_activation, self.a, phi, x)
        self.b = self._tort_o_lm_update_state(self.b_activation, self.b, phi, x)
        self.r = self._tort_o_lm_update_state(self.r_activation, self.r, phi, x)

    @staticmethod
    def _tort_o_lm_update_state(activation, state, phi, V):
        dx = (activation.steady_state(V) - state) / activation.time_constant(V)
        return state + dx * phi * Approximation.EPS
