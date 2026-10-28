from calculator import divide


def test_normal_division():
    assert divide(10, 2) == 5.0
    print("TC01: PASS")


def test_division_by_zero():
    assert divide(10, 0) == "Error: Cannot divide by zero"
    print("TC02: PASS")


def test_negative_division():
    assert divide(-10, 2) == -5.0
    print("TC03: PASS")


test_normal_division()
test_division_by_zero()
test_negative_division()

print("All test cases completed.")