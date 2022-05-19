from skimage import data, exposure, img_as_float, io
from matplotlib import pyplot as plt

img = img_as_float(
    io.imread('./images_in/image_in.jpg', as_gray=True))

gamma = 10
gain = 1


gamma_corection = exposure.adjust_gamma(img, gamma=gamma, gain=gain)


f = plt.figure(figsize=(30, 30))

# show original image
f.add_subplot(5, 5, 1)
plt.imshow(img, cmap='gray')
plt.title('Original image')

# show  gaussian image
f.add_subplot(5, 5, 2)
plt.imshow(gamma_corection, cmap='gray')

plt.title('gama corection')

plt.show()

io.imsave(
    './images_out/image_out_exposure.jpg', laplace_img)
