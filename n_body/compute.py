import numpy


G = 6.673*1e-11


def update(stars, dt):
    n = len(stars)

    for i in range(n):
        stars[i].force = numpy.array([0, 0], dtype=numpy.float64)

    for i in range(n):
        star1 = stars[i]
        p1 = star1.pos
        m1 = star1.m

        for j in range(i):
            star2 = stars[j]
            p2 = star2.pos
            m2 = star2.m

            diff = p1 - p2
            d = numpy.linalg.norm(diff)

            f = -G * m1 * m2 * (1.0/d)**3 * diff

            star1.force += f
            star2.force += -f


    for i in range(n):
        star = stars[i]
        star.vel += dt*star.force/star.m
        star.pos += dt*star.vel

    return stars
