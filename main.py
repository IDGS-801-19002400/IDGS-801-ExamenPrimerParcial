
from pytest import main

from TuclaseExamen import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# Run unit tests automatically
main(['-vv'])
