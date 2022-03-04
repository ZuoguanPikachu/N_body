from PIL import Image, ImageDraw
from n_body.record import load
from utils.progress_bar import progress_bar
import numpy
import os


def render_one(stars, t, k, bg_size=(1920, 1080), bg_color=(17, 47, 65), dir_="renders"):
    try:
        os.mkdir(dir_)
    except FileExistsError:
        pass

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

    img.save(f"{dir_}/{t}.jpg")


def render_series(filename, k, bg_size=(1920, 1080), bg_color=(17, 47, 65, 255), dir_="renders"):
    try:
        os.mkdir(dir_)
    except FileExistsError:
        pass

    data = load(filename)

    stars = data["stars"]
    n = len(stars)
    T = len(data["pos"])

    mask = Image.new("RGBA", bg_size, (17, 47, 65, 64))
    img = Image.new("RGBA", bg_size, bg_color)
    for t in progress_bar(T, "Rendering"):
        img = Image.alpha_composite(img, mask)

        painter = ImageDraw.Draw(img)

        for i in range(n):
            pos = data["pos"][t-1][i]
            r = stars[i]["r"]
            color = stars[i]["color"]

            pos_ = numpy.array([1, -1], dtype=numpy.float64)*pos/k + numpy.array(bg_size, dtype=numpy.float64)/2
            p1 = pos_ - r
            p2 = pos_ + r

            painter.ellipse([tuple(p1.tolist()), tuple(p2.tolist())], fill=color)

        img.save(f"{dir_}/{t-1}.png")
