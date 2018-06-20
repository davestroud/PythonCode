import stdio
import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Compute using the law of cosines.

# Great circle distance in radians
angle1 = math.acos(math.sin(x1) * math.sin(x2)
                   + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# Convert back to degrees.
angle1 = math.degrees(angle1)

# Each degree on a great circle of Earth is 60 nautical miles.
distance1 = 60.0 * angle1

stdio.writeln(str(distance1) + ' nautical miles')

# Compute using the Haversine formula.

a = math.sin((x2 - x1) / 2.0) ** 2.0 \
    + (math.cos(x1) * math.cos(x2) * (math.sin((y2 - y1) / 2.0) ** 2.0))

# Great circle distance in radians
angle2 = 2.0 * math.asin(min(1.0, math.sqrt(a)))

# Convert back to degrees.
angle2 = math.degrees(angle2)

# Each degree on a great circle of Earth is 60 nautical miles.
distance2 = 60.0 * angle2

stdio.writeln(str(distance2) + ' nautical miles')
