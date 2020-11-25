# Gong
import pytest

from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc=Calc()

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 1, 2), (-1, -1, -2)])
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert c == result

    @pytest.mark.parametrize('a,b,c',[(0,0,0),(1,1,0),(-1,-1,0)])
    def test_sub(self, a, b, c):
        result=self.calc.sub(a,b)
        assert c==result

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 1, 1), (-1, -1, 1)])
    def test_mul(self, a, b, c):
        result = self.calc.mul(a, b)
        assert c == result

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 1, 1), (-1, -1, 1)])
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        assert c == result


if __name__ == '__main__':
    pytest.main()
