def calcular_total_com_desconto(pedido: dict) -> float:
 
    # pedidos acima de 100 recebem 10% d
    total = 0
    for item in pedido.get("itens", []):
        total += item["preco"]
 
    if total > 100.00:
        total = total * 0.90
 
    return total
 
 
def dividir_conta(pedido: dict, numero_pessoas: int) -> float:
    
    # divide o total do pedido pelo numero de pessoas e lança o 
    # zerodivisionerror se for 0 pessoas
    
    total = 0
    for item in pedido.get("itens", []):
        total += item["preco"]
 
    return total / numero_pessoas
 