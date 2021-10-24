from action_potential.action_potentials.action_potential import ActionPotential


class CurrentModulatedActionPotential(ActionPotential):
    name = "Current Modulated Action potential"

    def __init__(
        self,
        sodium_activation,
        sodium_inactivation,
        potassium_activation,
        input_current,
    ):
        super().__init__(sodium_activation, sodium_inactivation, potassium_activation)

        self.input_current = input_current

    def f(self, x, t):
        dxdt = super().f(x, t)

        I_current = self.input_current.F(t)

        return dxdt + (I_current / self.C)

    def set_input_current(self, input_current):
        self.input_current = input_current
