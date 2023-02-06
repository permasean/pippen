from pippen.core.structures.frame import Frame
import pytest

class TestMethodsExperimental:
    @pytest.mark.parametrize(
        "data, expected",
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
                }, 
                {
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
    def test_delete_column(self, data, expected):
        frame = Frame(mode='experimental')
        frame.set_data(data)
        frame.delete_column('first_name')
        assert frame.data == expected

    