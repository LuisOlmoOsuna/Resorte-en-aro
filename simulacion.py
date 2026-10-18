from scipy.integrate import solve_ivp

from parametros import E0, t_inicial, t_final, t_eval
from sistema import sistema


def simular():

    solucion = solve_ivp(
        sistema,
        (t_inicial, t_final),
        E0,
        t_eval=t_eval,
        method="RK45",
        rtol=1e-9,
        atol=1e-11
    )

    if not solucion.success:
        raise RuntimeError(
            f"Error durante la integración: {solucion.message}"
        )

    return solucion