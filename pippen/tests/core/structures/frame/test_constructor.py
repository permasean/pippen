from pippen.core.structures.frame import Frame

class TestConstructor:
    def test_standard_mode(self):
        frame = Frame()
        assert isinstance(frame.data, list)
        assert isinstance(frame.header, list)