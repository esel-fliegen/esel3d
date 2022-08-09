# esel3d

[Esel-3D](https://pypi.org/project/esel-3d/0.2/) is an interactive playground to visualize math in three spatial dimensions.
It is a 3D plotter for curves, surfaces, shapes and more. The redering uses [BabylonJS](https://www.babylonjs.com/) 
game engine to produce vibrant visuals and provides intuitive controls right inside a Jupyter Notebook or
Google Colab cell. 

### Install

```html
#in the first Colab cell
!pip install esel3d

```

### Example Usage

```python
from esel3d import plot3d
import numpy as np

#define boundary condition and plot resolution
x_initial = -2
x_final = 2
y_initial = -1
y_final = 1

resolution = 0.1

#define function
def func(x, y):
  return -np.power(x, 2)

#create instance and plot.
#instance creation and plot must be in the same cell. 

plt3d = plot3d()
plt3d.surface(func, [xinitial, xfinal], [yinitial, yfinal], resolution)
plt3d.plot()

```

## Navigate

Explore and view the plot from all angles in 3D space.
![Fig:1](https://raw.githubusercontent.com/esel-fliegen/esel3d/main/img/esel3d_img1.png)

## Configurable

Add custom labels. Change the color scheme of the axis. Chose the background color which is the most appealing. Plot up to 3 sufaces. 
![Fig:2](https://raw.githubusercontent.com/esel-fliegen/esel3d/main/img/esel3d_img2.png)
![Fig:5](https://raw.githubusercontent.com/esel-fliegen/esel3d/main/img/esel3d_img5.png)
![Fig:3](https://raw.githubusercontent.com/esel-fliegen/esel3d/main/img/esel3d_img3.png)

## Inspect

With the point explorer gizmo, users can view point location. 

![Fig:4](https://raw.githubusercontent.com/esel-fliegen/esel3d/main/img/esel3d_img4.png)
 
## Tutorials and Examples

Tuts and examples will be provided in the form of YouTube videos with accompanying example notebooks. 

[Demo-Notebook](https://colab.research.google.com/gist/esel-fliegen/e56b29d1814ffaf839854f775c229cd6/esel3d_beta-demo-colab.ipynb)

## TODO
- [ ] Add configs for Jupyter Notebook compatibility
- [ ] Add animation option
- [ ] Make 3D cylindrical grid
- [ ] Make 3D polar grid
- [ ] Make vector field plot