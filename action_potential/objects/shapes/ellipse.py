import matplotlib.patches as patches

from objects.abstract import AbstractObject, np


class Ellipse(AbstractObject):
    class Attr(AbstractObject.Attr):
        w = "w"
        h = "h"
        angle = "angle"

    class DEFAULT(AbstractObject.DEFAULT):
        angle = 0  # in radians

    def __init__(self, config: dict):
        super().__init__(config)

        self.w = self.config[self.Attr.w]
        self.h = self.config[self.Attr.h]
        self.angle = self.config.get(self.Attr.angle, self.DEFAULT.angle)

    def draw(self, ax):
        self.o = patches.Ellipse(
            (self.x, self.y),
            self.w,
            self.h,
            angle=np.degrees(self.angle),
            color=self.color,
        )
        ax.add_patch(self.o)

    def update(self, config: dict):
        super().update(config)

        self.o.center = (self.x, self.y)
        self.o.set_width(self.w)
        self.o.set_height(self.h)
        self.o.set_angle(np.degrees(self.angle))
        self.o.set_color(self.color)
