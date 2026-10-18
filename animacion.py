import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from parametros import R


def animar(solucion):

    Phi = solucion.y[0]
    l = solucion.y[1]

    # Coordenadas del punto de enganche
    x_A = R * np.cos(Phi)
    y_A = R * np.sin(Phi)

    # Coordenadas de la masa
    x_M = (R + l) * np.cos(Phi)
    y_M = (R + l) * np.sin(Phi)

    # Figura
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.set_aspect("equal")
    ax.grid()

    # Límites de la animación
    limite = R + np.max(np.abs(l)) + 0.5

    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)

    # Dibujamos el aro
    angulo_aro = np.linspace(0, 2 * np.pi, 300)

    x_aro = R * np.cos(angulo_aro)
    y_aro = R * np.sin(angulo_aro)

    ax.plot(x_aro, y_aro)

    # Elementos que se actualizarán
    punto_A, = ax.plot([], [], "o")
    masa, = ax.plot([], [], "o")
    resorte, = ax.plot([], [], "-")

    def actualizar(frame):

        # Punto de enganche
        punto_A.set_data(
            [x_A[frame]],
            [y_A[frame]]
        )

        # Masa
        masa.set_data(
            [x_M[frame]],
            [y_M[frame]]
        )

        # Resorte
        resorte.set_data(
            [x_A[frame], x_M[frame]],
            [y_A[frame], y_M[frame]]
        )

        return punto_A, masa, resorte

    animacion = FuncAnimation(
        fig,
        actualizar,
        frames=len(Phi),
        interval=20,
        blit=True
    )

    plt.show()

    return animacion