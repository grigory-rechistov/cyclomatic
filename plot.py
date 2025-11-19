import sys
import os
import matplotlib.pyplot as plt
import subprocess
from cyclomatic.cyclomatic import cyclomatic_singly
from churn_one_file import get_churn
from pathlib import Path

def one_file(path):
    res = cyclomatic_singly(path)
    return res.score

extension_to_file_type = {
    '*.py': 'py',
    '*.c': 'c',
    '*.cpp': 'cpp',
    '*.cc': 'cpp',
    '*.h': 'cpp',
    '*.hpp': 'cpp',
    '*.C': 'cpp'
}


def main(argv):
    repo_dir = determine_root_dir(argv)

    wildcards = tuple(extension_to_file_type.keys())
    cmd = ("git", "ls-files") + wildcards
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         cwd=repo_dir)

    for line in p.stdout:
        filename, cc, churn = analyse_file(repo_dir, line)
        print(f"{filename} {cc} {churn}")

    status = p.wait()
    p.stdout.close()

    # TODO: plot the data

# x = [1,2,3]
# y = [4,5,6]


# plt.scatter(x, y)

# plt.annotate('ey', xy= (2,5), textcoords='data')

# plt.savefig("churn-vs-complexity.svg")
# # plt.show()


    return status


def analyse_file(repo_dir, line):
    filename = line.decode().strip()
    full_filename = os.path.join(repo_dir, filename)
    extension = Path(full_filename).suffix
    language = extension_to_file_type['*' + extension]

    cc = cyclomatic_singly(full_filename, language=language).score
    churn = get_churn(full_filename)
    return filename, cc, churn


def determine_root_dir(argv):
    if len(argv) > 1:
        repo_dir = sys.argv[1]
    else:
        repo_dir = "."
    return repo_dir


if __name__ == "__main__":
    sys.exit(main(sys.argv))
