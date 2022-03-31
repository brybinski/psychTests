from typing import *

# I just didn't have time to write better solution for
# Excel VBA
lst: List = [1,3,4,5,8,9,10,12,13,14,17,18,20,21,22,23,25,27,29,30,31,32,34,36,37,38,40,41,42,43,47,48,51,54,55,56,57,58,59,62,63,65,67,68,69,70,71,72,73,74,75,78,79,82,83,86,87,88,89,90]

it: int = 0
for i in lst:
    print(f"indexes({it}) = {i+9}")
    it += 1
