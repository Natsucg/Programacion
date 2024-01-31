import random

class JuegoAdivinarNumero:
    def __init__(self, numero_minimo, numero_maximo):
        self.numero_minimo = numero_minimo
        self.numero_maximo = numero_maximo
        self.numero_a_adivinar = random.randint(numero_minimo, numero_maximo)
        self.intentos_realizados = 0

    def jugar(self):
        print(f"Bienvenido al juego de adivinar el número entre {self.numero_minimo} y {self.numero_maximo}.")

        while True:
            intento = int(input("Ingresa tu número: "))
            self.intentos_realizados += 1

            if intento < self.numero_a_adivinar:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > self.numero_a_adivinar:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! ¡Adivinaste el número {self.numero_a_adivinar} en {self.intentos_realizados} intentos!")
                break

# Uso del juego
if __name__ == "__main__":
    numero_minimo = 1
    numero_maximo = 100
    juego = JuegoAdivinarNumero(numero_minimo, numero_maximo)
    juego.jugar()