import numpy as np

# 1
rng = np.random.default_rng()

taulukko = np.sort(rng.integers(low=1, high=101, size=20))
taulukko2d = taulukko.reshape(4, 5)

print(taulukko2d)

# 2

u = np.array([2, 3])
v = np.array([4, -7])
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

# 3

print(f"\nVektorin u = 2i + 3j normi: ", np.linalg.norm(u), "\n"
      "Vektorin v = 4i - 7j normi: ", np.linalg.norm(v), "\n"
      "Vektorin uu = i + j + k normi: ", np.linalg.norm(uu), "\n"
      "Vektorin vv = 3i - 3j + 2k normi: ", np.linalg.norm(vv), "\n")
