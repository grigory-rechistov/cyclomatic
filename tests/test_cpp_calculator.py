import pytest
from cyclomatic.calculator.cpp_calculator import CppCalculator
from cyclomatic.ast.to_ast import to_ast


def get_cc_from_text(code:str) -> int:
    tree, _ = to_ast(source=code.encode('utf-8'), language='cpp')
    c = CppCalculator()
    c.visit(tree.root_node)
    return c.block.score


def test_cc_of_empty_function_is_one():
    code = """int foobar(char a) {}"""
    assert get_cc_from_text(code) == 1


def test_cc_of_if_inside_function_is_two():
    code = """int foobar(char a)
    {
        if (a > 5) {return 4;}
    }"""
    assert get_cc_from_text(code) == 2


def test_cc_of_switch_with_three_cases_is_four():
    code = """int foobar(char a)
    {
        switch(a) {
        case 1:
            return 3;
        case 2:
            return 4;
        case 3:
         return 5;
        }
        return 0;
    }"""
    assert get_cc_from_text(code) == 4


def test_cc_of_switch_with_default_is_two():
    code = """int foobar(char a)
    {
        switch(a) {
        default:
            break;
        return 0;
        }
    }"""
    assert get_cc_from_text(code) == 2


def test_cc_of_try_catch_is_two():
    code = """int main() {
    try {
        cout << "1";
    }
    catch (int num) {
        cout << "2";
    }
    return 0;
}"""
    assert get_cc_from_text(code) == 2

@pytest.mark.filterwarnings("ignore:Failed to parse")
def test_cc_of_undisciplined_ifdef():
    code = """int foobar(char a) {
    if (a > 0) {
        return 3
#ifdef FOO
        + a;
    } else if (a < 0) {
        return 7;
#else
        + 5;
#endif
    }
        return 0;
}"""
    assert get_cc_from_text(code) == 4
