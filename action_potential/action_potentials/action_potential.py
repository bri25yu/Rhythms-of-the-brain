import numpy as np

from action_potential.functions.function import Function
from action_potential.approximations.approximation import Approximation


class ActionPotential(Function):
    name = "Action potential"
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

    def __init__(self, sodium_activation, sodium_inactivation, potassium_activation):
        self.sodium_activation = sodium_activation
        self.sodium_inactivation = sodium_inactivation
        self.potassium_activation = potassium_activation
        
        self.reset()

    def f(self, x, t):
        alpha_m, beta_m = self.sodium_activation.alpha(x), self.sodium_activation.beta(x)
        alpha_h, beta_h = self.sodium_inactivation.alpha(x), self.sodium_inactivation.beta(x)
        alpha_n, beta_n = self.potassium_activation.alpha(x), self.potassium_activation.beta(x)
        
        dm = alpha_m * (1 - self.m) - beta_m * self.m
        dh = alpha_h * (1 - self.h) - beta_h * self.h
        dn = alpha_n * (1 - self.n) - beta_n * self.n
        
        phi = self.Q_10 ** ((self.T - self.T_base) / 10)

        self.m = self.m + dm * phi * Approximation.EPS
        self.h = self.h + dh * phi * Approximation.EPS
        self.n = self.n + dn * phi * Approximation.EPS
        
        g_Na = self.g_Na * (self.m ** 3) * self.h
        g_K = self.g_K * (self.n ** 4)
        g_L = self.g_L
        
        return -g_Na * (x - self.E_Na) - g_K * (x - self.E_K) - g_L * (x - self.E_L)
    
    def set_V_0(self, V_0):
        self.m = self.sodium_activation.steady_state(V_0)
        self.h = self.sodium_inactivation.steady_state(V_0)
        self.n = self.potassium_activation.steady_state(V_0)
        
    def reset(self):
        self.set_V_0(self.x_0)
