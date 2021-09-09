import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    from objects.shapes.ellipse import Ellipse

    c = Ellipse({
        Ellipse.Attr.x: 1,
        Ellipse.Attr.y: 2,
        Ellipse.Attr.w: 3,
        Ellipse.Attr.h: 5,
        Ellipse.Attr.angle: np.pi / 4,
        Ellipse.Attr.color: "green",
    })
    c.draw(ax)

    plt.savefig("temp.png")
    plt.close()


if __name__ == "__main__":
    main()
