import pytest
from Carrinho import Item, Carrinho


def test_criar_item_valido():
    item = Item("Notebook", 3500, 1)
    assert item.subtotal() == 3500


def test_criar_item_invalido_preco():
    with pytest.raises(ValueError, match="preço"):
        Item("Notebook", -100, 1)


def test_criar_item_invalido_qtd():
    with pytest.raises(ValueError, match="quantidade"):
        Item("Notebook", 2000, 0)


def test_adicionar_item_ao_carrinho():
    carrinho = Carrinho()
    item = Item("Mouse", 100, 2)
    carrinho.adicionar_item(item)
    assert len(carrinho.itens) == 1


def test_remover_item_existente():
    carrinho = Carrinho()
    carrinho.adicionar_item(Item("Mouse", 100, 2))
    carrinho.remover_item("Mouse")
    assert len(carrinho.itens) == 0


def test_remover_item_inexistente():
    carrinho = Carrinho()
    carrinho.adicionar_item(Item("Mouse", 100, 2))
    with pytest.raises(ValueError, match="não encontrado"):
        carrinho.remover_item("Teclado")


def test_calcular_total():
    carrinho = Carrinho()
    carrinho.adicionar_item(Item("Mouse", 100, 2))   # 200
    carrinho.adicionar_item(Item("Teclado", 200, 1)) # 200
    assert carrinho.calcular_total() == 400


def test_listar_itens():
    carrinho = Carrinho()
    carrinho.adicionar_item(Item("Notebook", 3000, 1))
    carrinho.adicionar_item(Item("Mouse", 100, 2))
    itens = carrinho.listar_itens()
    assert ("Notebook", 1, 3000, 3000) in itens
    assert ("Mouse", 2, 100, 200) in itens
