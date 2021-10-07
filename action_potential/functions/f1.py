import numpy as np

from action_potential.functions.function import Function


class F1(Function):
    name = r"$F(t) = e^t$"
    x_0 = 1

    @staticmethod
    def f(x, t):
        return x

    @staticmethod
    def F(t):
        return np.exp(t)

    @staticmethod
    def dfdt(x, t):
        return 0
