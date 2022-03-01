import numpy


class Star:
    def __init__(self, m, pos, vel, r=5, color="white"):
        self.m = m
        self.pos = numpy.array(pos, dtype=numpy.float64)
        self.vel = numpy.array(vel, dtype=numpy.float64)
        self.r = r
        self.color = color
        self.force = numpy.array([0, 0], dtype=numpy.float64)