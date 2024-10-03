import os
from os.path import join

src = "../HCP_Q3_grad"
dst = "../HCP_ordered"

os.system(
    f"direction_order.py {join(src, 'grad.txt')} {join(src, 'bval.txt')} -o {join(dst, 'milp1.txt')} -s 1"
)
