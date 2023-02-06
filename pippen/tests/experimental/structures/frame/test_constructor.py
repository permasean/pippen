from pippen.core.structures.frame import Frame

class TestConstructorExperimental:
    def test_experimental_mode(self):
        frame = Frame(mode="experimental")
        assert isinstance(frame.data, dict)
        assert isinstance(frame.header, list)