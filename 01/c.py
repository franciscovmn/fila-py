@staticmethod
def combina(f_res, f1, f2):
    while not f1.vazia() or not f2.vazia():
        if not f1.vazia():
            f_res.enfileirar(f1.desenfileirar())
        if not f2.vazia():
            f_res.enfileirar(f2.desenfileirar())
