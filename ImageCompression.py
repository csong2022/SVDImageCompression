import matplotlib.pyplot as plt
import numpy as np
import time

from PIL import Image

img = Image.open('wp1892090.png')
# imggray = img.convert('LA')
plt.figure(figsize=(9, 6))
plt.imshow(imggray)
imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.asmatrix(imgmat)
plt.figure(figsize=(9,6))
plt.imshow(imgmat, cmap='gray')

U, sigma, V = np.linalg.svd(imgmat)

reconstimg = np.asmatrix(U[:, :1]) * np.diag(sigma[:1]) * np.asmatrix(V[:1, :])
plt.imshow(reconstimg, cmap='gray')

for i in range(5, 51, 5):
    reconstimg = np.asmatrix(U[:, :i]) * np.diag(sigma[:i]) * np.asmatrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()