# Cyclomatic Complexity vs Churn plot generator

What this plot is and why it matters:
<https://www.stickyminds.com/article/getting-empirical-about-refactoring>.

## Dependencies

This project was tested to work with Python 3.10 on Linux.

A few Python dependencies, listed in requirements.txt, are
fetched by `pip3` into the virtual environment (see steps below).

1. `git` command line utility to calculate churn.
2. Tree-Sitter for parsing and walking over source files.
3. Matplotlib for visualising results.

## Installing the tool and its dependencies

0. Clone this repository, enter its top folder in command line shell.

1. Create and activate virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

2. (Optional, required if you are behind firewall) Set up network proxy to be able to fetch dependencies:

    export https_proxy=<your-proxy>

3. Install dependencies:

    pip3 install -r requirements.txt

## Invocation

Run `plot.py` on a folder with a Git repository.
E.g., to analyze the project itself as a smoke test:

    python3 ./plot.py .

This should print one line per analysed file in format `file-name cyclic-complexity churn`.

At the end, it should generate a new SVG file `churn-vs-complexity.svg`.
You can open that SVG in your browser as a picture.

Currently, it looks for files with extensions matching Python, C and C++ files recursively
in a given folder.

When completed, it puts file called `churn-vs-complexity.svg` into current folder.


===========================================================

# Original README

## Feature:
> python 3.10.0 is required
1. calculate cyclomatic complexity of a program (python)
2. generate ast from source code with the help of tree-sitter
3. support the calculation in parallel when the target is a directory


## Examples:
```
import pathlib
import cyclomatic
from cyclomatic import (
    cyclomatic_singly,
    cyclomatic_in_batch,
    cyclomatic_in_parallel
)

package_path = pathlib.Path(cyclomatic.__file__).parent

# get the cyclomatic complexity of the whole file
result = cyclomatic_singly(str(package_path / 'cyclomatic.py'))
score_of_the_module = result.score

# get the cyclomatic complexity under the target directory
result = cyclomatic_in_batch(str(package_path))
file_names = list(result.keys())
corresponding_complexity_score = [i.score for i in list(result.values())]

# calculating in parallel would be much more efficient if there are many files
result = cyclomatic_in_parallel(str(package_path))

```

## Introduction:

- The cyclomatic complexity is equal to the num of decision point plus one.
This package use two steps to calculate it:
  1. generates ast from the source code with the help of tree-sitter
  2. walks the ast and counts the num of decision points

- package structure:
  1. cyclomatic.ast is responsible for ast generation.
  2. cyclomatic.calculator is responsible for calculation of the cyclomatic complexity. every module under this package is a calculator for the target program language. Though it only supports python for now. 


## Concepts:

[Cyclomatic complexity - Wikiwand](https://www.wikiwand.com/en/Cyclomatic_complexity)

[Control-flow graph - Wikiwand](https://www.wikiwand.com/en/Control-flow_graph)

## Resources:

tree-sitter python binding: [py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
