from n_body.star import Star
from n_body.compute import update
from n_body.render import render_series
from n_body.record import Recorder, load
from utils.progress_bar import progress_bar
import os


if __name__ == "__main__":
    dt = 0.0005*3600
    sub_stepping = 16000

    stars = [
        Star(m=1.989*1e30, pos=[0, 0], vel=[0, 0], r=24, color="red"),
        Star(m=3.3*1e23, pos=[7*1e10, 0], vel=[0, 47890], r=6, color="white"),
        Star(m=4.87*1e24, pos=[1.085*1e11, 0], vel=[0, 35000], r=6, color="yellow"),
        Star(m=5.972*1e24, pos=[1.521*1e11, 0], vel=[0, 29783], r=12, color="blue")
    ]

    recoder = Recorder(stars)

    for t in progress_bar(100):
        for i in range(sub_stepping):
            stars = update(stars, dt)

        recoder.add(stars)

    recoder.save("data.pk")

    render_series(filename="data.pk", k=3.04*1e8)
    os.system("ffmpeg -f image2 -i renders/%d.png -r 60 m.mp4")
