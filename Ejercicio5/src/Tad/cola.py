class Cola:
    def __init__(self):
        self.cola_clientes = []

    def encolar(self, item):
        self.cola_clientes.append(item)

    def desencolar(self):
        return self.cola_clientes.pop(0) if self.cola_clientes else None

    def is_empty(self):
        return len(self.cola_clientes) == 0

    def __len__(self):
        return len(self.cola_clientes)

    def __iter__(self):
        return iter(self.cola_clientes)
