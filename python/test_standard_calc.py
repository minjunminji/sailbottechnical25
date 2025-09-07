from standard_calc import bound_to_180, is_angle_between

""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180
    assert bound_to_180(360) == 0
    assert bound_to_180(-360) == 0
    assert bound_to_180(540) == -180
    assert bound_to_180(600) == -120
    assert bound_to_180(719) == -1


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert not is_angle_between(0, 3, 2)
    assert not is_angle_between(0, 359, 2)
    assert not is_angle_between(0, 0, 90)
    assert not is_angle_between(0, 90, 90)
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)
    assert is_angle_between(350, 355, 10)
    assert not is_angle_between(345, 180, 10)
    assert not is_angle_between(-720, 0, 90)
