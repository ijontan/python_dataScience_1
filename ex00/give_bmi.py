import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi"""
    try:
        types = (int, float)
        h_array = np.array(height)
        w_array = np.array(weight)

        assert h_array.dtype in types, "type of height must be int or float"
        assert w_array.dtype in types, "type of weight must be int or float"
        assert h_array.size == w_array.size, "both list must be same size"
        return (w_array / (h_array / 100) ** 2).tolist()
    except Exception as e:
        raise e


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit"""
    try:
        types = (int, float)
        bmi_array = np.array(bmi)

        assert bmi_array.dtype in types, "type of bmi must be int or float"
        assert isinstance(limit, int), "type of limit must be int"
        return (bmi_array >= limit).tolist()
    except Exception as e:
        raise e
