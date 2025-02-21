import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import tkinter
matplotlib.use('TkAgg') 

def animate_fire_spread(rgb_image, FLI, fire_sequence, steps=100):
    fig, ax = plt.subplots(1, 3, figsize=(14, 7), dpi=150)

    ax[0].imshow(rgb_image)
    ax[0].set_title('RGB Image Reference')
    ax[0].axis('off')

    ax[1].imshow(FLI, cmap='OrRd')
    ax[1].set_title('Fuel Load Index')
    ax[1].axis('off')

    ax[2].imshow(FLI, cmap='OrRd', alpha=0.6)
    fire_im = ax[2].imshow(fire_sequence[0], cmap='hot', vmin=0, vmax=2, alpha=0.7)
    ax[2].set_title('Fire Spread Simulation')
    ax[2].axis('off')

    def update(frame):
        fire_im.set_array(fire_sequence[frame])
        ax[2].set_title(f'Fire Spread Step {frame}')
        return [fire_im]
    global anim
    anim = animation.FuncAnimation(fig, update, frames=steps, interval=200, blit=False)
    # anim.save('fire_spread_simulation.gif', writer='imagemagick', fps=60)
    plt.show()
    
