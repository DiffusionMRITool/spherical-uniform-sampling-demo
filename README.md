This code is used for reproduce paper image.

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
(Note: you need to change `exec_path = "/path/to/direction_flip.py"` to your corresponding script path, e.g. `"~/dmritool-sampling/src/qspace_sampling/direction_flip.py"` if you clone the repo in the home directory)

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
(Note: you also need to change `exec_path = "/path/to/direction_order.py"` to your corresponding script path)

3. Draw picture
```bash
python draw.py
```