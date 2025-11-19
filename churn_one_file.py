# Calculate and print churn for given file path
import subprocess
import sys


def main(path):
    # Query git for one line per commit touching the file, count number of
    # returned lines
    cmd = ("git", "log", "--oneline", "--", path)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    churn = sum(1 for _ in p.stdout)
    p.wait()
    status = p.poll()
    p.stdout.close()
    if status != 0:
        print(f"git failed with error code {status}", file=sys.stderr)
        return 1

    print(churn)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

