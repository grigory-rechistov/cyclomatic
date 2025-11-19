# Calculate and print churn for given file path
import subprocess
from pathlib import Path
import sys


def get_churn(path: str) -> int:
    # Query git for one line per commit touching the file, count number of
    # returned lines
    p = Path(path)
    cwd = str(p.parent)
    file = str(p.name)
    cmd = ("git", "log", "--oneline", "--", file)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd)
    churn = sum(1 for _ in p.stdout)
    p.wait()
    status = p.poll()
    p.stdout.close()
    if status != 0:
        raise RuntimeError(f"git failed with error code {status}")
    return churn


def main(path):
    print(get_churn(path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
