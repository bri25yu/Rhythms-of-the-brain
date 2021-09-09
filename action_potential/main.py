import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    from objects.shapes.circle import Circle

    c = Circle({
        Circle.Attr.x: 1,
        Circle.Attr.y: 2,
        Circle.Attr.r: 0.5,
        Circle.Attr.color: "blue",
    })
    c.draw(ax)

    plt.savefig("temp.png")
    plt.close()


if __name__ == "__main__":
    main()
