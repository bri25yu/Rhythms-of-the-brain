from action_potential.currents.base_input_current import BaseInputCurrent


class BlipInputCurrent(BaseInputCurrent):
    name = "Blip input current"

    def F(t):
        if 20.0 < t < 22.0:
            return 10.0  # mV
        return 0.0
