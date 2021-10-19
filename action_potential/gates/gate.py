class Gate:
    name = None

    def steady_state(self, V):
        raise NotImplementedError()

    def time_constant(self, V):
        raise NotImplementedError()

    def alpha(self, V):
        raise NotImplementedError()

    def beta(self, V):
        raise NotImplementedError()
