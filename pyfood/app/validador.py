def validar_pedido(pedido: dict) -> bool:

    # Regra do endereço não poder estar vazio
    if "endereco_entrega" not in pedido or not pedido["endereco_entrega"]:
        return False
 
    # Regra do 1 item
    itens = pedido.get("itens", [])
    if len(itens) < 1:
        return False
 
    # Regra do valor minimo de 20
    total = 0
    for item in itens:
        total += item["preco"]
 
    if total < 20.00:
        return False
 
    return True
 