import random

import pytest

from exercicio1.src.custom_stack_class import CustomStack
from exercicio2.src.number_asc_order import NumberAscOrder


def test_sort_pilha_com_seis_numeros_sorteados_da_mega_sena(mocker):
    numeros_sorteados = random.sample(range(1, 61), 6)

    mock_stack = mocker.Mock(spec=CustomStack)
    # is_empty() retorna False enquanto houver elementos e True após o 6º pop
    mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
    # pop() devolve os números na ordem em que teriam sido empilhados (LIFO)
    mock_stack.pop.side_effect = list(reversed(numeros_sorteados))

    resultado = NumberAscOrder().sort(mock_stack)

    assert resultado == sorted(numeros_sorteados)
    assert mock_stack.pop.call_count == 6
    assert mock_stack.is_empty.call_count == 7


def test_sort_pilha_vazia(mocker):
    mock_stack = mocker.Mock(spec=CustomStack)
    mock_stack.is_empty.return_value = True

    resultado = NumberAscOrder().sort(mock_stack)

    assert resultado == []
    mock_stack.pop.assert_not_called()


def test_sort_com_parametro_que_nao_e_custom_stack_lanca_type_error():
    with pytest.raises(TypeError):
        NumberAscOrder().sort([1, 2, 3, 4, 5, 6])
