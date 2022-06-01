from multiprocessing import Pipe
import numpy as np
a, b = Pipe()
data = np.random.normal(size=(10, 1))
a.send(data)
print(b.recv())