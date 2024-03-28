import numpy as np

a = 1.6
b = 2.3
a2 = a**2
b2 = b**2
c2 = a2 + b2
c = np.sqrt(c2)
print("1)"
      "\n{}m\u00b2".format(a), "+", "{}m\u00b2".format(b), "=", "{}m\u00b2".format(a + b),
      f"\n= {a2:.2f}m + {b2:.2f}m = {c2:.2f}m"
      f"\n= √{c2:.2f}m = {c:.2f}m")
