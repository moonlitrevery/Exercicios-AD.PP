import pytest
from exercicio3 import raiz_quadrada, divisao

def test_raiz_quadrada_valida():
    assert raiz_quadrada(9) == 3.0

def test_divisao_valida():
    assert divisao(10, 2) == 5.0

def test_raiz_quadrada_invalida():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)

def test_divisao_invalida():
    with pytest.raises(ValueError):
        divisao(10, -5)
