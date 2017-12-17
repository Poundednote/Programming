import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.array([[0, 0 , 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')
np.random.choice([0, 255], 4 * 4, p=[0.1, 0.9]).reshape(4, 4)
plt.show()
