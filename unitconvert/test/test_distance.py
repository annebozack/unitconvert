from unitconvert import distance

def test_miles_to_kilometers():
    # 3.1 miles to km should be 4.988954
    assert round(distance.miles_to_kilometers(3.1), 1) == 5.0

from unitconvert import distance

def test_kilometers_to_miles():
    #  5 km to miles should be 3.106855
    assert round(distance.kilometers_to_miles(5), 1) == 3.1
