"""
Partner Names: Yousef & Pavan
"""

# * Month and day codes
MONTH_CODES = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

DAYS_OF_WEEK = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]


# * Check if a year is a leap year
def isLeapYear(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# * Find the day of the week
def getDayOfTheWeek(year, month, day):

    monthCode = MONTH_CODES[month - 1]

    # * Steps 1 to 3
    lastTwoDigits = year % 100
    numberOfTwelves = lastTwoDigits // 12
    remainder = lastTwoDigits % 12
    numberOfFours = remainder // 4

    # * Leap year adjustment
    if isLeapYear(year) and (month == 1 or month == 2):
        monthCode = monthCode - 1

    # * Century adjustments
    if 1600 <= year < 1700:
        monthCode = monthCode + 6
    elif 1700 <= year < 1800:
        monthCode = monthCode + 4
    elif 1800 <= year < 1900:
        monthCode = monthCode + 2
    elif 2000 <= year < 2100:
        monthCode = monthCode + 6
    elif 2100 <= year < 2200:
        monthCode = monthCode + 4

    # * Final calculation
    total = numberOfTwelves + remainder + numberOfFours + day + monthCode
    dayNumber = total % 7

    return DAYS_OF_WEEK[dayNumber]


# * Print every day in 2026
def makeCalendar():

    year = 2026

    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeapYear(year):
        daysInMonths[1] = 29

    # * Loop through every month and day
    for month in range(1, 13):

        numberOfDays = daysInMonths[month - 1]

        for day in range(1, numberOfDays + 1):

            dayOfWeek = getDayOfTheWeek(year, month, day)

            print(f"{month}-{day}-{year} is a {dayOfWeek.lower()}.")