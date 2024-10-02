This code is used for reproduce paper image.

You need to to first install the `qspace_direction` package to use this.

### Single shell flipping (Fig. 2)

1. Move to working directory
```bash
cd Exp_flip
```

2. (Optional) Generate flipped files.
There are already flipped files in `ElectricRepulsion_*`

You can run corresponding generation script to generate by yourself.

For example, for flipped result by method MILP-P-S(EEM), you should run
```bash
python generate_MILPEEM.py
```

3. Draw picture
```bash
python draw.py
```

### Multiple shell ordering (Fig. 3)

1. Move to working directory
```bash
cd Exp_order
```

2. (Optional) Generate flipped files.
There are already flipped files in `HCP_ordered`

You can run corresponding generation script to generate by yourself.

For example, for ordered result by method MILP-O-M, you should run
```bash
python generate.py
```

3. Draw picture
```bash
python draw.py
```