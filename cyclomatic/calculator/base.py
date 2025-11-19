import tree_sitter
import warnings
import dataclasses
import typing
from cyclomatic.config import LANGUAGE_MAPPING


class TreeSitterNodeVisitor:

    language_tag = None

    def __init_subclass__(cls, **kwargs):
        # auto register calculator into the language mapping,
        # so the top level api could auto use the corresponding calculator
        if cls.language_tag is None:
            raise Exception(f'calculator:{cls} does not have the language_tag property.')
        if cls.language_tag not in LANGUAGE_MAPPING:
            raise Exception(f"language_tag:{cls.language_tag} does not have"
                            " corresponding tree-sitter parser")

        LANGUAGE_MAPPING[cls.language_tag][-1] = cls

    def visit(self, node: tree_sitter.Node):
        self.report_parsing_problems(node)

        method = 'visit_' + node.type
        # print("about to visit ", method)
        visitor = getattr(self, method, self.generic_visit)
        res = visitor(node)
        # print("exited ", method, node.start_point.row + 1, "<")
        return res

    def report_parsing_problems(self, node):
        if node.type == "ERROR":
            lineno = node.start_point.row+1
            warnings.warn(f"Failed to parse line {lineno}, expect"
                          " under-reported complexity: " + node.text.decode())

    def generic_visit(self, node: tree_sitter.Node):
        for _node in node.children:
            if _node.is_named:
                self.visit(_node)


@dataclasses.dataclass
class Block:
    id: int
    name_pos: typing.Tuple[int, int]
    score: float = 0
    sub_blocks: typing.List['Block'] = dataclasses.field(default_factory=list)
