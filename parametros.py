# parametros.py

import numpy as np

# PARÁMETROS

m = 0.1       # Masa que cuelga (kg)
R = 1          # Radio del aro (m)
k = 10        # Constante elástica del resorte (N/m)
l_nat = 0.5         # Longitud natural del resorte (m)
g = 9.81         # Aceleración de la gravedad (m/s^2)



# CONDICIONES INICIALES
#Como son EDOs de 2º orden, necesitaremos de condicion inicial y valor inicial
#para las variables y para sus derivadas


phi_0 = np.deg2rad(30)       # Ángulo inicial del aro
l_0 = 0.1                    # Longitud inicial del resorte

phi_dot_0 = 1              # Velocidad angular inicial de phi
l_dot_0 = 0                # Velocidad inicial de extensión


#Como vamos a trabajar con el sistema de EDOs en forma matricial, guardamos las 
#condiciones iniciales en un vector

E0 = np.array((
    phi_0,
    l_0,
    phi_dot_0,
    l_dot_0
))

#Esta parte del código se encarga de definir los "steps" de tiempo

t_inicial = 0.0
t_final = 20.0


t_eval = np.linspace(
    t_inicial,
    t_final,
    1000
)