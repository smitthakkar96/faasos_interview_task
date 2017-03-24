""" Generate a sample of large log FILE """

import random

from constants import SAMPLE_LOG


FILE = open('sample.log', "w+")

for i in range(9999 * random.randint(0, 10)):
    FILE.write(SAMPLE_LOG+"\n")

FILE.close()
