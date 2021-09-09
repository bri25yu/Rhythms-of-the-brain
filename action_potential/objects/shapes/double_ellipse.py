from objects.abstract import np
from objects.abstract import AbstractObject
from objects.shapes.ellipse import Ellipse


class DoubleEllipse(Ellipse):
    class Attr(Ellipse.Attr):
        space = "space"

    def __init__(self, config: dict):
        super().__init__(config)

        self.space = self.config[self.Attr.space] / 2

    def draw(self, ax):
        self.e1 = self._create_ellipse(*self._get_left_ellipse_params())
        self.e2 = self._create_ellipse(*self._get_right_ellipse_params())

        self.e1.draw(ax)
        self.e2.draw(ax)

    def update(self, config: dict):
        AbstractObject.update(self, config)

        self._update_ellipse_params(
            self.e1,
            *self._get_left_ellipse_params(),
        )
        self._update_ellipse_params(
            self.e2,
            *self._get_right_ellipse_params(),
        )

    def _create_ellipse(self, x, y):
        config = {
            **self.config,
            self.Attr.x: x,
            self.Attr.y: y,
        }
        return Ellipse(config)

    def _get_left_ellipse_params(self):
        x1 = self.x + self.space * np.cos(self.angle)
        y1 = self.y + self.space * np.sin(self.angle)
        return x1, y1

    def _get_right_ellipse_params(self):
        x2 = self.x - self.space * np.cos(self.angle)
        y2 = self.y - self.space * np.sin(self.angle)
        return x2, y2

    def _update_ellipse_params(self, o, x, y):
        config = {
            **self.config,
            o.Attr.x: x,
            o.Attr.y: y,
        }
        o.update(config)
