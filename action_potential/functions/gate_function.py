import numpy as np

from action_potential.functions.function import Function


class GateFunction(Function):
    name = None

    def __init__(self, V_i, V_f, gate):
        super().__init__()

        self.gate = gate
        self.name = self.gate.name

        self.m_0 = self.gate.steady_state(V_i)
        self.m_inf = self.gate.steady_state(V_f)
        self.tau = self.gate.time_constant(V_f)

        self.x_0 = self.m_0

    def f(self, x, t):
        return (self.m_inf - x) / self.tau

    def F(self, t):
        return self.m_inf + (self.m_0 - self.m_inf) * np.exp(-t / self.tau)
