This code is used to reproduce images in our paper.

You need to to first install the `spherical_uniform_sampling` package to use this.

### Single shell flipping 

1. Move to working directory
```bash
cd Experiment_flip
```

2. (Optional) Generate flipped files.
There are already polarity optimized files in `ElectricRepulsion_dirflip` (optimized by `dirflip`), `ElectricRepulsion_MILPEEM` (optimized by `MILP-P-S(EEM)`) and `ElectricRepulsion_MILPSC` (optimized by `MILP-P-S(SC)`)

You can run corresponding generation script to generate by yourself.

For example, for polarity optimization result by method MILP-P-S(EEM), you should run
```bash
python generate_MILPEEM.py
```

3. Draw picture
```bash
python draw.py
```

### Single shell ordering

1. Move to working directory
```bash
cd Experiment_order_single
```

2. (Optional) Generate order optimized files.
There are already order optimized files in `ElectricRepulsion_dirorder` (optimized by `dirorder`), `ElectricRepulsion_MILPOS` (optimized by `MILP-O-S`) and `ElectricRepulsion_camino` (optimized by `orderpoints`)

You can run corresponding generation script to generate by yourself.

For example, for order optimization result by method MILP-O-S, you should run
```bash
python generate_MILP.py
```

3. Draw picture
```bash
python draw.py
```

### Multiple shell ordering

1. Move to working directory
```bash
cd Experiment_order_multi
```

2. (Optional) Generate order optimized files.
There are already order optimized files in `HCP_ordered`

You can run corresponding generation script to generate by yourself.

For example, for order optimization by method MILP-O-M, you should run
```bash
python generate.py
```

3. Draw picture
```bash
python draw.py
```