"""
A python module for converting distance.
"""

def miles_to_kilometers(miles):
    """Convert miles to kilometers.

    PARAMETERS
    ----------
    miles : float
        A distance in miles

    RETURNS
    -------
    km : float
    """

    return miles*1.60934

def kilometers_to_miles(km):
    """Convert kilometers to miles.

    PARAMETERS
    ----------
    km : float
        A distance in kilometers

    RETURNS
    -------
    miles : float
    """

    return km*0.621371
