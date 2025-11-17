# Calculate and print CC for given file path
import sys

from cyclomatic.cyclomatic import cyclomatic_singly

def main(path):
    res = cyclomatic_singly(path)
    print(res.score)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
