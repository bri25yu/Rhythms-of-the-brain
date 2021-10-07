import numpy as np

from action_potential.functions.function import Function
from action_potential.approximations.approximation import Approximation


class Taylor2Approximation(Approximation):
    name = "Taylor2"

    @staticmethod
    def approximate(f: Function, t):
        EPS = Taylor2Approximation.EPS

        x = np.zeros(t.shape)
        x[0] = f.x_0
        for i in range(1, len(t)):
            zero_order = x[i - 1]
            first_order = EPS * f.f(x[i - 1], t[i - 1])
            second_order = (1 / 2) * (EPS ** 2) * f.dfdt(x[i - 1], t[i - 1])
            x[i] = zero_order + first_order + second_order
        return x
