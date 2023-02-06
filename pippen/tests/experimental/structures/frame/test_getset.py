from pippen.core.structures.frame import Frame
import pytest

class TestGetSetExperimental:
    @pytest.mark.parametrize(
        "data",
        [
            (
                {
                    "first_name": 
                        {
                            1: "Holly", 
                            2: "James", 
                            3: "John"
                        }, 
                    "last_name": 
                        {
                            1: "Sullinger", 
                            2: "Knowles", 
                            3: "Parker"
                        }
                }
            )
        ]
    )
    def test_set_data(self, data):
        frame = Frame('experimental')
        frame.set_data(data)
        assert frame.data == data