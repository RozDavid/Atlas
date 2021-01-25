import numpy as np
import trimesh

# load a file by name or from a buffer
mesh = trimesh.load_mesh('results/release/semseg/test_final/sample1.ply')

print(mesh.moment_inertia)

mesh.show()