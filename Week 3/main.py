"""
Partner Names: Yousef & Pavan
"""

from dow import getDayOfTheWeek, makeCalendar


# * Ask the user for a date
def getDayOfTheWeekForUserDate():

    print("Day of the Week Lookup")

    month = input("Enter month (1-12): ")

    if not month.isnumeric():
        print("Invalid month")
        return

    month = int(month)

    day = input("Enter day (1-31): ")

    if not day.isnumeric():
        print("Invalid day")
        return

    day = int(day)

    year = input("Enter year: ")

    if not year.isnumeric():
        print("Invalid year")
        return

    year = int(year)

    # * Check month and day range
    if month < 1 or month > 12:
        print("Invalid month")
        return

    if day < 1 or day > 31:
        print("Invalid day")
        return

    dayOfWeek = getDayOfTheWeek(year, month, day)

    print(f"{month}-{day}-{year} is a {dayOfWeek.lower()}.")


def main():

    # * Print the 2026 calendar
    makeCalendar()

    # * Ask for a custom date
    getDayOfTheWeekForUserDate()


main()