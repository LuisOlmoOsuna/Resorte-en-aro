from simulacion import simular
from animacion import animar


def main():

    # Resolver las ecuaciones del movimiento
    solucion = simular()

    # Animar el sistema
    animacion = animar(solucion)

    return animacion


if __name__ == "__main__":
    animacion = main()