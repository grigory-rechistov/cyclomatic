import sys
import os
import matplotlib.pyplot as plt
import subprocess
from cyclomatic.cyclomatic import cyclomatic_singly
from churn_one_file import get_churn
from pathlib import Path

# Ignore parsers defects
#import warnings
# warnings.filterwarnings("ignore", category=UserWarning)

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

    datapoints = []
    for line in p.stdout:
        filename, cc, churn = analyse_file(repo_dir, line)
        print(f"{filename} {cc} {churn}")
        datapoints.append((filename, cc, churn))

    status = p.wait()
    p.stdout.close()

    save_churn_complexity(os.path.realpath(repo_dir), datapoints)

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


def save_churn_complexity(project, datapoints):

    x_s = list(cc for (filename, cc, churn) in datapoints)
    y_s = list(churn for (filename, cc, churn) in datapoints)

    fig, dia = plt.subplots()
    dia.scatter(x_s, y_s)

    dia.set_title(f'CC-Churn diagram for {project}')
    dia.set_xlabel('Cyclomatic complexity')
    dia.set_ylabel('Churn')

    for (filename, cc, churn) in datapoints:
        dia.annotate(filename, xy=(cc, churn), textcoords='data')

    plt.savefig("churn-vs-complexity.svg")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
