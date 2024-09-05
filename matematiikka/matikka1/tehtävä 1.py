import numpy as np

rad1 = 2.493
print(f"1)\ta) {rad1} rad on {np.degrees(rad1):.2f}°")
rad2 = 0.911
print(f"\tb) {rad2} rad on {np.degrees(rad2):.2f}°")

deg1 = 137.7
print(f"\n2)\ta) {deg1}° on {np.radians(deg1):.2f} rad")
deg2 = 62.3
print(f"\tb) {deg2}° on {np.radians(deg2):.2f} rad")

degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("\n3)\n"
      "Aste\t|\tRadiaani\n"
      "---------------------")
for deg in degrees:
    print(f"{deg}° \t|\t{np.radians(deg):.2f} rad")
