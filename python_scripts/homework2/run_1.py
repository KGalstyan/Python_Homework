def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # print("True")
        return True
    else:
        # print("False")
        return False

# is_leap(2008)
# is_leap(2000)
# is_leap(1900)
# is_leap(2025)
# is_leap(2028)