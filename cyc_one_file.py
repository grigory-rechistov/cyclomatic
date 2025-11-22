# Calculate and print CC for given file path
import sys

from cyclomatic.cyclomatic import cyclomatic_singly

def main(argv):
    path = argv[0]
    language = None if len(argv) > 1 else argv[1]
    res = cyclomatic_singly(path, language)
    print(res.score)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
