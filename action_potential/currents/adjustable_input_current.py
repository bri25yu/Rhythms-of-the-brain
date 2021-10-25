from action_potential.currents.base_input_current import BaseInputCurrent


class AdjustableInputCurrent(BaseInputCurrent):
    name = "Adjustable input current"

    def __init__(self, input_current=0.0):
        self.input_current = input_current

    def F(self, t):
        return self.input_current

    def set_input_current(self, input_current):
        self.input_current = input_current
