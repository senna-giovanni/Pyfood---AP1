import pytest
from app.calculos import calcular_total_com_desconto, dividir_conta
 
 
# etapa 2 - calculos com fixture
 
def test_pedido_simples_sem_desconto(pedido_simples):
    total = calcular_total_com_desconto(pedido_simples)
    assert total == 14.00
 
 
def test_pedido_premium_com_desconto_de_10_porcento(pedido_premium):
    #total bruto: 45 + 60 + 20 = 125.00 → com 10% desconto = 112.50
    total = calcular_total_com_desconto(pedido_premium)
    assert total == pytest.approx(112.50)
 
 
def test_pedido_vazio_total_zero(pedido_vazio):
    total = calcular_total_com_desconto(pedido_vazio)
    assert total == 0.00
 
 
def test_arquivo_log_temporario_pode_ser_escrito(arquivo_log_temporario):
    arquivo_log_temporario.write("Log de teste\n")
    assert not arquivo_log_temporario.closed
 
 
# etapa 3 - teste de exceção
 
def test_deve_falhar_ao_dividir_por_zero(pedido_simples):
    with pytest.raises(ZeroDivisionError):
        dividir_conta(pedido_simples, 0)
 
 
def test_dividir_conta_entre_pessoas(pedido_premium):
    #total: 125.00 dividido por 5 = 25
    resultado = dividir_conta(pedido_premium, 5)
    assert resultado == pytest.approx(25.00)