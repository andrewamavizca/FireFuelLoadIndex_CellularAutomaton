import numpy as np

def fli_calc(image, a=0.6, b=0.2, c=0.1, d=0.1):
    FLI = (a * image['ndvi'] + b * image['ndmi'] + c * (1 - image['nbr']) + d * (1 - image['cwc']))
    return (FLI - np.min(FLI)) / (np.max(FLI) - np.min(FLI))

def fire_spread_simulation(fuel_map, num_ignition_points=1, steps=100, spread_prob=0.6, wind_factor=1.2):
    fire_grid = np.zeros_like(fuel_map)
    ignition_points = np.column_stack((np.random.randint(0, fuel_map.shape[0], num_ignition_points),
                                       np.random.randint(0, fuel_map.shape[1], num_ignition_points)))
    for point in ignition_points:
        fire_grid[tuple(point)] = 1
    
    fire_sequence = [fire_grid.copy()]
    
    for _ in range(steps):
        new_fire_grid = fire_grid.copy()
        for i in range(1, fuel_map.shape[0] - 1):
            for j in range(1, fuel_map.shape[1] - 1):
                if fire_grid[i, j] == 1:
                    new_fire_grid[i, j] = 2
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if fire_grid[i + x, j + y] == 0:
                            if np.random.rand() < spread_prob * fuel_map[i + x, j + y] * wind_factor:
                                new_fire_grid[i + x, j + y] = 1
        fire_grid = new_fire_grid.copy()
        fire_sequence.append(fire_grid.copy())
    
    return fire_sequence
