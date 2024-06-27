
from factorial_module.factorial_module import *

def test_factorial_iterative():
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(5) == 120
    assert_raises_value_error(factorial_iterative, -1)

def test_factorial_recursion():
    assert factorial_recursion(0) == 1
    assert factorial_recursion(1) == 1
    assert factorial_recursion(5) == 120
    assert_raises_value_error(factorial_recursion, -1)

def test_clumsy():
    assert clumsy(0) == 0
    assert clumsy(1) == 1
    assert clumsy(5) == 7 
    assert_raises_value_error(clumsy, -1)

def assert_raises_value_error(func, arg):
    try:
        func(arg)
        assert False, f"Expected ValueError for argument {arg}, but no exception was raised."
    except ValueError:
        pass  


    
  
