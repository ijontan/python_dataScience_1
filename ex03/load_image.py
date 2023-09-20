import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """ft_load"""
    try:
        assert isinstance(path, str), "path must be a string"
        img = Image.open(path)
        img_arr = np.array(img)
        print("The shape of image is :", img_arr.shape)
        return img_arr
    except Exception as e:
        print("Exception: ", e)
        return None
