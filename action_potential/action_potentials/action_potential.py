import numpy as np

from action_potential.functions.function import Function
from action_potential.approximations.approximation import Approximation


class ActionPotential(Function):
    name = "Action potential"

    # These numbers default to the Hodkin-Huxley model
    x_0 = -65.0

    g_Na = 120.0
    g_K = 36.0
    g_L = 0.3
    E_Na = 50.0
    E_K = -77.0
    E_L = -54.4

    Q_10 = 3.0
    T_base = 6.3
    T = 7.3

    C = 1.0

    def __init__(self, sodium_activation, sodium_inactivation, potassium_activation):
        self.sodium_activation = sodium_activation
        self.sodium_inactivation = sodium_inactivation
        self.potassium_activation = potassium_activation

        self.reset()

    def f(self, x, t):
        self._update_state(x, t)

        g_Na = self.g_Na * (self.m ** 3) * self.h
        g_K = self.g_K * (self.n ** 4)
        g_L = self.g_L

        return (-g_Na * (x - self.E_Na) - g_K * (x - self.E_K) - g_L * (x - self.E_L)) / self.C

    def set_V_0(self, V_0):
        self.m = self.sodium_activation.steady_state(V_0)
        self.h = self.sodium_inactivation.steady_state(V_0)
        self.n = self.potassium_activation.steady_state(V_0)

    def reset(self):
        self.set_V_0(self.x_0)

    def _update_state(self, x, t):
        phi = self._hodgkin_huxley_temperature_constant()

        self.m = self._hodgkin_huxley_update_state(self.sodium_activation, self.m, phi, x)
        self.h = self._hodgkin_huxley_update_state(self.sodium_inactivation, self.h, phi, x)
        self.n = self._hodgkin_huxley_update_state(self.potassium_activation, self.n, phi, x)

    @staticmethod
    def _hodgkin_huxley_update_state(activation, state, phi, V):
        alpha, beta = activation.alpha(V), activation.beta(V)
        dx = alpha * (1 - state) - beta * state
        return state + dx * phi * Approximation.EPS

    def _hodgkin_huxley_temperature_constant(self):
        return self.Q_10 ** ((self.T - self.T_base) / 10)
