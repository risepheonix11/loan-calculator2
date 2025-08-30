import turtle as t
from random import random

for i in range(20):
    steps = int(random()*100)
    angle = int(random()*360)
    t.right(angle)
    t.fd(steps)



