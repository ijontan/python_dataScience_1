from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(file: np.ndarray, new_shape: tuple) -> np.ndarray:
    """ft_zoom"""
    try:
        (start_x, start_y, width, height) = new_shape
        (old_height, old_width, _) = file.shape
        assert file is not None, "file is None"
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
        return None


def ft_rotate(file: np.ndarray, angle: int) -> np.ndarray:
    """ft_rotate"""
    possible_rotations = [0, 90, 180, 270]
    try:
        assert angle in possible_rotations, "angle must be 0, 90, 180 or 270"
        if angle == 0:
            return file
        elif angle == 90 or angle == -270:
            return np.transpose(file, axes=(1, 0, 2))[::-1]
        elif angle == 180 or angle == -180:
            return file[::-1, ::-1]
        elif angle == 270 or angle == -90:
            return np.transpose(file, axes=(1, 0, 2))[:, ::-1]
    except Exception as e:
        print("Exception: ", e)
        return None


def main():
    """main"""
    try:
        file = ft_load("animal.jpeg")
        if file is None:
            return
        zoomed = ft_zoom(file, (450, 100, 400, 400))
        if zoomed is None:
            return
        print("Shape of image is :", zoomed.shape)
        print(zoomed)
        rotated = ft_rotate(zoomed, 90)
        if rotated is None:
            return
        print("Shape after rotate is :", rotated.shape)
        print(rotated)
        plt.imshow(rotated)
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt..")


if __name__ == "__main__":
    main()
