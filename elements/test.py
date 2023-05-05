# from pathlib import Path

# BASE_DIR = Path(__file__).parent

# image_path = BASE_DIR / 'sampleFile.jpeg'

# print(image_path)
# print(f"Type: {type(image_path)}")

# print(str(image_path))
# print(f"Type 2: {type(str(image_path))}")


import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0

    assert 'division by zero' in str(e.value)
