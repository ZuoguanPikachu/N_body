import pickle
import copy


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
        with open(filename, "wb") as f:
            data = {
                "stars": self.stars,
                "pos": self.pos
            }

            pickle.dump(data, f)
            f.close()


def load(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
        f.close()
    
    return data
