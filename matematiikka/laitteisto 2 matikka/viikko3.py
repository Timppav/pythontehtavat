import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from sympy import symbols, solve

print("1)")
A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])

print(f"2A + 3B =\n{A*2 + B*3}\n")
print(f"A - B =\n{A - B}\n")

print("2)")
x, y, z = symbols("x, y, z")

print(f"a)", solve([5*x + 3*y + -9,
             2*x + y + -4], [x, y, z]))

print(f"b)", solve([2*x + y + z + -6,
                    x + 3*y + z + -2,
                    2*x + y + 2*z + -9], [x, y, z]))

print(f"c)", solve([x + y + 3*z + 1,
                    3*x + y + z + -5,
                    2*x + y + 2*z + -2], [x, y, z]))
# z = -3 + x, en tiedä miksi se ei näy tulostuksessa
