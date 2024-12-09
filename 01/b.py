class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, valor):
        novo_no = No(valor)
        if not self.inicio:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if not self.inicio:
            raise IndexError("Fila vazia")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        return valor

    def vazia(self):
        return self.inicio is None

    @staticmethod
    def combina(f_res, f1, f2):
        while not f1.vazia() or not f2.vazia():
            if not f1.vazia():
                f_res.enfileirar(f1.desenfileirar())
            if not f2.vazia():
                f_res.enfileirar(f2.desenfileirar())
