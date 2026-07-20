import math

anglestr=input("enter an angle in degrees:")

angledegrees=float(anglestr)

angleradians=math.radians(angledegrees)

sine=math.sin(angleradians)
cosine=math.cos(angleradians)
tangent=math.tan(angleradians)

print(f"for an angle of {angledegrees} degrees:")

print(f"sine:{sine}")
print(f"tangent{tangent}")
print(f"cosine{cosine}")