from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(file: np.ndarray, new_shape: tuple) -> np.ndarray:
    """ft_zoom"""
    try:
        (start_x, start_y, width, height) = new_shape
        (old_height, old_width, _) = file.shape
        assert isinstance(new_shape, tuple), "new_shape must be a tuple"
        assert len(new_shape) == 4, "new_shape must be a 4-tuple"
        assert np.array(new_shape).dtype == np.int64, "new_shape only int"
        assert all([i >= 0 for i in new_shape]), "new_shape must be positive"
        assert start_x + width <= old_width, "old_width exceeded"
        assert start_y + height <= old_height, "old_height exceeded"
        new_file = file[start_y:start_y + height, start_x:start_x + width]
        return new_file
    except Exception as e:
        print("Exception: ", e)


def main():
    """main"""
    try:
        file = ft_load("animal.jpeg")
        print(file)
        zoomed = ft_zoom(file, (450, 100, 400, 400))
        print("New shape after slicing :", zoomed.shape)
        print(zoomed)
        plt.imshow(zoomed)
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt..")


if __name__ == "__main__":
    main()
