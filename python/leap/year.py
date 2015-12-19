def is_leap_year(year):
    return year % 4 == 0 and (year % 100 == 0) == (year % 400 == 0)
