import matplotlib.pyplot as plt

# Función para verificar si la entrada es un entero positivo
def es_entero_positivo(valor):
    try:
        entero = int(valor)
        if entero > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Mensaje de bienvenida
print("Laboratorio de Suma Acumulativa")

# Solicitar al usuario la cantidad de números a sumar
cantidad_numeros = input("Ingrese la cantidad de números que desea sumar: ")

# Verificar que la entrada sea un entero positivo
while not es_entero_positivo(cantidad_numeros):
    cantidad_numeros = input("Ingrese una cantidad válida de números (entero positivo): ")

cantidad_numeros = int(cantidad_numeros)

# Inicializar una lista para almacenar los números ingresados
numeros = []

# Solicitar al usuario que ingrese los números uno por uno
for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calcular la suma acumulativa
suma_acumulativa = []
acumulativo = 0
for numero in numeros:
    acumulativo += numero
    suma_acumulativa.append(acumulativo)

# Mostrar la suma acumulativa
print("Suma acumulativa:")
for i, suma in enumerate(suma_acumulativa):
    print(f"Para el número {i+1}, la suma acumulativa es: {suma}")

# Crear un gráfico de barras
plt.bar(range(1, cantidad_numeros+1), suma_acumulativa)
plt.xlabel("Número de entrada")
plt.ylabel("Suma acumulativa")
plt.title("Gráfico de Suma Acumulativa")
plt.show()