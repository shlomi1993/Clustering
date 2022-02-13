# Shlomi Ben-Shushan

import sys
import numpy as np

K = int(sys.argv[1])
open("randomCents.txt", "w").close()
file = open("randomCents.txt", "a")
for i in range(K):
    cent = str(np.random.sample(3).round(4)).replace("[", "").replace("]", "") + "\n"
    file.write(cent)
file.close()



