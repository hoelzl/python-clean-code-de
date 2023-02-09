from simple_pytest.arithmetic import lerp, my_abs, negate, sign


def test_sign_for_positive_number():
    assert sign(2) == 1


def test_sign_for_negative_number():
    assert sign(-2) == -1


def test_sign_for_zero():
    assert sign(0) == 0


class TestLerp:
    def test_for_t_eq_0(self):
        assert lerp(1, 3, 0) == 1

    def test_for_t_eq_1(self):
        assert lerp(1, 3, 1) == 3

    def test_for_intermediate_t(self):
        # Maybe use isclose here, although the result is exact for t == 0.5 and integer
        # boundaries.
        assert lerp(1, 3, 0.5) == 2

    def something_else(self):
        # This method is not a test because it does not have `test` in the name!
        assert lerp(1, 3, 0.1) == 1.5


def test_negate():
    assert negate(2) == -2
    assert negate(-2) == 2


def test_my_abs():
    assert my_abs(2) == 2
    assert my_abs(-2) == 2
