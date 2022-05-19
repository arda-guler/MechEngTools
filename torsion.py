import math
pi = math.pi

def J_cylinder(r):
    return (pi/2) * (r**4)

def get_rot_angle(T, L, G, J):
    radi = (T * L) / (G * J)
    degr = math.degrees(radi)
    print("return: (radians, degrees)")
    return (radi, degr)

def get_shear(T, r, J):
    return T * r / J

def transmit_turn(turn_angle, shaft_r, other_r):
    return turn_angle * shaft_r/other_r
