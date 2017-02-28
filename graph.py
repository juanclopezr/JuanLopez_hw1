import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('atpos.dat')

print(data.shape)
plt.imshow(data,cmap='jet')
#plt.set_cmap('nipy_spectral')
plt.savefig('graph.pdf', format='pdf')
