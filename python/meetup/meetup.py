from datetime import date
from calendar import monthrange

def meetup_day(year, month, day, num):
    """Return a day in the given year and month and on the given
    day of the week that fits the requirements set in 'num'.
    'num' may be one of the following:
        "teenth", "last", "1st", "2nd", "3rd" or "4th"
    """
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index = week.index(day)
    month_length = monthrange(year, month)[1]
    days_in_month = [date(year, month, i) for i in range(1, month_length + 1)]
    candidates = [d for d in days_in_month if d.weekday() == day_index]

    if num == 'teenth':
        for candidate in candidates:
            if 13 <= candidate.day <= 19:
                return candidate
    if num == 'last':
        return candidates[len(candidates)-1]
    return candidates[int(num[0])-1]
