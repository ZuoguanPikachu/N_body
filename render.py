from PIL import Image, ImageDraw
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
