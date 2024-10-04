from matplotlib import pyplot as plt
import numpy as np
from os.path import join


def read_bvec(filename, start=0):
    with open(filename, "r") as f:
        lines = f.readlines()
        p = [list(map(float, l.split())) for l in lines[start:]]
    return np.array(p)


def covering_radius(vects):
    if len(vects) < 2:
        return 0
    vects = np.array(vects)
    innerProductAll = np.abs(vects @ vects.T)
    return (
        np.arccos((np.clip(np.max(np.triu(innerProductAll, 1)), -1, 1))) * 180 / np.pi
    )


def stats(folder, x, f, start=0):
    res = {"quater": [], "half": [], "three-quater": []}
    for i in x:
        filename = "Elec{:0>3}.txt".format(i)
        vects = read_bvec(join(folder, filename), start)
        res["quater"].append(f(vects[: i // 4]))
        res["half"].append(f(vects[: i // 2]))
        res["three-quater"].append(f(vects[: 3 * i // 4]))

    return res


origin = "../ElectricRepulsion"
MILP_O_S = "../ElectricRepulsion_MILPOS"
dirorder = "../ElectricRepulsion_dirorder"
camino = "../ElectricRepulsion_camino"

x = np.arange(10, 260, 10)
y_label = lambda name: {
    "quater": f"{name} of a quater of points",
    "half": f"{name} of a half of points",
    "three-quater": f"{name} of three quater of points",
}


MILP_O_S_stats = stats(MILP_O_S, x, covering_radius)
camino_stats = stats(camino, x, covering_radius, 1)
dirorder_stats = stats(dirorder, x, covering_radius, 1)
for k in ["quater", "half", "three-quater"]:
    plt.cla()
    plt.scatter(
        x, MILP_O_S_stats[k], c="none", edgecolors="b", marker="o", label="MILP-O-S"
    )
    plt.scatter(
        x,
        dirorder_stats[k],
        c="none",
        edgecolors="r",
        marker="^",
        label="dirorder",
    )
    plt.scatter(
        x, camino_stats[k], c="none", edgecolors="y", marker="s", label="camino"
    )

    fontsize = 20
    plt.xlabel("Size of subset K", fontsize=fontsize)
    plt.ylabel(y_label("SC")[k], fontsize=fontsize)
    plt.legend(fontsize=13, markerscale=1.3)
    plt.tight_layout()
    plt.savefig(f"fig/{k}_SC.svg")
