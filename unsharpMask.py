from skimage.filters import gaussian
from skimage.filters import unsharp_mask
from skimage import io, img_as_float
from matplotlib import pyplot as plt


mask_multiplicator = 4.0


#original image
img = img_as_float(
    io.imread('./images_in/image_in.jpg', as_gray=True))
# gaussian img
gaussian_img = gaussian(img, sigma=1, mode='reflect')
# blurred_img
blurred_img = (img - gaussian_img) * mask_multiplicator
# unsharp mask
unsharp_img = img + blurred_img


f = plt.figure(figsize=(30, 30))

# show original image
f.add_subplot(5, 5, 1)
plt.imshow(img, cmap='gray')
plt.title('Original image')

# show  gaussian image
f.add_subplot(5, 5, 2)
plt.imshow(gaussian_img, cmap='gray')
plt.title('Gaussian image')

# show  blurred image
f.add_subplot(5, 5, 3)
plt.imshow(blurred_img, cmap='gray')
plt.title('blurred image')


# show sharpening image
f.add_subplot(5, 5, 4)
plt.imshow(unsharp_img, cmap='gray')

f.add_subplot(5, 5, 5)
io.imshow(unsharp_img)

plt.title('Unsharp mask')

plt.show()


# export the image to images_out folder
io.imsave('./images_out/image_out_unsharp.jpg', unsharp_img)