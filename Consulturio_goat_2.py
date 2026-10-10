from collections import deque
from datetime import datetime

# ==========================================================
# Proyecto: Gestión de Citas - Consultorio Odontológico
# Autor: Daniel Garibello Escobar
# ==========================================================

# Inicio una lista vacía con los corchetes [] para guardar 
# todos los diccionarios con la información de cada paciente.
pacientes_consul = []

print("=" * 75)
print("  Bienvenido a Consultorio GOAT donde tu sonrisa es lo mas importante para nosotros")
print("=" * 75)

# Utilizo un ciclo while blindado para exigir un número entero mayor a 0
while True:
    try:
        registros = int(input("\n¿Cuántas citas vamos a ingresar hoy?: "))
        if registros > 0:
            break
        print("-> Error: Debe ingresar un número estrictamente mayor a 0.")
    except ValueError:
        print("-> Error: Ingrese un valor numérico entero válido.")

print("\n--- INICIANDO REGISTRO DE PACIENTES ---")

# Con un ciclo for recorro el número de registros que indicó el usuario
for i in range(registros):
    print(f"\n[Paciente #{i + 1} de {registros}]")
    
    # Capturo los datos básicos de identificación y contacto blindando contra cadenas vacías
    while True:
        cedula = input("Cédula del paciente: ").strip()
        if cedula:
            break
        print("-> Error: La cédula no puede estar vacía.")

    while True:
        nombre = input("Nombre y apellido: ").strip()
        if nombre:
            break
        print("-> Error: El nombre no puede estar vacío.")

    while True:
        telefono = input("Número de contacto: ").strip()
        if telefono:
            break
        print("-> Error: El número de contacto no puede estar vacío.")
    
    # Presento las opciones de cliente y blindo el rango válido entre 1 y 3
    while True:
        print("\n¿Qué tipo de cliente es?:")
        print("1 -> Particular")
        print("2 -> EPS")
        print("3 -> Prepagada")
        try:
            opcion_cliente = int(input("Selecciona tu opción: "))
            if opcion_cliente in [1, 2, 3]:
                break
            print("-> Error: Debe seleccionar una opción válida (1, 2 o 3).")
        except ValueError:
            print("-> Error: Ingrese un número de las opciones (1, 2 o 3).")
    
    if opcion_cliente == 1:
        tipo_cliente = "Particular"
    elif opcion_cliente == 2:
        tipo_cliente = "EPS"
    elif opcion_cliente == 3:
        tipo_cliente = "Prepagada"
        
    # Presento las opciones de atención y blindo el rango válido entre 1 y 4
    while True:
        print("\n¿Qué tipo de atención se va a realizar?:")
        print("1 -> Limpieza")
        print("2 -> Calzas")
        print("3 -> Extracción")
        print("4 -> Diagnóstico")
        try:
            opcion_atencion = int(input("Selecciona tu opción: "))
            if opcion_atencion in [1, 2, 3, 4]:
                break
            print("-> Error: Debe seleccionar una opción válida (1, 2, 3 o 4).")
        except ValueError:
            print("-> Error: Ingrese un número de las opciones (1, 2, 3 o 4).")
    
    if opcion_atencion == 1:
        tipo_atencion = "Limpieza"
    elif opcion_atencion == 2:
        tipo_atencion = "Calzas"
    elif opcion_atencion == 3:
        tipo_atencion = "Extracción"
    elif opcion_atencion == 4:
        tipo_atencion = "Diagnóstico"
        
    # Aplico la regla del negocio: para Limpieza o Diagnóstico, la cantidad se define en 1 automáticamente.
    if tipo_atencion in ["Limpieza", "Diagnóstico"]:
        cantidad = 1
        print("-> Nota: Para Limpieza o Diagnóstico la cantidad se establece automáticamente en 1.")
    else:
        # Utilizo un ciclo while blindado con try-except para exigir un entero mayor a 0
        while True:
            try:
                cantidad = int(input(f"¿Cuántas unidades para {tipo_atencion} (debe ser mayor a 0)?: "))
                if cantidad > 0:
                    break
                print("-> Error: La cantidad ingresada debe ser estrictamente mayor a 0. Intenta de nuevo.")
            except ValueError:
                print("-> Error: Por favor ingrese un número entero válido.")
        
    # Presento las opciones de prioridad y blindo la entrada para aceptar únicamente 1 o 2
    while True:
        print("\n¿Cuál es la prioridad de esta cita?:")
        print("1 -> Normal")
        print("2 -> Urgente")
        try:
            opcion_prioridad = int(input("Selecciona tu opción: "))
            if opcion_prioridad in [1, 2]:
                break
            print("-> Error: Debe seleccionar una opción válida (1 o 2).")
        except ValueError:
            print("-> Error: Ingrese un número (1 para Normal, 2 para Urgente).")
            
    prioridad = "Urgente" if opcion_prioridad == 2 else "Normal"
    
    # Valido mediante un ciclo que la fecha ingresada cumpla con el formato y convierto a datetime para poder ordenar luego
    while True:
        fecha_str = input("Fecha de la cita (Ej: DD/MM/AAAA): ").strip()
        try:
            fecha_dt = datetime.strptime(fecha_str, "%d/%m/%Y")
            break
        except ValueError:
            print("-> Error: Formato inválido. Asegúrate de usar el formato DD/MM/AAAA incluyendo las barras (/).")
    
    # Empaqueto los datos recolectados en un diccionario y dejo los montos en 0 para calcularlos después
    cita_actual = {
        'cedula': cedula,
        'nombre': nombre,
        'telefono': telefono,
        'tipo_cliente': tipo_cliente,
        'tipo_atencion': tipo_atencion,
        'cantidad': cantidad,
        'prioridad': prioridad,
        'fecha': fecha_dt,
        'fecha_str': fecha_str,
        'valor_atencion': 0, 
        'valor_pagar': 0      
    }
    
    # Almaceno el diccionario en mi lista principal
    pacientes_consul.append(cita_actual)

print("\n--- Procesando tarifas y calculando totales ---")

# ==========================================================
# Lógica de Cálculo y Tarifas
# ==========================================================

# Recorro la lista de pacientes para calcular el costo financiero de cada servicio
for paciente in pacientes_consul:
    # Extraigo los datos clave del diccionario para facilitar las operaciones lógicas
    t_cliente = paciente["tipo_cliente"]
    t_atencion = paciente["tipo_atencion"]
    cant = paciente["cantidad"]

    # 1. Defino el valor base de la cita según la categoría del cliente
    if t_cliente == "Particular":
        valor_cita_base = 80000
    elif t_cliente == "EPS":
        valor_cita_base = 5000
    elif t_cliente == "Prepagada":
        valor_cita_base = 30000
    else:
        valor_cita_base = 0

    # 2. Consulto la matriz de tarifas para determinar el valor unitario de la atención
    valor_atencion_unitario = 0

    if t_cliente == "Particular":
        if t_atencion == "Limpieza":
            valor_atencion_unitario = 60000
        elif t_atencion == "Calzas":
            valor_atencion_unitario = 80000
        elif t_atencion == "Extracción":
            valor_atencion_unitario = 100000
        elif t_atencion == "Diagnóstico":
            valor_atencion_unitario = 50000

    elif t_cliente == "EPS":
        if t_atencion == "Limpieza":
            valor_atencion_unitario = 0
        elif t_atencion == "Calzas":
            valor_atencion_unitario = 40000
        elif t_atencion == "Extracción":
            valor_atencion_unitario = 40000
        elif t_atencion == "Diagnóstico":
            valor_atencion_unitario = 0

    elif t_cliente == "Prepagada":
        if t_atencion == "Limpieza":
            valor_atencion_unitario = 0
        elif t_atencion == "Calzas":
            valor_atencion_unitario = 10000
        elif t_atencion == "Extracción":
            valor_atencion_unitario = 10000
        elif t_atencion == "Diagnóstico":
            valor_atencion_unitario = 0

    # 3. Calculo el total sumando la base y el costo unitario multiplicado por la cantidad
    total_pagar = valor_cita_base + (valor_atencion_unitario * cant)

    # Actualizo los campos del diccionario con los valores reales obtenidos
    paciente["valor_atencion"] = valor_atencion_unitario
    paciente["valor_pagar"] = total_pagar


# ==========================================================
# Plan de Contingencia: Pila de Extracciones Urgentes
# ==========================================================

# Creo la Pila vacía utilizando deque para manejar la contingencia
pila_contingencia = deque()

# Filtro los pacientes que vienen a extracción y son de prioridad urgente
pacientes_contingencia = [
    p for p in pacientes_consul 
    if p["tipo_atencion"] == "Extracción" and p["prioridad"] == "Urgente"
]

# Ordeno de la fecha más lejana a la más cercana para que al hacer pop() 
# me salgan primero los de la fecha más cercana (cumpliendo la lógica LIFO de la Pila)
pacientes_contingencia.sort(key=lambda x: x["fecha"], reverse=True)

# Apilo los clientes filtrados
for p in pacientes_contingencia:
    pila_contingencia.append(p)

print("\n" + "=" * 50)
print("   INFORME DE PILA - PLAN DE CONTINGENCIA URGENTE")
print("=" * 50)

if not pila_contingencia:
    print("No hay pacientes registrados para el plan de contingencia de extracción urgente.")
else:
    # Vacio la Pila con pop() para ir desapilando los pacientes en orden
    contador_pila = 1
    while len(pila_contingencia) > 0:
        paciente_pila = pila_contingencia.pop()
        print(
            f"Llamado #{contador_pila}: {paciente_pila['nombre']} | "
            f"Cédula: {paciente_pila['cedula']} | Fecha: {paciente_pila['fecha_str']} | "
            f"Teléfono: {paciente_pila['telefono']}"
        )
        contador_pila += 1


# ==========================================================
# Gestión de la Agenda Diaria: Cola de Atención
# ==========================================================

# Creo la Cola vacía utilizando deque para la atención diaria en orden de agenda
cola_atencion = deque()

# Ordeno todos los pacientes registrados por fecha de cita (de la más cercana a la más lejana)
pacientes_agenda = sorted(pacientes_consul, key=lambda x: x["fecha"])

# Encolo los registros respetando el orden estricto de la agenda
for p in pacientes_agenda:
    cola_atencion.append(p)

print("\n" + "=" * 50)
print("      GESTIÓN DE ATENCIÓN DIARIA - COLA DE CITAS")
print("=" * 50)

# Vacio la Cola con popleft() para ir atendiendo según el principio FIFO (primero en llegar/agendado, primero en ser atendido)
contador_cola = 1
while len(cola_atencion) > 0:
    paciente_cola = cola_atencion.popleft()
    print(
        f"Atendiendo Turno #{contador_cola}: {paciente_cola['nombre']} | "
        f"Servicio: {paciente_cola['tipo_atencion']} | Prioridad: {paciente_cola['prioridad']} | "
        f"Fecha: {paciente_cola['fecha_str']}"
    )
    contador_cola += 1


# ==========================================================
# Generación de Reportes
# ==========================================================

# Obtengo el total de clientes utilizando la función len() sobre la lista
total_clientes = len(pacientes_consul)

# Sumo los ingresos totales aplicando una comprensión de listas
ingresos_totales = sum(p["valor_pagar"] for p in pacientes_consul)

# Cuento cuántos registros requieren el servicio de extracción
num_extracciones = sum(
    1 for p in pacientes_consul if p["tipo_atencion"] == "Extracción"
)

print("\n" + "=" * 50)
print("            REPORTE GENERAL DEL CONSULTORIO")
print("=" * 50)
print(f"1. Total de clientes registrados: {total_clientes}")
print(f"2. Ingresos totales recibidos: ${ingresos_totales:,.0f}")
print(f"3. Número de clientes para extracción de dientes: {num_extracciones}")
print("=" * 50)


# ==========================================================
# Ordenamiento y Módulo de Búsqueda
# ==========================================================

# Ordeno la lista enfocándome en la llave 'valor_atencion' de mayor a menor,
# cumpliendo con el criterio solicitado en la actividad.
pacientes_ordenados = sorted(
    pacientes_consul, 
    key=lambda x: x["valor_atencion"], 
    reverse=True
)

print("\n--- Lista de clientes ordenada por el valor de la atención (De Mayor a Menor) ---")
for p in pacientes_ordenados:
    print(
        f"- {p['nombre']} | Cédula: {p['cedula']} | Servicio: {p['tipo_atencion']}"
        f" | Valor Atención: ${p['valor_atencion']:,.0f} | Total a Pagar: ${p['valor_pagar']:,.0f}"
    )

# Implemento un ciclo while para permitir múltiples consultas por cédula de forma fluida
print("\n--- Búsqueda ---")
buscando = True

while buscando:
    cedula_buscar = input("Ingrese la cédula del paciente a buscar: ").strip()

    # Utilizo una variable de control para verificar si el registro existe
    encontrado = None
    for p in pacientes_ordenados:
        if p["cedula"] == cedula_buscar:
            encontrado = p
            break # Interrumpo el ciclo al hallar la coincidencia

    # Si encuentro el registro, despliego la información detallada
    if encontrado:
        print("\n¡Registro encontrado exitosamente!")
        print(f"   * Nombre: {encontrado['nombre']}")
        print(f"   * Teléfono: {encontrado['telefono']}")
        print(f"   * Tipo de Cliente: {encontrado['tipo_cliente']}")
        print(f"   * Atención: {encontrado['tipo_atencion']}")
        print(f"   * Cantidad: {encontrado['cantidad']}")
        print(f"   * Prioridad: {encontrado['prioridad']}")
        print(f"   * Fecha de la cita: {encontrado['fecha_str']}")
        print(f"   * Valor de la atención: ${encontrado['valor_atencion']:,.0f}")
        print(f"   * Valor total a pagar: ${encontrado['valor_pagar']:,.0f}")
        
        buscando = False
    else:
        print("\nNo se encontró ningún registro asociado a esa cédula.")
        
        # Doy la opción de reintentar la búsqueda o salir del módulo
        opcion_salida = input("¿Desea intentar con otra cédula? (s/n): ").lower().strip()
        if opcion_salida != 's':
            print("\nSaliendo del módulo de búsqueda.")
            buscando = False