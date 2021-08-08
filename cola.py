import vector


class cola(vector):

    def __init__(self, n):
        vector.__init__(self, n)
        self.primero=0
        self.ultimo=0

    def esLlena(self):
        return self.primero == self.ultimo

    def esVacia(self):
        return self.primero == self.ultimo

    def encolar(self,d):
        self.ultimo=(self.ultimo + 1) % self.n
        if self.esLlena():
            print("Cola llena, no se puede encolar\n")
            self.ultimo=(self.ultimo - 1 + self.n)%self.n
            return
            self.V[ultimo] = d

    def desencolar(self):
        if self.esVacia():
            print("Cola vacía, no se puede desencolar\n")
            return None
        self.primero = (self.primero + 1 )%self.n
        return self.V[primero]

    def siguiente(self):
        if self.esVacia():
            print("Cola vacía, no hay siguiente\n")
            return None
        aux = (self.primero + 1)%self.n
        return self.V[aux]
