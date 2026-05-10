import cv2
import os
import time
import sys
from PIL import Image
CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,^".'


def draw(br):
    index = int((br / 255) * (len(CHARS) - 1))
    return CHARS[index]


capture = cv2.VideoCapture("---") # Enter your video name instead of "---", video must be in the same folder as this script.
if os.name == 'nt':
    os.system('')

while True:
    ret, frame = capture.read()
    if not ret:
        break

    cc = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    picture = Image.fromarray(cc).convert("L")

    wt = 100
    h = int(wt * picture.height // picture.width // 2)
    picture = picture.resize((wt, h))

    frameBfr = ""
    for y in range(h):
        for x in range(wt):
            b = picture.getpixel((x, y))
            frameBfr += draw(b)
        frameBfr += "\n"

    sys.stdout.write("\033[H")
    sys.stdout.write(frameBfr)
    sys.stdout.flush()

    time.sleep(0.02)
capture.release()
input("Любая клаваша чтобы выйти")
