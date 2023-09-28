from PIL import Image
import numpy as np
from matplotlib.image import imread


def list_to_image(image_as_list, original_shape, path_to_save):
    image = np.array(image_as_list)
    image = image.reshape(original_shape)
    print(image.shape)
    new_img = Image.fromarray(image, "RGB")
    new_img.show()
    new_img.save(path_to_save + ".jpeg")


def image_to_list(image_path):
    img = imread(image_path)
    reshaped_image = img.reshape((-1))
    reshaped_image = reshaped_image.tolist()
    return reshaped_image, img.shape
