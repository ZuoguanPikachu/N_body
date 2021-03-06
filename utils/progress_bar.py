import time


class progress_bar:
    def __init__(self, I, description="Running"):
        self.I = I
        self.description = description
        self.i = 0
        self.time0 = time.time()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        bar = "{:<41}".format("="*(int(self.i*40/self.I)+1))

        time_ = time.time()
        delta_time = int(time_-self.time0)
        if self.i == 0:
            total_time = 0
        else:
            total_time = int(delta_time*self.I/self.i)

        if total_time == 0:
            total_time_formatted = "00:00:00"
            delta_time_formatted = "00:00:00"
        else:
            m, s = divmod(total_time, 60)
            h, m = divmod(m, 60)
            total_time_formatted = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)

            m, s = divmod(delta_time, 60)
            h, m = divmod(m, 60)
            delta_time_formatted = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)

        print("\r", end="")
        if self.i == self.I:
            print(f"{self.description}......  {bar} {int(self.i*100/self.I)}%|100%    {delta_time_formatted}|{total_time_formatted}\n")
        else:
            print(f"{self.description}......  {bar} {int(self.i*100/self.I)}%|100%    {delta_time_formatted}|{total_time_formatted}", end="", flush=True)

        if self.i < self.I:
            self.i += 1
            return self.i
        else:
            raise StopIteration()
        