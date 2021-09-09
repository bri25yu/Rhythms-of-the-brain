import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np


SAVE_PATH = "temp.gif"

def main():
    fig, ax = setup_plot()
    o = setup_object_to_draw()

    def init():
        o.draw(ax)
        return o,

    def animate(i):
        o.update({
            o.Attr.x: o.x + 0.1,
        })
        return o,

    anim = FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=10,
        interval=200,
    )

    anim.save(SAVE_PATH)


def setup_plot():
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    return fig, ax


def setup_object_to_draw():
    from objects.shapes.circle import Circle
    from objects.shapes.ellipse import Ellipse
    from objects.shapes.double_ellipse import DoubleEllipse
    cls = DoubleEllipse

    c = cls({
        cls.Attr.x: 1,
        cls.Attr.y: 2,
        # cls.Attr.r: 3,
        cls.Attr.w: 1,
        cls.Attr.h: 5,
        cls.Attr.angle: np.pi / 4,
        cls.Attr.space: 2,
        cls.Attr.color: "blue",
    })

    return c


if __name__ == "__main__":
    main()
