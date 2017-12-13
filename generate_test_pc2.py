import struct
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def gaussian_2d(x_coord, y_coord, x_0, y_0, sigma_x, sigma_y, amplitude):
    return amplitude * np.exp(- (np.power((x_coord - x_0), 2) / (2 * np.power(sigma_x, 2)) +
                                  np.power((y_coord - y_0), 2) / (2 * np.power(sigma_y, 2))))


x_vals = np.linspace(-1, 1, 10)
y_vals = np.linspace(-1, 1, 10)
print(x_vals, y_vals)
# x_vals, y_vals = np.meshgrid(x_vals, y_vals)
# fig = plt.figure()
# ax = fig.gca(projection='3d')

# print(x.shape)
# print(y.shape)
# z = gaussian_2d(x, y, 0, 0, 1, 1, 1)
# print(z.shape)



# for t in range(10):
#     z = gaussian_2d(x, y, 0, 0, 1, 1, t)
#     ax.plot_surface(x, y, z, rstride=3, cstride=3, linewidth=1, antialiased=True,
#                    cmap=cm.viridis)
    # plt.contourf(x, y, z)
    # plt.colorbar()
# plt.show()


vertCount = len(x_vals)*len(y_vals)
start = 1
sampling = 1
sampleCount = 250


with open('test_gaussian_pc2.pc2', 'wb') as f:

    headerFormat = '<12siiffi'
    headerStr = struct.pack(headerFormat, b'POINTCACHE2\0',
                            1, vertCount, start, sampling, sampleCount)
    f.write(headerStr)

    a = np.linspace(1, 10, sampleCount)
    i = 0
    for s in range(sampleCount):
        for y_i in y_vals:
            for x_i in x_vals:
                # z_val = a[s]
                z_val = gaussian_2d(x_i, y_i, 0, 0, 1, 1, a[s])
                print(x_i, y_i, z_val)
                print(i)
                i += 1
                thisVertex = struct.pack('<fff', float(x_i), float(z_val), float(y_i))
                f.write(thisVertex)
