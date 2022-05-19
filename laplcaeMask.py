from skimage.filters import gaussian
from skimage.filters import laplace
from skimage import io, img_as_float
from matplotlib import pyplot as plt

ksize = 5

img = img_as_float(
    io.imread('./images_in/image_in.jpg', as_gray=True))

mask = gaussian(img, sigma=1, mode='reflect')

laplace_img = laplace(img, ksize, mask)


f = plt.figure(figsize=(30, 30))

# show original image
f.add_subplot(5, 5, 1)
plt.imshow(img, cmap='gray')
plt.title('Original image')

# show  gaussian image
f.add_subplot(5, 5, 2)
plt.imshow(mask, cmap='gray')
plt.title('Gaussian image')

# show  lapace image
f.add_subplot(5, 5, 3)
plt.imshow(laplace_img, cmap='gray')
f.add_subplot(5, 5, 4)
io.imshow(laplace_img)

plt.title('Laplace image')

plt.show()

io.imsave('./images_out/image_out_laplace.jpg', laplace_img)
