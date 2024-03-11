import math

leones_zoo = 23
Cuidadores_Leones = 10

Cuidadores_Requeridos = math.ceil(leones_zoo / 2)
print("Numero de cuidadores requeridos:", Cuidadores_Requeridos)

Cumple_norma = Cuidadores_Leones >= Cuidadores_Requeridos
print("¿Cumple con la norma?:", Cumple_norma)
