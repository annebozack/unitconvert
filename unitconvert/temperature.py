"""
A python module for converting temperature.
"""

def fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius.

    PARAMETERS
    ----------
    fahrenheit : float
        A temperature in fahrenheit

    RETURNS
    -------
    celsius : float
    """

    return (fahrenheit - 32)*(5/9)

def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit.

    PARAMETERS
    ----------
    celsius : float
        A temperature in celsius

    RETURNS
    -------
    fahrenheit : float
    """

    return celsius*(9/5) + 32

