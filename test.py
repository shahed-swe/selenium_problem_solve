import pytest

class TestDemo:
    
    @pytest.mark.parametrize('data', [4,6,7])
    def test_mark(self, data):
        if data > 3:
            assert True
        else:
            assert False, "Less then 5"