import pickle
import copy
import sys


class Recorder:
    def __init__(self, stars):
        self.stars = stars
        self.n = len(stars)
        self.pos = []
        
        self.add(self.stars)
    
    def add(self, stars):
        pos_t = []
        for i in range(self.n):
            star_i = copy.deepcopy(stars[i])
            pos_t.append(star_i.pos)

        self.pos.append(pos_t)
    
    def save(self, filename):
        stars_render_info = []
        for star in self.stars:
            stars_render_info.append({"color": star.color, "r": star.r})

        with open(filename, "wb") as f:
            data = {
                "stars": stars_render_info,
                "pos": self.pos
            }

            pickle.dump(data, f)
            f.close()


def load(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
        f.close()
    
    return data
