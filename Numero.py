import random

class JuegoAdivinarNumero:
    def __init__(self, numero_minimo, numero_maximo):
        self.numero_minimo = numero_minimo
        self.numero_maximo = numero_maximo
        self.numero_a_adivinar = random.randint(numero_minimo, numero_maximo)
        self.intentos_realizados = 0

    def mostrar_pista(self, intento):
        diferencia = abs(intento - self.numero_a_adivinar)
        if diferencia == 0:
            return "¡Correcto! Has adivinado el número."
        elif diferencia <= 5:
            return "Estás muy cerca."
        elif diferencia <= 10:
            return "Estás cerca."
        elif diferencia <= 20:
            return "Estás algo lejos."
        else:
            return "Estás muy lejos."
        
    def jugar(self):
        print(f"Bienvenido al juego de adivinar el número entre {self.numero_minimo} y {self.numero_maximo}.")

        while True:
            intento = int(input("Ingresa tu número: "))
            self.intentos_realizados += 1
            print(self.mostrar_pista(intento))
            

# Uso del juego
if __name__ == "__main__":
    numero_minimo = 1
    numero_maximo = 100
    juego = JuegoAdivinarNumero(numero_minimo, numero_maximo)
    juego.jugar()