import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """ft_invert"""
    try:
        assert isinstance(array, np.ndarray), "array must be a np.ndarray"
        return 255 - array
    except Exception as e:
        print("Exception: ", e)
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """ft_red"""
    try:
        assert isinstance(array, np.ndarray), "array must be a np.ndarray"
        return array * [1, 0, 0]
    except Exception as e:
        print("Exception: ", e)
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """ft_green"""
    try:
        assert isinstance(array, np.ndarray), "array must be a np.ndarray"
        return np.array([[[0, i[1], 0] for i in row]
                        for row in array]).astype(np.uint8)
    except Exception as e:
        print("Exception: ", e)
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """ft_blue"""
    try:
        assert isinstance(array, np.ndarray), "array must be a np.ndarray"
        return np.array([[[0, 0, i[2]] for i in row]
                        for row in array]).astype(np.uint8)
    except Exception as e:
        print("Exception: ", e)
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """ft_grey"""
    try:
        assert isinstance(array, np.ndarray), "array must be a np.ndarray"
        return np.array([[[np.mean(i), np.mean(i), np.mean(i)] for i in row]
                        for row in array]).astype(np.uint8)

    except Exception as e:
        print("Exception: ", e)
        return None
