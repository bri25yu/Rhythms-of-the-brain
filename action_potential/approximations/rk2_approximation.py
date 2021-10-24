import numpy as np

from action_potential.functions.function import Function
from action_potential.approximations.approximation import Approximation


class RK2Approximation(Approximation):
    name = "RK2"

    @staticmethod
    def approximate(f: Function, t):
        EPS = RK2Approximation.EPS

        x = np.zeros(t.shape)
        x[0] = f.x_0
        for i in range(1, len(t)):
            k1 = f.f(x[i - 1], t[i - 1])
            k2 = f.f(x[i - 1] + (EPS / 2), t[i - 1] + EPS * (k1 / 2))
            x[i] = x[i - 1] + EPS * (1 / 2) * (k1 + k2)
            if i % 100 == 0: print(f"Finished {i} / {len(t)}\r", end="", flush=True)
        print()
        return x
