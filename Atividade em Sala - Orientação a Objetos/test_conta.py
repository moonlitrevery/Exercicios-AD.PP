import pytest
from Conta import Conta

def test_criacao_conta():
    conta = Conta(123, "Luna")
    assert conta.numero == 123
    assert conta.titular == "Luna"
    assert conta.saldo == 0.0


def test_deposito_valido():
    conta = Conta(123, "Luna")
    conta.depositar(100)
    assert conta.saldo == 100


def test_deposito_invalido():
    conta = Conta(123, "Luna")
    with pytest.raises(ValueError, match="positivo"):
        conta.depositar(-50)


def test_saque_valido():
    conta = Conta(123, "Luna")
    conta.depositar(200)
    conta.sacar(150)
    assert conta.saldo == 50


def test_saque_invalido_valor_negativo():
    conta = Conta(123, "Luna")
    conta.depositar(100)
    with pytest.raises(ValueError, match="positivo"):
        conta.sacar(-10)


def test_saque_invalido_saldo_insuficiente():
    conta = Conta(123, "Luna")
    conta.depositar(50)
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta.sacar(100)


def test_extrato():
    conta = Conta(123, "Luna")
    conta.depositar(250)
    extrato = conta.extrato()
    assert "Conta: 123" in extrato
    assert "Titular: Luna" in extrato
    assert "Saldo: 250.00" in extrato
