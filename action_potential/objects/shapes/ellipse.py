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
        e = patches.Ellipse(
            (self.x, self.y),
            self.w,
            self.h,
            angle=np.degrees(self.angle),
            color=self.color,
        )
        ax.add_patch(e)
