def leap_year(year):
    """
    Determine whether an year is a leap year

    param: int year
    return: Bool
    
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
