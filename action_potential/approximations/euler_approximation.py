import numpy as np

from action_potential.functions.function import Function
from action_potential.approximations.approximation import Approximation


class EulerApproximation(Approximation):
    name = "Euler's"

    @staticmethod
    def approximate(f: Function, t):
        x = np.zeros(t.shape)
        x[0] = f.x_0
        for i in range(1, len(t)):
            x[i] = x[i-1] + EulerApproximation.EPS * f.f(x[i-1], t[i-1])
        return x
