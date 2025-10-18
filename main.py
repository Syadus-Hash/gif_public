import imageio.v3 as iio

path_index = None
filenames = [path_index + 'pic_1.png',path_index + 'pic_2.png',path_index + 'pic_3.png',path_index + 'pic_4.png' ] # path
images = []
for filename in filenames:
    images.append(iio.imread(filename)) # imread loads an image based on the file path
iio.imwrite('cat.gif', images, duration = 75, loop = 0)
