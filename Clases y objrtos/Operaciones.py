class Operaciones: 

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


    def sumar(self):
       
       result = self.n1 + self.n2;
       print(result)

    def restar(self):
     print(self.n1 - self.n2)

    def multiplicar(self):
     print(self.n1 * self.n2)

    def dividir(self):
        print(self.n1 /self.n2)
     


suma1 = Operaciones(10,5)

suma1.sumar()
suma1.restar()
suma1.multiplicar()
suma1.dividir()








    

        
        