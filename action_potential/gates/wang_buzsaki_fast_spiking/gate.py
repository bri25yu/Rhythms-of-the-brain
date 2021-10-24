from action_potential.gates.gate import Gate


class WangBuzsakiFastSpikingGate(Gate):
    name = None
    time_constant_multiplier = 1.0

    def steady_state(self, V):
        alpha = self.alpha(V)
        beta = self.beta(V)

        return alpha / (alpha + beta)

    def time_constant(self, V):
        alpha = self.alpha(V)
        beta = self.beta(V)

        return self.time_constant_multiplier / (alpha + beta)
