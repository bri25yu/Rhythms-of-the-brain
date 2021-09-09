from objects.abstract import AbstractObject, plt


class Circle(AbstractObject):
    class Attr(AbstractObject.Attr):
        r = "r"

    def __init__(self, config: dict):
        super().__init__(config)

        self.r = self.config[self.Attr.r]

    def draw(self, ax):
        c = plt.Circle((self.x, self.y), self.r, color=self.color)
        ax.add_patch(c)
