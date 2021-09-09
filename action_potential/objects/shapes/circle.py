from objects.abstract import AbstractObject, plt


class Circle(AbstractObject):
    class Attr(AbstractObject.Attr):
        r = "r"

    def __init__(self, config: dict):
        super().__init__(config)

        self.r = self.config[self.Attr.r]

    def draw(self, ax):
        self.o = plt.Circle((self.x, self.y), self.r, color=self.color)
        ax.add_patch(self.o)
    
    def update(self, config: dict):
        super().update(config)

        self.o.center = (self.x, self.y)
        self.o.set_radius(self.r)
        self.o.set_color(self.color)
