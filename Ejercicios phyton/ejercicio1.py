# Ejercicio 1: Calculadora simple

# Instrucciones:
# - Pedir al usuario el primer número.
# - Pedir al usuario el segundo número.
# - Preguntar qué operación desea realizar (+, -, *, /).
# - Mostrar el resultado con el mensaje: "El resultado es: "

# Tu código aquí:

# Solicitar el primer número:
n1 = float(input("Ingrese un primer número: "))


# Solicitar el segundo número:
n2 = float(input("Ingrese el segundo número: "))


# Pedir la operación a realizar:
operación = input ("Ingrese que operación desea realizar(+,-,*,/): ")


# Calcular el resultado según la operación:
if operación == "+":
    resultado = n1 + n2
elif operación == "-":
    resultado = n1 - n2
elif operación == "*":
    resultado = n1 * n2
elif operación == "/":
    if n2 != 0:
        resultado = n1 / n2
    else: print("No es posible dividir entre cero")

print("La operación no es válida")
# Mostrar el resultado:
# print("El resultado es:", ...)
print("El resultado es:", resultado)