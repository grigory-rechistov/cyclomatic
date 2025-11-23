import tree_sitter
import typing

from cyclomatic.calculator.base import TreeSitterNodeVisitor, Block
from cyclomatic.calculator.cpp_calculator import CppCalculator


class CeeCalculator(CppCalculator):
    language_tag = 'c'
