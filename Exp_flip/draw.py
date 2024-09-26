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
    innerProductAll = vects @ vects.T
    return (
        np.arccos((np.clip(np.max(np.triu(innerProductAll, 1)), -1, 1))) * 180 / np.pi
    )


def norm_of_mean(vects: np.ndarray):
    mean = vects.mean(axis=0)
    return np.linalg.norm(mean)


def electrostatic_energy(points: np.ndarray, order=2):
    l = len(points)
    eij = lambda i, j: 1 / (np.linalg.norm(points[i] - points[j]) ** order)

    s = 0
    for i in range(1, l):
        for j in range(i):
            s += eij(i, j)

    return s / (l * (l - 1) / 2)


def stats(folder, x, start=0):
    res = {"SC": [], "EEM": [], "NormOfMean": []}
    for i in x:
        filename = "Elec{:0>3}.txt".format(i)
        vects = read_bvec(join(folder, filename), start)
        res["EEM"].append(electrostatic_energy(vects))
        res["NormOfMean"].append(norm_of_mean(vects))
        res["SC"].append(covering_radius(vects))

    return res


origin = "../ElectricRepulsion"
MILP_EEM = "../ElectricRepulsion_MILPEEM"
MILP_SC = "../ElectricRepulsion_MILPSC"
dirflip = "../ElectricRepulsion_dirflip"

x = np.arange(10, 260, 10)
origin_stats = stats(origin, x)
MILP_EEM_stats = stats(MILP_EEM, x)
MILP_SC_stats = stats(MILP_SC, x)
dirflip_stats = stats(dirflip, x, 1)
y_label = {
    "SC": "Covering Radius (degree)",
    "EEM": "Electrastic Energy (order = 2)",
    "NormOfMean": "Norm of Mean Direction Vector",
}

for k in origin_stats.keys():
    plt.cla()
    plt.scatter(
        x, origin_stats[k], c="none", edgecolors="b", marker="o", label="origin"
    )
    plt.scatter(
        x, MILP_SC_stats[k], c="r", edgecolors="r", marker="^", label="MILP-P-S(SC)"
    )
    plt.scatter(
        x,
        MILP_EEM_stats[k],
        c="none",
        edgecolors="r",
        marker="^",
        label="MILP-P-S(EEM)",
    )
    plt.scatter(
        x, dirflip_stats[k], c="none", edgecolors="y", marker="s", label="dirflip"
    )

    fontsize = 20
    plt.xlabel("Size of subset K", fontsize=fontsize)
    plt.ylabel(y_label[k], fontsize=fontsize)
    plt.legend(fontsize=13, markerscale=1.3)
    plt.tight_layout()
    plt.savefig(f"fig/{k}.svg")
