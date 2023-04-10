class MathDojo:
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, *args):
        for arg in args:
            self.resultado += arg
        return self
    
    def restar(self, *args):
        for arg in args:
            self.resultado -= arg
        return self
md = MathDojo()
resultado = md.sumar(2).sumar(3, 1).restar(1).resultado
print(resultado)  # Output: 8