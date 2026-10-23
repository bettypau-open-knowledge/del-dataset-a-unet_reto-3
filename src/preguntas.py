"""Banco de preguntas · Unidad 3: Procesamiento de imágenes y máscaras.
Índices de respuesta correcta: 0=A, 1=B, 2=C.
"""

def pregunta_1():
    """Pregunta 1 de la Unidad 3."""
    return {"titulo": 'Intensidades de una imagen RGB', "enunciado": 'Una imagen RGB de 640 × 480 píxeles, con 8 bits por canal, ¿cuántos valores de intensidad almacena sin considerar metadatos?', "opciones": ['307,200 valores.', '921,600 valores.', '2,457,600 valores.'], "correcta": 1}

def pregunta_2():
    """Pregunta 2 de la Unidad 3."""
    return {"titulo": 'Dimensiones de una imagen', "enunciado": 'Al leer una imagen RGB con NumPy, obtenemos un arreglo con `shape = (480, 640, 3)`. ¿Qué representa esta estructura?', "opciones": ['480 píxeles de ancho, 640 de alto y 3 canales.', '480 imágenes, cada una de 640 píxeles y 3 canales.', '480 píxeles de alto, 640 de ancho y 3 canales.'], "correcta": 2}

def pregunta_3():
    """Pregunta 3 de la Unidad 3."""
    return {"titulo": 'Convenciones HWC y CHW', "enunciado": '¿Cuál es la diferencia principal entre las convenciones HWC y CHW?', "opciones": ['HWC organiza las dimensiones como alto, ancho y canales; CHW como canales, alto y ancho.', 'HWC se utiliza exclusivamente para imágenes en escala de grises y CHW para imágenes RGB.', 'HWC almacena imágenes normalizadas y CHW imágenes sin normalizar.'], "correcta": 0}

def pregunta_4():
    """Pregunta 4 de la Unidad 3."""
    return {"titulo": 'Relación de aspecto', "enunciado": '¿Qué puede ocurrir al redimensionar directamente una imagen de 800 × 400 píxeles a 256 × 256 píxeles?', "opciones": ['La imagen conserva automáticamente su relación de aspecto.', 'La imagen puede deformarse porque cambia su relación de aspecto.', 'La imagen pierde necesariamente uno de sus canales de color.'], "correcta": 1}

def pregunta_5():
    """Pregunta 5 de la Unidad 3."""
    return {"titulo": 'Interpolación de máscaras', "enunciado": '¿Por qué se recomienda utilizar interpolación por vecino más cercano (nearest neighbor) al redimensionar máscaras categóricas?', "opciones": ['Porque permite suavizar los bordes generando valores intermedios.', 'Porque convierte automáticamente cualquier máscara en una máscara binaria.', 'Porque evita introducir valores de clase nuevos mediante la interpolación.'], "correcta": 2}

def pregunta_6():
    """Pregunta 6 de la Unidad 3."""
    return {"titulo": 'Escalado de intensidades', "enunciado": 'Una imagen tiene valores de intensidad entre 0 y 255 y tipo `uint8`. ¿Qué operación permite obtener valores entre 0 y 1 en `float32`?', "opciones": ['Convertir a `float32` y dividir entre 255.', 'Dividir entre 255 y convertir el resultado a `uint8`.', 'Multiplicar los valores por 255 y convertir a `float32`.'], "correcta": 0}

def pregunta_7():
    """Pregunta 7 de la Unidad 3."""
    return {"titulo": 'Máscara binaria 0/255', "enunciado": 'Una máscara binaria contiene valores 0 y 255. ¿Qué procedimiento permite convertirla a una representación con etiquetas 0 y 1?', "opciones": ['Aplicar interpolación bilineal.', 'Dividir entre 255 y convertir a un tipo entero adecuado.', 'Convertirla a RGB para obtener tres canales.'], "correcta": 1}

def pregunta_8():
    """Pregunta 8 de la Unidad 3."""
    return {"titulo": 'Trimaps de Oxford-IIIT Pet', "enunciado": 'En Oxford-IIIT Pet, las máscaras originales son trimaps que distinguen objeto, fondo y región de borde. ¿Qué debemos considerar al convertirlas a máscaras binarias?', "opciones": ['Definir explícitamente cómo se tratará la región de borde.', 'Eliminar todos los píxeles de fondo y conservar únicamente los de borde.', 'Aplicar normalización de intensidades para convertir automáticamente las tres clases en dos.'], "correcta": 0}

def pregunta_9():
    """Pregunta 9 de la Unidad 3."""
    return {"titulo": 'Visualización mediante overlays', "enunciado": '¿Cuál es la principal utilidad de superponer una máscara sobre su imagen original mediante un overlay?', "opciones": ['Incrementar automáticamente la resolución de la máscara.', 'Convertir una imagen RGB en escala de grises.', 'Comprobar visualmente que la región anotada corresponde espacialmente con el objeto.'], "correcta": 2}

def pregunta_10():
    """Pregunta 10 de la Unidad 3."""
    return {"titulo": 'Aumento de datos sincronizado', "enunciado": 'Durante el aumento de datos se aplica una rotación aleatoria a una imagen de entrenamiento. ¿Qué debe hacerse con su máscara de segmentación?', "opciones": ['Mantener la máscara original porque las etiquetas no deben modificarse.', 'Aplicar la misma transformación geométrica a la máscara, utilizando una interpolación apropiada para etiquetas.', 'Aplicar una rotación aleatoria independiente a la máscara para aumentar la diversidad.'], "correcta": 1}

PREGUNTAS = {
    1: pregunta_1,
    2: pregunta_2,
    3: pregunta_3,
    4: pregunta_4,
    5: pregunta_5,
    6: pregunta_6,
    7: pregunta_7,
    8: pregunta_8,
    9: pregunta_9,
    10: pregunta_10,
}
