class Restaurante:
    def __init__(self):
        self.fila_pedido = []
        self.fila_pagamento = []
        self.fila_entrega = []

    def inserir_cliente(self, nome):
        self.fila_pedido.append(nome)
        print(f"Cliente {nome} adicionado à fila de pedidos.")

    def atender_pedido(self):
        if self.fila_pedido:
            cliente = self.fila_pedido.pop(0)
            self.fila_pagamento.append(cliente)
            print(f"{cliente} passou para a fila de pagamento.")
        else:
            print("Fila de pedidos vazia.")

    def atender_pagamento(self):
        if self.fila_pagamento:
            cliente = self.fila_pagamento.pop(0)
            self.fila_entrega.append(cliente)
            print(f"{cliente} passou para a fila de entrega.")
        else:
            print("Fila de pagamento vazia.")

    def atender_entrega(self):
        if self.fila_entrega:
            cliente = self.fila_entrega.pop(0)
            print(f"{cliente} recebeu sua encomenda.")
        else:
            print("Fila de entrega vazia.")
