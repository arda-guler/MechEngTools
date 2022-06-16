sigma_x = 0
sigma_y = 0
sigma_z = -18.50E6

tau_xy = 0
tau_xz = 4.88E6
tau_yz = 0

E = 200E9
v = 0.3

G = E/(2*(1+v))

e_x = sigma_x/E  - v*sigma_y/E - v*sigma_z/E
e_y = sigma_y/E  - v*sigma_x/E - v*sigma_z/E
e_z = sigma_z/E  - v*sigma_y/E - v*sigma_x/E

gamma_xy = tau_xy/G
gamma_xz = tau_xz/G
gamma_yz = tau_yz/G

print("e_x", format(e_x, ".2E"))
print("e_y", format(e_y, ".2E"))
print("e_z", format(e_z, ".2E"))

print("gamma_xy", format(gamma_xy, ".2E"))
print("gamma_xz", format(gamma_xz, ".2E"))
print("gamma_yz", format(gamma_yz, ".2E"))
