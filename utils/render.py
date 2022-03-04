from operator import le
from PIL import Image, ImageDraw
from record import load
import numpy


def render_one(stars, t, k, bg_size=(1920, 1080), bg_color=(17, 47, 65)):
    img = Image.new("RGB", bg_size, bg_color)
    painter = ImageDraw.Draw(img)

    n = len(stars)
    for i in range(n):
        pos = stars[i].pos
        r = stars[i].r
        color = stars[i].color

        pos_ = numpy.array([1, -1], dtype=numpy.float64)*pos/k + numpy.array(bg_size, dtype=numpy.float64)/2
        p1 = pos_ - r
        p2 = pos_ + r

        painter.ellipse([tuple(p1.tolist()), tuple(p2.tolist())], fill=color)

    img.save(f"renders/{t}.jpg")


def render_series(k, bg_size=(1920, 1080), bg_color=(17, 47, 65, 255)):
    data = load("data.pk")

    stars = data["stars"]
    n = len(stars)
    T = len(data["pos"])

    mask = Image.new("RGBA", bg_size, (17, 47, 65, 64))
    img = Image.new("RGBA", bg_size, bg_color)
    for t in range(T):
        img = Image.alpha_composite(img, mask)

        painter = ImageDraw.Draw(img)

        for i in range(n):
            pos = data["pos"][t][i]
            r = stars[i].r
            color = stars[i].color

            pos_ = numpy.array([1, -1], dtype=numpy.float64)*pos/k + numpy.array(bg_size, dtype=numpy.float64)/2
            p1 = pos_ - r
            p2 = pos_ + r

            painter.ellipse([tuple(p1.tolist()), tuple(p2.tolist())], fill=color)

        img.save(f"renders/{t}.png")
