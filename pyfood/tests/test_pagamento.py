from unittest.mock import call
from app.pagamento import finalizar_compra
 
 
# etapa 4 - dublÊ de testes (mock)
 
def test_deve_verificar_fraude_antes_de_cobrar(mocker, pedido_simples):
    mock_gateway = mocker.Mock()
 
    resultado = finalizar_compra(pedido_simples, mock_gateway)
 
    roteiro_esperado = [
        call.verificar_fraude(pedido_simples),
        call.cobrar(pedido_simples),
    ]
    mock_gateway.assert_has_calls(roteiro_esperado, any_order=False)
    assert resultado == "Compra aprovada"
 
 
def test_finalizar_compra_retorna_compra_aprovada(mocker, pedido_premium):
    mock_gateway = mocker.Mock()
 
    resultado = finalizar_compra(pedido_premium, mock_gateway)
 
    assert resultado == "Compra aprovada"
 
 
def test_gateway_cobrar_e_verificar_fraude_sao_chamados(mocker, pedido_simples):
    mock_gateway = mocker.Mock()
 
    finalizar_compra(pedido_simples, mock_gateway)
 
    mock_gateway.verificar_fraude.assert_called_once_with(pedido_simples)
    mock_gateway.cobrar.assert_called_once_with(pedido_simples)