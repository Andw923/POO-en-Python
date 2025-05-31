# carro_autonomo.py

class CarroAutonomo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def estado(self):
        return f"{self.marca} {self.modelo} va a {self.velocidad_actual} km/h"

# Ejemplo de uso
if __name__ == "__main__":
    carro = CarroAutonomo("Tesla", "Model X", 250)
    carro.acelerar(60)
    carro.acelerar(100)
    carro.frenar(30)
    print(carro.estado())
