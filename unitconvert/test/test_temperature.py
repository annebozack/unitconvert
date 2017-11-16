from unitconvert import temperature

def test_fahrenheit_to_celsius():
    # 32F to C should be zero
    assert temperature.fahrenheit_to_celsius(32) == 0

    # 98.6F to C should be 37
    assert temperature.fahrenheit_to_celsius(98.6) == 37

from unitconvert.temperature import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    # 0C to F should be 32
    assert temperature.celsius_to_fahrenheit(0) == 32

    # 37C to F should be 98.6
    assert temperature.celsius_to_fahrenheit(37) == 98.6