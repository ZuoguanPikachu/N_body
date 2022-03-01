from render import render_one
from star import Star
from compute import compute
from rich.progress import track
import os

if __name__ == "__main__":
    sub_stepping = 16000

    stars = [
        Star(m=1.989*1e30, pos=[0, 0], vel=[0, 0], r=24, color="red"),
        Star(m=3.3*1e23, pos=[7*1e10, 0], vel=[0, 47890], r=6, color="white"),
        Star(m=4.87*1e24, pos=[1.085*1e11, 0], vel=[0, 35000], r=6, color="yellow"),
        Star(m=5.972*1e24, pos=[1.521*1e11, 0], vel=[0, 29783], r=12, color="blue")
    ]

    os.mkdir("renders")

    for t in track(range(4400), description="Rendering..."):
        for i in range(sub_stepping):
            stars = compute(stars)

        render_one(stars, t, 3.04*1e8)

    print("")
    os.system("ffmpeg -f image2 -i renders/%d.jpg -r 60  m.mp4")
