import math

sigma_x = 0
sigma_y = -18.50
tau = 4.88

sigma_mean = (sigma_x + sigma_y) / 2
sigma_diff = (sigma_x - sigma_y) / 2
R = (tau**2 + sigma_diff**2)**(0.5)

sigma_max = sigma_mean + R
sigma_min = sigma_mean - R

principal_angle_rad = 0.5 * math.atan(tau/sigma_diff)
principal_angle_deg = math.degrees(principal_angle_rad)

print("sigma_diff", sigma_diff)
print("sigma_mean", sigma_mean)
print("Theta_p:", principal_angle_deg)
print("Sigma max:", sigma_max)
print("Sigma min:", sigma_min)
print("Shear max:", R)
