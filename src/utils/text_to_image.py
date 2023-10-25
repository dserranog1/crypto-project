from PIL import Image
import numpy as np
from matplotlib.image import imread


def list_to_image(image_as_list, original_shape, path_to_save):
    image = np.array(image_as_list)
    image = image.reshape(original_shape)
    new_img = Image.fromarray(image.astype(np.uint8))
    new_img.show()
    new_img.save(path_to_save + ".jpeg")


def image_to_list(image_path):
    img = Image.open(image_path)
    array_img = np.array(img)
    original_shape = array_img.shape
    return array_img.reshape(-1), original_shape
