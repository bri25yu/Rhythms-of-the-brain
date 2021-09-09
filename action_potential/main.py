import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    from objects.shapes.double_ellipse import DoubleEllipse

    c = DoubleEllipse({
        DoubleEllipse.Attr.x: 1,
        DoubleEllipse.Attr.y: 2,
        DoubleEllipse.Attr.w: 1,
        DoubleEllipse.Attr.h: 5,
        DoubleEllipse.Attr.angle: np.pi / 4,
        DoubleEllipse.Attr.space: 2,
        DoubleEllipse.Attr.color: "blue",
    })
    c.draw(ax)

    plt.savefig("temp.png")
    plt.close()


if __name__ == "__main__":
    main()
