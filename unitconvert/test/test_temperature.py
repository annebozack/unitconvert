from unitconvert import temperature

def test_fahrenheit_to_celsius():
    # 32F to C should be zero
    assert round(temperature.fahrenheit_to_celsius(32), 0) == 0

    # 98.6F to C should be 37
    assert round(temperature.fahrenheit_to_celsius(98.6), 0) == 37

from unitconvert.temperature import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    # 0C to F should be 32
    assert round(temperature.celsius_to_fahrenheit(0), 0) == 32

    # 37C to F should be 98.6
    assert round(temperature.celsius_to_fahrenheit(37), 1) == 98.6