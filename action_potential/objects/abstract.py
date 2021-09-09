import matplotlib.pyplot as plt


class AbstractObject:
    class Attr:
        x = "x"
        y = "y"
        layer = "layer"
        color = "color"

    class DEFAULT:
        layer = 0
        color = "r"

    def __init__(self, config: dict):
        self.config = config

        self.x = self.config[self.Attr.x]
        self.y = self.config[self.Attr.y]
        self.layer = self.config.get(self.Attr.layer, self.DEFAULT.layer)
        self.color = self.config.get(self.Attr.color, self.DEFAULT.color)

    def draw(self, ax):
        raise NotImplementedError()

    def update(self, config: dict):
        self.__init__(config)
