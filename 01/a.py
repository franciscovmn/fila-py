class FilaSequencialCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.tamanho = 0

    def enfileirar(self, valor):
        if self.tamanho == self.capacidade:
            raise OverflowError("Fila cheia")
        fim = (self.inicio + self.tamanho) % self.capacidade
        self.fila[fim] = valor
        self.tamanho += 1

    def desenfileirar(self):
        if self.tamanho == 0:
            raise IndexError("Fila vazia")
        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def vazia(self):
        return self.tamanho == 0

    @staticmethod
    def combina(f_res, f1, f2):
        while not f1.vazia() or not f2.vazia():
            if not f1.vazia():
                f_res.enfileirar(f1.desenfileirar())
            if not f2.vazia():
                f_res.enfileirar(f2.desenfileirar())
