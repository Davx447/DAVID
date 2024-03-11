#Calcular el volumen de agua en la bañera despues de 2 horas
volumen_agua_bañera_litros = min(
    Capacidad_bañera_litros, Ritmo_llenado_litros_hora * Tiempo_horas)

#Verificar si el nivel del agua rebasa el limite de la bañera al agregar el volument de la persona
nivel_agua_con_persona_cm = (
    (volumen_agua_bañera_litros + Volumen_persona_litros) / Capacidad_bañera_litros) * Altura_bañera_cm

#Verificar si el nivel del agua con el sifon rebasa el limite de la bañera
if nivel_agua_con_persona_cm > Altura_sifon_cm:
    print("El agua rebasa el limite de la bañera")
else:
    print("Puedes ingresar a la bañera sin que el agua rebase el limite.")
