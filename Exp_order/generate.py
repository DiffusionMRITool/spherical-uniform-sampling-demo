import os
from os.path import join

src = "../HCP_Q3_grad"
dst = "../HCP_ordered"
# change this to path of direction_order.py
# exec_path = "/path/to/direction_order.py"
exec_path = "~/project/src/qspace_direction/direction_order.py"

os.system(
    f"python {exec_path} {join(src, 'grad.txt')} {join(src, 'bval.txt')} -o {join(dst, 'milp1.txt')} -n 1 -v"
)
