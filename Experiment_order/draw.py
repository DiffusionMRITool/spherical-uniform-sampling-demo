from matplotlib import pyplot as plt
import numpy as np


def read_bvec_bval(bvec_file, bval_file, start=0):
    with open(bvec_file, "r") as f:
        lines = f.readlines()
        bvec = [list(map(float, l.split())) for l in lines[start:]]
    with open(bval_file, "r") as f:
        lines = f.readlines()
        bval = [int(l) for l in lines[start:]]
    return bvec, bval


def covering_radius(vects):
    if len(vects) < 2:
        return 0
    vects = np.array(vects)
    innerProductAll = vects @ vects.T
    return (
        np.arccos((np.clip(np.max(np.triu(innerProductAll, 1)), -1, 1))) * 180 / np.pi
    )


def stats(bvecs, bvals):
    bvalsSet = set(bvals)
    # bval=0 stands for combined shell
    bvalsSet.add(0)
    d = {bval: [] for bval in bvalsSet}
    res = {bval: [0] for bval in bvalsSet}

    for val, vec in zip(bvals, bvecs):
        d[val].append(vec)
        d[0].append(vec)

        for v in bvalsSet:
            res[v].append(covering_radius(d[v]))

    return {k: np.array(v) for k, v in res.items()}


milp_bval = "../HCP_ordered/milp_bval.txt"
milp_bvec = "../HCP_ordered/milp_bvec.txt"
camino_bval = "../HCP_ordered/camino_bval.txt"
camino_bvec = "../HCP_ordered/camino_bvec.txt"
mrtrix_bval = "../HCP_ordered/mrtrix_bval.txt"
mrtrix_bvec = "../HCP_ordered/mrtrix_bvec.txt"

milp_stats = stats(*read_bvec_bval(milp_bvec, milp_bval))
camino_stats = stats(*read_bvec_bval(camino_bvec, camino_bval))
mrtrix_stats = stats(*read_bvec_bval(mrtrix_bvec, mrtrix_bval))

x = np.arange(0, 275, 5)
for val in milp_stats.keys():
    plt.cla()
    plt.scatter(
        x, milp_stats[val][x], c="none", edgecolors="b", marker="o", label="MILP-O-M"
    )
    plt.scatter(
        x, camino_stats[val][x], c="none", edgecolors="y", marker="s", label="camino"
    )
    plt.scatter(
        x, mrtrix_stats[val][x], c="none", edgecolors="r", marker="D", label="Mrtrix"
    )

    fontsize = 20
    plt.xlabel("Size of subset K", fontsize=fontsize)
    plt.ylabel("Covering Radius", fontsize=fontsize)
    plt.legend(fontsize=13, markerscale=1.3)
    plt.tight_layout()
    plt.savefig(f"fig/{val if val else 'combined'}.svg")
