class Gate:
    name = None

    def steady_state(self, V):
        alpha = self.alpha(V)
        beta = self.beta(V)

        return alpha / (alpha + beta)

    def time_constant(self, V):
        alpha = self.alpha(V)
        beta = self.beta(V)

        return 1 / (alpha + beta)

    def alpha(self, V):
        raise NotImplementedError()

    def beta(self, V):
        raise NotImplementedError()
