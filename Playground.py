import stdio
import sys
import random


year = int(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and (year % 100 != 0)
isLeapYear = isLeapYear or (year % 400 == 0)


stdio.writeln(isLeapYear)

stdio.writeln(random.randrange(2, 10))
