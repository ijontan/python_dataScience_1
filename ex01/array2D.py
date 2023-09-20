import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me"""
    try:
        assert isinstance(family, list), "family must be a list"
        f_arr = np.array(family)
        assert f_arr.ndim == 2, "family must be a 2D list"
        assert isinstance(start, int), "start must be an integer"
        assert isinstance(end, int), "end must be an integer"

        oldShape = f_arr.shape
        print("My Shape is :", oldShape)
        new_f_arr = f_arr[start:end]
        newShape = new_f_arr.shape
        print("My new Shape is :", newShape)

        return new_f_arr.tolist()
    except Exception as e:
        print("Exception: ", e)
