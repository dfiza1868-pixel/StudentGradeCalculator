from grade_calculator import total_marks, average, grade, is_pass


def test_total_marks():
    assert total_marks([80, 90, 70, 60, 50]) == 350


def test_average():
    assert average([80, 90, 70, 60, 50]) == 70


def test_grade_a():
    assert grade(95) == "A"


def test_grade_b():
    assert grade(85) == "B"


def test_pass():
    assert is_pass([60, 70, 80, 90, 50]) is True


def test_fail():
    assert is_pass([60, 70, 80, 90, 20]) is False


def test_grade_f():
    assert grade(40) == "F"