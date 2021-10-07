from action_potential.currents.base_input_current import BaseInputCurrent


class SustainedInputCurrent(BaseInputCurrent):
    name = "Sustained input current"

    def F(t):
        if 20.0 < t < 80.0:
            return 10.0  # mV
        return 0.0
