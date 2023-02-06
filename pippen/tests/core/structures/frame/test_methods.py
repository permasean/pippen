from pippen.core.structures.frame import Frame
import pytest

class TestMethods:
    @pytest.mark.parametrize(
        "header, data, expected",
        [
            (
                ["first_name", "last_name", "street_address", "country"],
                [
                    ["James", "Holden", "1234 Galactic Ave", "Europa"],
                    ["John", "Stockton", "1234 Rodeo Dr", "USA"],
                    ["Patrick", "Star", "1234 Bikini Bottom", "Pacific Ocean"]
                ],
                [
                    ["Holden", "1234 Galactic Ave", "Europa"],
                    ["Stockton", "1234 Rodeo Dr", "USA"],
                    ["Star", "1234 Bikini Bottom", "Pacific Ocean"]
                ],
            )
        ]
    )
    def test_delete_column(self, header, data, expected):
        frame = Frame()
        frame.set_header(header)
        frame.set_data(data)
        frame.delete_column('first_name')
        assert frame.data == expected

    