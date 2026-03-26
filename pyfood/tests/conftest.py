import pytest
 
 
@pytest.fixture
def pedido_vazio():
    #pedido sem item
    return {
        "endereco_entrega": "Rua Vazia, 0",
        "itens": []
    }
 
 
@pytest.fixture
def pedido_simples():
    #pedido que não chega a 50 reais
    return {
        "endereco_entrega": "Av. Principal, 45",
        "itens": [
            {"nome": "Suco", "preco": 8.00},
            {"nome": "Coxinha", "preco": 6.00},
        ]
    }
 
 
@pytest.fixture
def pedido_premium():
    #pedido que passa de 100 reais
    return {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": [
            {"nome": "Hamburguer Duplo", "preco": 45.00},
            {"nome": "Pizza Grande", "preco": 60.00},
            {"nome": "Sobremesa", "preco": 20.00},
        ]
    }
 
 
@pytest.fixture
def arquivo_log_temporario(tmp_path):
    #fixture com yield
    caminho = tmp_path / "log_teste.txt"
    arquivo = open(caminho, "w", encoding="utf-8")
    yield arquivo
    arquivo.close()