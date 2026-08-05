import math

print(math.sqrt(9))
print(math.ceil(4.2))
print("=" * 20)

from math import sqrt, ceil

print(sqrt(9))


# ================================================
import random

print(random.randint(1, 10))
print(random.choice(["정상", "경고", "위험"]))


print("================================")


import datetime

now = datetime.datetime.now()
print(now)

dir(math)
help(math.sqrt)

import os

current_working_directory = os.getcwd()
print(current_working_directory)

file_list = os.listdir()
for file_name in file_list:
    print(file_name)
