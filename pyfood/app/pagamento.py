def finalizar_compra(pedido: dict, gateway_modulo) -> str:
    
    
    #1 - Verifica fraude antes de cobrar.
    #2 - Realiza a cobrança.
    #3 - Retorna 'Cmpra aprovada'.
    
    gateway_modulo.verificar_fraude(pedido)
    gateway_modulo.cobrar(pedido)
    return "Compra aprovada"