# Ángel de Jesús Mérida Jiménez - 23661
# Función de conversión de binario a decimal

def binario_a_decimal():
    while True:
        binario = input("Por favor, ingresa un número binario de 8 bits: ")
        if not set(binario).issubset('01'):
            print("Error: El número binario solo puede contener 1s y 0s")
        elif len(binario) > 8:
            print("Error: El número binario no puede tener más de 8 bits")
        else:
            decimal = 0
            for digito in binario:
                decimal = decimal * 2 + int(digito)
            print("El número en decimal es el siguiente: ", decimal)
            return decimal




