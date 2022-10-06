class TestingSuite():
    def test_type(self):
        assert type(1) == int

    def test_str(self):
        assert 'pytest'.capitalize() == 'Pytest'