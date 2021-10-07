class Function:
    name = None
    x_0 = None

    @staticmethod
    def f(x, t):
        raise NotImplementedError()

    @staticmethod
    def F(t):
        raise NotImplementedError()

    @staticmethod
    def dfdt(x, t):
        raise NotImplementedError()
