from cyclomatic.calculator.cpp_calculator import CppCalculator
from cyclomatic.ast.to_ast import to_ast


def test_cc_of_empty_function_is_one():
    code = """int foobar(char a) {}"""

    tree, _ = to_ast(source=code.encode('utf-8'), language='cpp')
    c = CppCalculator()
    c.visit(tree.root_node)

    assert c.block.score == 1
