import numpy as np

from parametros import m, R, k, l_nat, g


def sistema(t, E):

    #Sacamos todas las variables del vector E
    Phi, l, Phi_dot, l_dot = E

    # Ecuaciones del movimiento
    Phi_ddot = -(2 * l_dot * Phi_dot + g * np.cos(Phi)) / (R + l)

    l_ddot = (
        (R + l) * Phi_dot**2
        - g * np.sin(Phi)
        - (k / m) * (l - l_nat)
    )

    # Derivada del vector de estado
    dE_dt = np.array([
        Phi_dot,
        l_dot,
        Phi_ddot,
        l_ddot
    ])

    return dE_dt