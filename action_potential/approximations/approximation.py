from action_potential.functions.function import Function


class Approximation:
    name = None
    EPS = 1e-3

    @staticmethod
    def approximate(f: Function, t):
        raise NotImplementedError()
