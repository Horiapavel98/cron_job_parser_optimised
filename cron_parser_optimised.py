import sys

timeLimits = {
    "minute"        : (0, 59),
    "hour"          : (0, 23),
    "day_of_month"  : (1, 31),
    "month"         : (1, 12),
    "day_of_week"   : (0, 7)
}

def timeUnitCount(timeOffset, key):
    # Get the time limits from the dictionary
    (start_limit, end_limit) = timeLimits[key]
    # Check for */ - every
    if timeOffset.find("*/") != -1:
        timeOffset = timeOffset[2:]
        if timeOffset == "*":
            result = ""
            for i in range(start_limit, end_limit + 1):
                result = result + str(i) + " "
            return result
        elif timeOffset.isnumeric() == False:
            raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' must be numeric value")
        elif int(timeOffset) < start_limit or int(timeOffset) >= end_limit:
            raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' must be between " + start_limit + " and " + end_limit)
        else:
            index = 0
            result = ""
            while index < end_limit:
                result = result + str(index) + " "
                index = index + int(timeOffset)
            return result
    # Check for alphanumeric
    else:
        if timeOffset == "*":
            result = ""
            for i in range(start_limit, end_limit + 1):
                result = result + str(i) + " "
            return result
        if timeOffset.find(",") != -1 and timeOffset.find("-") != -1:
            timeRanges = timeOffset.split(",")
            ranges = []
            result = ""
            for t in timeRanges:
                # Check if tuple, if not just append
                if t.find("-") == -1:
                    result = result + str(t) + " "
                else:
                    lt = tuple(t.split("-"))
                    ranges.append(lt)

            if checkIfRangesAreNumeric(ranges) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' ranges not valid - must be numeric only")

            if checkRanges(ranges) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' ranges not valid")
            
            if checkValidityOfTimeRanges(ranges, key) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' ranges threshholds must be in " + str(start_limit) + " to " + str(end_limit))


            for t in ranges:
                start = int(t[0])
                end = int(t[1])
                while start <= end:
                    result = result + str(start) + " "
                    start = start + 1
            return result
        elif timeOffset.find(",") != -1:
            # Mention: We can have multiple minutes in a sequence, this is different to the range
            # e.g. of valid sequence: 1, 15, 31
            times = timeOffset.split(",")
            
            # Check for numeric values
            if checkIfNumeric(times) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' argument must be numeric only")

            # Check if minute are in range 0-59
            if checkIfInTimesRange(times, key) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' " + key + " is not in " + start_limit + " to " + + end_limit)

            result = ""
            for time in times:
                result = result + time + " "
            return result

        elif timeOffset.find("-") != -1: 
            # if we want to specify multiple minutes using the hyphen
            times = timeOffset.split("-")

            # Check if range is not used incorrectly: it can only specify 2 limits, start and end.
            if len(times) > 2:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' range specified incorrectly - use (start_" + key + ")-(end_" + key + ")")

            # Check for numeric values
            if checkIfNumeric(times) == False:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' argument must be numeric only")
            
            start = int(times[0])
            end = int(times[1])

            # Check for valid bounds
            if start < start_limit or start > end_limit:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' invalid start minute '" + str(start) + "' for range")
            if end < start_limit or end > end_limit:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' invalid end minute '" + str(end) + "' for range")
            if start > end:
                raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' start " + key + " is greater than end " + key + " '" + str(end) + "' for range")

            result = ""
            while start <= end:
                result = result + str(start) + " "
                start = start + 1
            return result
        # If we get here means that either 'minutes' is only one minutes without additional quantifiers 
        # or 
        # 'minutes' is not numeric and it also doesn't have quantifiers(so it wasn't picked up earlier)
        elif timeOffset.isnumeric() == False:
            raise ValueError("Illegal Arguments for param " + key + " '" + timeOffset + "' must be numeric only, or range(-) or sequence(,)")
        else:
            return timeOffset

def checkValidityOfTimeRanges(ranges, key):
    for t in ranges:
        if checkIfInTimeRange(t[0], key) == False or checkIfInTimeRange(t[1], key) == False:
            return False
    return True

def checkIfInTimesRange(times, key):
    for timeUnit in times:
        # Also safe to cast to int here since we check for numeric before using this function.
        if checkIfInTimeRange(timeUnit, key) == False:
            return False
    return True

def checkIfInTimeRange(time, key):
    (start_limit, end_limit) = timeLimits[key]
    if int(time) < start_limit or int(time) > end_limit:
        return False
    return True

def checkIfNumeric(times):
    for timeUnit in times:
        if timeUnit.isnumeric() == False:
            return False
    return True

### Check if time ranges are numeric ###
def checkIfRangesAreNumeric(ranges):
    for t in ranges:
        if checkIfNumeric(t[0]) == False or checkIfNumeric(t[1]) == False:
            return False
    return True

### Check if ranges are not overflowing into one another and if they are valid ###
def checkRanges(ranges):
    i = 0
    while i < len(ranges) - 2:
        if ranges[i][0] > ranges[i][1]:
            return False
        if ranges[i+1][0] > ranges[i+1][1]:
            return False
        if ranges[i][1] > ranges[i+1][0]:
            return False
        i += 1
    return True


# ------------------- RUN ------------------- #

ls = sys.argv
ls = ls[1:]

### Variable for triggering testing ###
testing = False

def outputFormatter(args):
    # Check for argument length
    if  testing == False:
        if len(args) != 6:
            print("-----------------------------------------------")
            print("\nFor testing switch 'testing' variable to True\n")
            print("-----------------------------------------------")
            raise ValueError("Insufficient number of arguments: must be exactly 6: --> <MINUTE> <HOUR> <DAY_OF_MONTH> <MONTH> <DAY_OF_WEEK> <command>")

    minuteRow        = "minute        " + timeUnitCount(args[0], "minute")
    hourRow          = "hour          " + timeUnitCount(args[1], "hour")
    dayOfMonthRow    = "day of month  " + timeUnitCount(args[2], "day_of_month")
    monthRow         = "month         " + timeUnitCount(args[3], "month")
    dayOfWeekRow     = "day of week   " + timeUnitCount(args[4], "day_of_week")
    commandRow       = "command       " + args[5]

    return minuteRow + "\n" + hourRow + "\n" + dayOfMonthRow + "\n" + monthRow + "\n" + dayOfWeekRow + "\n" + commandRow

if testing == False:
    print(outputFormatter(ls))
else:
    print("For output change testing variable to False")