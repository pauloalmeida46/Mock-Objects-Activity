import pytest

from exercicio1.src.custom_stack_class import (
    CustomStack,
    StackEmptyException,
    StackFullException,
)


def test_push_one_element_in_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)

    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_new_stack_is_empty():
    cut = CustomStack(3)

    assert cut.is_empty() == True
    assert cut.size() == 0


def test_push_multiple_elements_updates_size_and_top():
    cut = CustomStack(3)

    cut.push(1)
    cut.push(2)
    cut.push(3)

    assert cut.size() == 3
    assert cut.is_empty() == False
    assert cut.top() == 3


def test_push_raises_stack_full_exception_when_limit_reached():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)

    with pytest.raises(StackFullException):
        cut.push(3)

    # garante que o elemento não foi adicionado além do limite
    assert cut.size() == 2


def test_pop_removes_and_returns_last_element():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)

    popped = cut.pop()

    assert popped == 2
    assert cut.size() == 1
    assert cut.top() == 1


def test_pop_raises_stack_empty_exception_when_stack_is_empty():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_raises_stack_empty_exception_when_stack_is_empty():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.top()


def test_top_does_not_remove_element():
    cut = CustomStack(3)
    cut.push(10)

    assert cut.top() == 10
    assert cut.size() == 1
