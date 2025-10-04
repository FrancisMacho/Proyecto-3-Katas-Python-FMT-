import math
from functools import reduce
from collections import Counter

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva 
# un diccionario con las frecuencias de cada letra en la cadena. Los espacios no 
# deben ser considerados.
def frecuencia_letras(cadena):
    """Calcula la frecuencia de cada letra en una cadena, ignorando espacios."""
    cadena_limpia = cadena.lower().replace(" ", "")
    return dict(Counter(cadena_limpia))

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
# Usa la función map().
def doble_valores(lista_numeros):
    """Devuelve una nueva lista con el doble de cada valor usando map()."""
    return list(map(lambda x: x * 2, lista_numeros))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como 
# parámetros. La función debe devolver una lista con todas las palabras de la 
# lista original que contengan la palabra objetivo.
def filtrar_palabras(lista_palabras, objetivo):
    """Filtra palabras que contienen el objetivo, insensible a mayúsculas."""
    objetivo_lower = objetivo.lower()
    return [
        palabra for palabra in lista_palabras 
        if objetivo_lower in palabra.lower()
    ]

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. 
# Usa la función map().
def diferencia_listas(lista1, lista2):
    """Calcula la diferencia (lista1[i] - lista2[i]) entre los valores de dos listas."""
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud.")
    return list(map(lambda par: par[0] - par[1], zip(lista1, lista2)))

# 5. Escribe una función que tome una lista de números como parámetro y un valor 
# opcional nota_aprobado (por defecto 5). La función debe calcular la media de 
# los números en la lista y determinar si la media es mayor o igual que 
# nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, 
# "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_media(numeros, nota_aprobado=5):
    """Calcula la media de una lista de números y determina el estado de aprobación."""
    if not numeros:
        return (0, "Lista vacía")
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial_recursivo(n):
    """Calcula el factorial de n (n!) de forma recursiva."""
    if n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. 
# Usa la función map().
def tuplas_a_strings(lista_tuplas):
    """Convierte una lista de tuplas a una lista de strings usando map()."""
    return list(map(lambda t: "".join(map(str, t)), lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si 
# el usuario ingresa un valor no numérico o intenta dividir por cero, maneja 
# esas excepciones de manera adecuada y muestra un mensaje indicando si la 
# división fue exitosa o no.
def division_con_manejo_errores(num1_str, num2_str):
    """Intenta dividir dos números, manejando ValueError y ZeroDivisionError."""
    exito = False
    resultado = "Error: Fallo en la operación."
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        resultado = f"Resultado: {num1 / num2}"
        exito = True
    except ValueError:
        resultado = "Error: Al menos uno de los valores no es un número válido."
    except ZeroDivisionError:
        resultado = "Error: No se puede dividir por cero."
    finally:
        # Se requiere devolver/mostrar el mensaje de éxito/fallo. Lo devolvemos junto al resultado
        return f"{resultado}. La operación fue {'exitosa' if exito else 'fallida'}."

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro 
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", 
# "Cocodrilo", "Oso"]. Usa la función filter().
def filtrar_mascotas(lista_mascotas):
    """Filtra una lista de mascotas excluyendo las prohibidas."""
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    prohibidas_lower = {m.lower() for m in mascotas_prohibidas}
    return list(filter(lambda mascota: mascota.lower() not in prohibidas_lower, lista_mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si 
# la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    """Excepción personalizada para cuando la lista de promedio está vacía."""
    def __init__(self, mensaje="La lista no puede estar vacía para calcular el promedio."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def calcular_promedio_con_excepcion(numeros):
    """Calcula el promedio de una lista o lanza una excepción si está vacía."""
    if not numeros:
        raise ListaVaciaError()
    return sum(numeros) / len(numeros)

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario 
# ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, 
# menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def validar_edad(edad_str):
    """Valida la edad como número entero dentro del rango [0, 120]."""
    try:
        edad = int(edad_str)
        if not 0 <= edad <= 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        return f"Edad ingresada correctamente: {edad}", True
    except ValueError as e:
        return f"Error en la entrada: {e}", False
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}", False

# 12. Genera una función que, al recibir una frase, devuelva una lista con la 
# longitud de cada palabra. Usa la función map().
def longitud_palabras(frase):
    """Devuelve la longitud de cada palabra en una frase usando map()."""
    palabras = frase.split()
    return list(map(len, palabras))

# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de 
# tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar 
# repetidas. Usa la función map().
def mayusculas_minusculas(caracteres):
    """Devuelve una lista de tuplas (MAYÚS, minús) para un conjunto de letras sin repetir."""
    letras_unicas = list(set(c.upper() for c in caracteres if c.isalpha()))
    return list(map(lambda c: (c, c.lower()), letras_unicas))

# 14. Crea una función que retorne las palabras de una lista que comiencen con una 
# letra en específico. Usa la función filter().
def palabras_que_comienzan_con(lista_palabras, letra):
    """Filtra palabras que comienzan con una letra específica, insensible a mayúsculas."""
    letra_lower = letra.lower()
    return list(filter(lambda p: p.lower().startswith(letra_lower), lista_palabras))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres_lambda = lambda x: x + 3

# 16. Escribe una función que tome una cadena de texto y un número entero n como 
# parámetros y devuelva una lista de todas las palabras que sean más largas que n. 
# Usa la función filter().
def palabras_mas_largas(cadena_texto, n):
    """Devuelve palabras de la cadena con longitud mayor a n usando filter()."""
    palabras = cadena_texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# 17. Crea una función que tome una lista de dígitos y devuelva el número 
# correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
def lista_a_numero(lista_digitos):
    """Convierte una lista de dígitos a un número entero usando reduce()."""
    return reduce(lambda acc, dig: acc * 10 + dig, lista_digitos)

# 18. Escribe un programa en Python que cree una lista de diccionarios con 
# información de estudiantes (nombre, edad, calificación) y use filter para 
# extraer a los estudiantes con una calificación mayor o igual a 90.
def filtrar_estudiantes_por_calificacion(estudiantes):
    """Filtra estudiantes con calificación >= 90 usando filter()."""
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# 19. Crea una función lambda que filtre los números impares de una lista dada.
es_impar_lambda = lambda x: x % 2 != 0

# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista 
# solo con los valores int. Usa la función filter().
def filtrar_solo_int(lista_mixta):
    """Devuelve solo los elementos de tipo int usando filter()."""
    return list(filter(lambda x: isinstance(x, int), lista_mixta))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
calcular_cubo_lambda = lambda x: x ** 3

# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la 
# función reduce().
def producto_total(lista_numerica):
    """Calcula el producto total de los valores de una lista usando reduce()."""
    return reduce(lambda acc, num: acc * num, lista_numerica, 1)

# 23. Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(lista_palabras):
    """Concatena una lista de palabras en una sola cadena (separada por espacios) usando reduce()."""
    return reduce(lambda acc, palabra: f"{acc} {palabra}".strip(), lista_palabras, "")

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
def diferencia_total(lista_numerica):
    """Calcula la diferencia total (num1 - num2 - num3...) usando reduce()."""
    if not lista_numerica:
        return 0
    return reduce(lambda acc, num: acc - num, lista_numerica[1:], lista_numerica[0])

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    """Cuenta el número de caracteres en una cadena."""
    return len(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
calcular_resto_lambda = lambda a, b: a % b

# 27. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def encontrar_primer_duplicado(lista):
    """Encuentra y devuelve el primer elemento que se repite en la lista."""
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare 
# todos los caracteres con el carácter '#' excepto los últimos cuatro.
def enmascarar_variable(variable):
    """Convierte la variable a string y enmascara los caracteres excepto los últimos 4."""
    cadena = str(variable)
    longitud = len(cadena)
    
    if longitud <= 4:
        return cadena
    else:
        return '#' * (longitud - 4) + cadena[-4:]

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si 
# están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    """Determina si dos palabras son anagramas."""
    p1_limpia = palabra1.lower().replace(" ", "")
    p2_limpia = palabra2.lower().replace(" ", "")
    
    return sorted(p1_limpia) == sorted(p2_limpia)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego 
# un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un 
# mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
class NombreNoEncontradoError(Exception):
    """Excepción para cuando un nombre no se encuentra en la lista."""
    pass

def buscar_nombre_con_excepcion(nombres_lista, nombre_a_buscar):
    """Busca un nombre y lanza una excepción si no se encuentra."""
    nombre_buscado = nombre_a_buscar.strip()
    
    if nombre_buscado in nombres_lista:
        return f"Éxito: El nombre '{nombre_buscado}' fue encontrado."
    else:
        raise NombreNoEncontradoError(f"Error: El nombre '{nombre_buscado}' no fue encontrado.")

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque 
# el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo 
# contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_puesto_empleado(nombre_completo, lista_empleados):
    """Busca el nombre en la lista de empleados y devuelve su puesto."""
    nombre_buscado = nombre_completo.strip().lower()
    
    for empleado in lista_empleados:
        if empleado.get('nombre', '').strip().lower() == nombre_buscado:
            return empleado.get('puesto', 'Puesto no especificado')
            
    return f"Mensaje: La persona '{nombre_completo}' no trabaja aquí."

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_correspondientes_lambda = lambda lista1, lista2: list(map(lambda par: par[0] + par[1], zip(lista1, lista2)))

# 34. Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
class Arbol:
    """Representa un árbol genérico con un tronco y ramas."""

    def __init__(self):
        self.longitud_tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.longitud_tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina una rama en una posición específica (índice)."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            # Se permite mantener este tipo de print/manejo de error si es parte del diseño de la función
            pass

    def info_arbol(self):
        """Devuelve información sobre el árbol."""
        return {
            "Longitud Tronco": self.longitud_tronco,
            "Número de Ramas": len(self.ramas),
            "Longitudes de Ramas": self.ramas
        }

# 35. Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
class UsuarioBanco:
    """Representa un usuario de banco con métodos de gestión de saldo."""

    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Sustrae dinero del saldo, lanzando un error si no es posible."""
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if self.saldo < cantidad:
            raise ValueError(f"Saldo insuficiente ({self.nombre}). Saldo actual: {self.saldo}")
        
        self.saldo -= cantidad
        return f"Retiro de {cantidad} exitoso. Nuevo saldo de {self.nombre}: {self.saldo}"

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero DESDE otro_usuario HACIA self."""
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        
        if otro_usuario.saldo < cantidad:
            raise ValueError(f"Transferencia fallida: Saldo insuficiente en la cuenta de {otro_usuario.nombre}. Saldo: {otro_usuario.saldo}")
        
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        return f"Transferencia de {cantidad} de {otro_usuario.nombre} a {self.nombre} exitosa."

    def agregar_dinero(self, cantidad):
        """Aumenta el saldo del usuario."""
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        
        self.saldo += cantidad
        return f"Agregado {cantidad}. Nuevo saldo de {self.nombre}: {self.saldo}"

# 36. Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
def procesar_texto(texto, opcion, *args):
    """Procesa un texto según la opción elegida."""
    opcion_lower = opcion.lower()
    
    if opcion_lower == "contar":
        frecuencias = {}
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum() or c.isspace())
        palabras = texto_limpio.split()
        for palabra in palabras:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        return frecuencias
    
    elif opcion_lower == "reemplazar":
        if len(args) != 2:
            return "Error: 'reemplazar' requiere palabra_original y palabra_nueva."
        return texto.replace(args[0], args[1])
    
    elif opcion_lower == "eliminar":
        if len(args) != 1:
            return "Error: 'eliminar' requiere la palabra a eliminar."
        palabras = texto.split()
        texto_filtrado = " ".join([p for p in palabras if p != args[0]])
        return texto_filtrado
    
    else:
        return f"Error: Opción '{opcion}' no válida."

# 37. Genera un programa que nos indique si es de noche, de día o de tarde según 
# la hora proporcionada por el usuario.
def determinar_franja_horaria(hora):
    """Indica si es de noche, de día o de tarde según la hora ingresada."""
    try:
        hora = int(hora)
        if not 0 <= hora <= 23:
            return "Error: Hora fuera de rango (0-23)."
            
        if 7 <= hora < 13:
            franja = "de día (Mañana)"
        elif 13 <= hora < 20:
            franja = "de tarde"
        else: # 20:00 a 6:59
            franja = "de noche"
            
        return f"Son las {hora}:00, la franja horaria es: {franja}"

    except ValueError:
        return "Error: Entrada no válida. La hora debe ser un número entero."

# 38. Escribe un programa que determine qué calificación en texto tiene un alumno 
# según su calificación numérica.
# Reglas: 0-69: insuficiente, 70-79: bien, 80-89: muy bien, 90-100: excelente
def obtener_calificacion_texto(nota):
    """Devuelve la calificación textual según la nota numérica [0-100]."""
    if not 0 <= nota <= 100:
        return "Nota fuera de rango (0-100)"
    
    if nota >= 90:
        return "excelente"
    elif nota >= 80:
        return "muy bien"
    elif nota >= 70:
        return "bien"
    else:
        return "insuficiente"

# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser 
# "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos 
# necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    """Calcula el área de una figura geométrica dada su tipo y datos."""
    figura = figura.lower()
    
    if figura == "rectangulo":
        if len(datos) != 2: return "Error: Rectángulo requiere (base, altura)."
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        if len(datos) != 1: return "Error: Círculo requiere (radio)."
        radio = datos[0]
        return math.pi * (radio ** 2)
        
    elif figura == "triangulo":
        if len(datos) != 2: return "Error: Triángulo requiere (base, altura)."
        base, altura = datos
        return (base * altura) / 2
        
    else:
        return f"Error: Figura '{figura}' no soportada."

# 40. Escribe un programa en Python que utilice condicionales para determinar el 
# monto final de una compra en una tienda en línea, después de aplicar un 
# descuento.
def calcular_monto_final(precio_original, valor_cupon=0):
    """Calcula el precio final aplicando un descuento condicional."""
    if precio_original <= 0:
        return {"Error": "El precio original debe ser positivo."}
        
    monto_final = precio_original
    descuento_aplicado = 0
    
    if 0 < valor_cupon <= 100:
        descuento_aplicado = (precio_original * valor_cupon) / 100
        monto_final = precio_original - descuento_aplicado
        
    return {
        "Precio Original": precio_original,
        "Valor Cupón (%)": valor_cupon,
        "Descuento Aplicado": descuento_aplicado,
        "Precio Final": monto_final
    }