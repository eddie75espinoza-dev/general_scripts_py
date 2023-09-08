def justificar_texto(texto, ancho):
    palabras = texto.split()
    lineas = []
    linea_actual = palabras[0]
    
    for palabra in palabras[1:]:
        if len(linea_actual) + len(palabra) + 1 <= ancho:
            linea_actual += " " + palabra + " "
        else:
            espacios_por_agregar = ancho - len(linea_actual)
            palabras_linea = linea_actual.split()
            if len(palabras_linea) == 1:
                linea_justificada = palabras_linea[0].ljust(ancho)
            else:
                espacios_entre_palabras = espacios_por_agregar // (len(palabras_linea) - 1)
                espacios_extra = espacios_por_agregar % (len(palabras_linea) - 1)
                linea_justificada = (" " * espacios_entre_palabras).join(palabras_linea)
                linea_justificada += " " * espacios_extra
            lineas.append(linea_justificada)
            linea_actual = palabra

    # Justificar la última línea (caso especial)
    ultima_linea_justificada = " ".join(linea_actual.split()).ljust(ancho)
    lineas.append(ultima_linea_justificada)
    
    # Justificar la primera línea (caso especial)
    primera_linea_justificada = lineas[0].ljust(ancho)
    lineas[0] = primera_linea_justificada
    
    texto_justificado = "\n".join(lineas)
    
    return texto_justificado


texto = "Con su pitido estridente, el tren salitre anuncia su paso y espera que el vigía autorice su avance. Don Rogelio gira el mecanismo que baja las barreras de protección y luego agita la bandera que autoriza la marcha del tren. Cual monstruo furioso, exudando agua y vapor caliente, asomó al tren salitrero. Cruzó el puente de El Colorado, cercano a mi casa, en donde con mis ojos de niño observó su marcha, extasiado. Aún suena en mis oídos su sonoro y repetido tra-ta-tra-ta-tra, brotando de sus ruedas pisando los rieles de la calle Ferrocarril. Sus carros vacíos traerán el oro blanco"
texto_justificado = justificar_texto(texto, 50)
print(texto_justificado)
