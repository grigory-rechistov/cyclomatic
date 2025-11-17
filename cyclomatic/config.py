import pathlib
import cyclomatic


package_path = pathlib.Path(cyclomatic.__file__).parent

# This mapping is dynamically updated on runtime when classes and modules are
# loaded. Very nasty mechanism based on __init_subclass__ hook magic
LANGUAGE_MAPPING = {
    'py': [None, 'python', None],
    'c': [None, 'c', None],
    'cpp': [None, 'cpp', None],
}
