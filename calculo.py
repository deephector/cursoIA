import numpy as np
import pandas as pd

def f(x):
    return np.sqrt(x + 2)



x = np.array([-2, -1, 0, 2, 4, 6])  # Creando el vector de valores de x
y = f(x)
y

tabla = pd.DataFrame( list(zip(x, y)), columns=['x', 'f(x)'] )
tabla

print(tabla)

#prueba github

print("he hecho un cambo al codigo")

print("Nuevo cambio, solo por praticar git")