import os
from os.path import join, exists

src = "../ElectricRepulsion"
dst = "../ElectricRepulsion_MILPSC"
# change this to path of direction_flip.py
exec_path = "/path/to/direction_flip.py"

for i in range(10, 260, 10):
    f = "Elec{:0>3}.txt".format(i)
    if exists(join(dst, f)):
        continue
    os.system(
        f"python {exec_path} --input {join(src, f)} --output {join(dst, f)} -c DISTANCE"
    )
