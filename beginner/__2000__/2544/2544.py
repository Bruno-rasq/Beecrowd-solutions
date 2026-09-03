import math
import sys

for line in sys.stdin:
    n = int(line.strip())
    clonagem = int(math.log2(n))
    print(clonagem)