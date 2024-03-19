

# Programa para imprimir números pares del 1 al 20 usando bucle while

numero = 1  # Inicializar variable con el primer número

while numero <= 20:
    # Verificar si el número es par (residuo de la división por 2 es cero)
    if numero % 2 == 0:
        print(numero)
    numero += 1  # Incrementar el número en 1 para la siguiente iteración
