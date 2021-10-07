import numpy as np

from action_potential.functions.function import Function


class F2(Function):
    name = r"$F(t) = \sin(t)$"
    x_0 = 0

    @staticmethod
    def f(x, t):
        return np.cos(t)

    @staticmethod
    def F(t):
        return np.sin(t)

    @staticmethod
    def dfdt(x, t):
        return -np.sin(t)
