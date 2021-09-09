from objects.abstract import np
from objects.shapes.ellipse import Ellipse


class DoubleEllipse(Ellipse):
    class Attr(Ellipse.Attr):
        space = "space"

    def __init__(self, config: dict):
        super().__init__(config)

        self.space = self.config[self.Attr.space] / 2

    def draw(self, ax):
        x1 = self.x + self.space * np.cos(self.angle)
        y1 = self.y + self.space * np.sin(self.angle)
        e1 = self._create_ellipse(x1, y1)

        x2 = self.x - self.space * np.cos(self.angle)
        y2 = self.y - self.space * np.sin(self.angle)
        e2 = self._create_ellipse(x2, y2)

        e1.draw(ax)
        e2.draw(ax)

    def _create_ellipse(self, x, y):
        config = {
            **self.config,
            self.Attr.x: x,
            self.Attr.y: y,
        }
        return Ellipse(config)
