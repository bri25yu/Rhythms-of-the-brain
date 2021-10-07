from action_potential.functions.function import Function


class BaseInputCurrent(Function):
    name = "Input current"
    x_0 = 0

    def F(t):
        return 0.0
