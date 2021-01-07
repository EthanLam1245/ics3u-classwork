import math
from main import calculate_hypotenuse, total_fare, shipping_charge, calculate_median, ordinal_number


def test_calculate_hypotenuse():
    assert calculate_hypotenuse(3, 4) == 5
    assert calculate_hypotenuse(4, 3) == 5
    assert calculate_hypotenuse(12, 16) == 20
    assert calculate_hypotenuse(13, 16) == 5 * math.sqrt(17)
    assert calculate_hypotenuse(1, 1) == math.sqrt(2)


def test_total_fare():
    assert total_fare(0.14) == 4.25
    assert total_fare(0.3) == 4.5
    assert total_fare(1) == 5.75
    assert total_fare(100) == 182.5
    assert total_fare(0) == 4


def test_shipping_charge():
    assert shipping_charge(1) == 10.95
    assert shipping_charge(20) == 67
    assert shipping_charge(4) == 19.8
    assert shipping_charge(0) == 0
    assert shipping_charge(103) == 311.85


def test_calculate_median():
    assert calculate_median(-1, 0, -2) == -1
    assert calculate_median(103, 123, 219) == 123
    assert calculate_median(423, -123, 186) == 186
    assert calculate_median(100, 100, 100) == 100
    assert calculate_median(26, 23, 23) == 23


def test_ordinal_number():
    assert ordinal_number(1) == "first"
    assert ordinal_number(12) == "twelfth"  
    assert ordinal_number(6) == "sixth"
    assert ordinal_number(0) == ""
    assert ordinal_number(13) == ""
