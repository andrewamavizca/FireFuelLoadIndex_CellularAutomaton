import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fire_simulation.preprocessing import split_into_patches, get_image_features
from fire_simulation.simulation import fli_calc, fire_spread_simulation
from fire_simulation.visualization import animate_fire_spread
from matplotlib import pyplot as plt
# Load data
date = '11_06_18'
image = np.load(f'data/{date}-center-fire.npy')
patches = split_into_patches(image, patch_size=128)
patch = get_image_features(patches[28])

# Compute FLI
FLI = fli_calc(patch)

# Simulate Fire Spread
fire_sequence = fire_spread_simulation(FLI, num_ignition_points=2, steps=100)

# Visualize
animate_fire_spread(patch['rgb'], FLI, fire_sequence, steps=100)

