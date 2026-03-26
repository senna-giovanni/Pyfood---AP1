import pytest
from app.validador import validar_pedido


# etapa 1 - validação dos pedidos (tdd)

def test_pedido_valido_deve_retornar_true():
    pedido = {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": [
            {"nome": "Hamburguer", "preco": 15.00},
            {"nome": "Refrigerante", "preco": 8.00},
        ]
    }
    assert validar_pedido(pedido) is True


def test_pedido_sem_itens_deve_retornar_false():
    pedido = {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": []
    }
    assert validar_pedido(pedido) is False


def test_pedido_abaixo_do_valor_minimo_deve_retornar_false():
    pedido = {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": [
            {"nome": "Bala", "preco": 1.00},
        ]
    }
    assert validar_pedido(pedido) is False


def test_pedido_sem_endereco_deve_retornar_false():
    pedido = {
        "itens": [
            {"nome": "Hamburguer", "preco": 25.00},
        ]
    }
    assert validar_pedido(pedido) is False


def test_pedido_com_endereco_vazio_deve_retornar_false():
    pedido = {
        "endereco_entrega": "",
        "itens": [
            {"nome": "Hamburguer", "preco": 25.00},
        ]
    }
    assert validar_pedido(pedido) is False


def test_pedido_com_valor_exatamente_no_minimo_deve_retornar_true():
    pedido = {
        "endereco_entrega": "Av. Brasil, 10",
        "itens": [
            {"nome": "Lanche", "preco": 20.00},
        ]
    }
    assert validar_pedido(pedido) is True