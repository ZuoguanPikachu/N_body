import numpy
from PIL import Image, ImageDraw
import os


G = 6.673*1e-11
dt = 0.001*3600
k = 304195000

sub_stepping = 24000

pos = numpy.array([
    [0, 0],
    [152097701000, 0]
], dtype=numpy.float64)

vel = numpy.array([
    [0, 0],
    [0, 107218]
], dtype=numpy.float64)
vel *= 5/18


force = numpy.array([
    [0, 0],
    [0, 0]
], dtype=numpy.float64)

m = numpy.array([1.989*1e30, 5.9724*1e24], dtype=numpy.float64)

def compute_force():
    for i in range(2):
        force[i] = numpy.array([0, 0], dtype=numpy.float64)

    for i in range(2):
        p = pos[i]
        for j in range(i):
            diff = p-pos[j]
            r = numpy.linalg.norm(diff)

            f = -G * m[i] * m[j] * (1.0/r)**3 * diff

            force[i] += f
            force[j] += -f


def update():
    for i in range(2):
        vel[i] += dt*force[i]/m[i]
        pos[i] += dt*vel[i]


def render(t):
    r = 5

    img = Image.new("RGB", (1920, 1080), (17, 47, 65))

    painter = ImageDraw.Draw(img)
    painter.ellipse([(455, 35), (1465, 1045)], outline="red", width=10)
    for i in range(2):
        pos_ = numpy.array([1, -1], dtype=numpy.float64)*pos[i]/k + numpy.array([960, 540], dtype=numpy.float64)
        p1 = pos_ - r
        p2 = pos_ + r

        painter.ellipse([tuple(p1.tolist()), tuple(p2.tolist())], fill="white")

    img.save(f"renders/{t}.jpg")


if __name__ == '__main__':
    os.mkdir("renders")

    t = 0
    while t < 4395:
        for i in range(sub_stepping):
            compute_force()
            update()

        render(t)
        t += 1
