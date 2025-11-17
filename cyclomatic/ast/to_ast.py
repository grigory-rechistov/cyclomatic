import pathlib
from tree_sitter import (Language, Parser, Tree)
from cyclomatic.config import package_path, LANGUAGE_MAPPING
from typing import Tuple

import tree_sitter_python
import tree_sitter_c
import tree_sitter_cpp


def to_ast(*, source: bytes = None, path: str = None, language=None) -> Tuple[Tree, str]:
    """
    convert source file or souce to a tree_sitter.Tree

    :param source: souce code
    :param path: source file path
    :param language: supported language in
    :return: tree_sitter.Tree
    """
    if path:
        if language is None:
            path = pathlib.Path(path)
            suffix = path.suffix[1:]
            language = suffix

        if language not in LANGUAGE_MAPPING:
            raise NotImplementedError(path.suffix[1:])

        with open(path, 'rb') as f:
            source = f.read()
    elif source and language:
        pass
    else:
        raise Exception(
            "Wrong parameters! Try:\n"
            "to_ast(path='path/to/source')\n"
            "to_ast(path='path/to/source', language='py')\n"
            "to_ast(source=b'def fun():\n    return 0')\n"
        )

    PY_LANGUAGE = Language(tree_sitter_python.language())
    C_LANGUAGE = Language(tree_sitter_c.language())
    CPP_LANGUAGE = Language(tree_sitter_cpp.language())

    detected_language = {"py": PY_LANGUAGE,
                         "c": C_LANGUAGE,
                         "cpp": CPP_LANGUAGE,
                         }[language]
    parser = Parser(detected_language)
    return parser.parse(source), language
