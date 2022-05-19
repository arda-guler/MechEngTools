import math

angle1 = float(input("Angle 1 (deg): "))
angle2 = float(input("Angle 2 (deg): "))

cos_a1 = math.cos(math.radians(angle1))
cos_a2 = math.cos(math.radians(angle2))

cos_a3 = math.sqrt(1 - (cos_a1**2 + cos_a2**2))
angle3 = math.degrees(math.acos(cos_a3))

print(angle3)
