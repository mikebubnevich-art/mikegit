import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter=100):
    z = 0j
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z * z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    result = np.zeros((height, width), dtype=int)
    
    for i, re in enumerate(y):
        for j, im in enumerate(x):
            result[i, j] = mandelbrot(complex(im, re), max_iter)
    return result


result = mandelbrot_set(-2.0, 0.5, -1.25, 1.25, 800, 600, 100)


plt.figure(figsize=(10, 8))
plt.imshow(result,  extent=(-2.0, 0.5, -1.25, 1.25))
plt.axis('off')


plt.savefig('mandelbrot_fractal.png', dpi=300, bbox_inches='tight', pad_inches=0)



plt.show()