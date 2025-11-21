from cyclomatic.calculator import *
from cyclomatic.cyclomatic import (
    cyclomatic_singly,
    cyclomatic_in_batch,
    cyclomatic_in_parallel
)

# Analyzed code may have crazy high depth.
# Increase the limit if analysis fails with RecursionError
import sys
sys.setrecursionlimit(10000)
