import Lab2.bmi
import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_under_weight():
    result =-1
    test_result=Lab2.bmi.calculate_bmi(weight=20, height=1.5)

    assert (test_result==result)

def test_bmi_normal_weight():
    result = 0
    test_result = Lab2.bmi.calculate_bmi(weight=55, height=1.7)

    assert (test_result == result)


def test_bmi_over_weight():
    result = 1
    test_result = Lab2.bmi.calculate_bmi(weight=100, height=1.7)

    assert (test_result == result)