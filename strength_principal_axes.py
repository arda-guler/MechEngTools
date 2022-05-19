# FOR ROTATING TO PRINCIPAL AXES

import math

def rotate(x, y):
    angle = math.radians(17.31)
    m11 = math.cos(angle)
    m12 = -math.sin(angle)
    m21 = math.sin(angle)
    m22 = math.cos(angle)

    return float(x * m11 + y * m21), float(x * m12 + y * m22)

while True:
    Iu = 8.265*10**(-6)
    Iv = 1.169*10**(-6)

    Mu = -43.1
    Mv = -36.47

    u = -float(input("u:"))
    v = float(input("v:"))

    #u, v = rotate(u, v)

    sigma = (v * Mu/Iu) - (u * Mv/Iv) + 250000
    print(sigma)
    print("")
