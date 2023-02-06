from pippen.core.structures.frame import Frame
import pytest

class TestGetSet:
    @pytest.mark.parametrize(
        "data",
        [
            (
                [
                    ["James", "Holden", "1234 Galactic Ave", "Europa"],
                    ["John", "Stockton", "1234 Rodeo Dr", "USA"],
                    ["Patrick", "Star", "1234 Bikini Bottom", "Pacific Ocean"]
                ]
            )
        ]
    )
    def test_set_data(self, data):
        frame = Frame()
        frame.set_data(data)
        assert frame.data == data

