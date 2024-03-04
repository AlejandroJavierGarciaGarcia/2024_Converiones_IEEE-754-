

#Función para pasar un número decimal a binario
#Estuardo Castro 23890
def entero_a_binario():
    num = int(input("\n * Ingresa un número entero: "))
    if num >= 0 and num <= 255:
        binario = format(num, '08b')
        print(f"   -El número binario de 8 bits es: {binario}")
    else:
        print("El número debe estar en el rango de 0 a 255.")

# Ángel de Jesús Mérida Jiménez - 23661
# Función de conversión de binario a decimal
def binario_a_decimal():
    while True:
        binario = input(" \n * Igresa un número binario de 8 bits: ")
        if not set(binario).issubset('01'):
            print(" * Error: El número binario solo puede contener 1s y 0s")
        elif len(binario) > 8:
            print(" * Error: El número binario no puede tener más de 8 bits")
        else:
            decimal = 0
            for digito in binario:
                decimal = decimal * 2 + int(digito)
            print("  - El número en decimal es el siguiente: ", decimal)
            return decimal
        
#Fucnión para convertir de IEE754 a dcimal
def convertToIEE754():
    print("\nIngrese el bit más significativo del número (Signo)")
    s = input()

    while len(s) != 1 or (s != '0' and s != '1'):
        print("  *Error: La entrada debe ser un único carácter '0' o '1'")
        s = input()

    print("\nIngrese los 8 bits correspondientes al exponente en IEEE 754")
    exp = input()

    # Verifica que la entrada no esté vacía y que sea '0' o '1'
    while len(exp) > 8 or not exp.isdigit() or not (all(bit == '0' or bit == '1' for bit in exp)):
        print("  * Error: La entrada debe tener hasta 8 caracteres y ser '0' o '1'")
        exp = input()
    exp = '0' * (8 - len(exp)) + exp

    print("\nIngrese los bits correspondientes a la fracción en IEEE 754")
    frac = input()

    # Verifica que la entrada no esté vacía y que sea '0' o '1'
    while len(frac) > 23 or not frac.isdigit() or not (all(bit == '0' or bit == '1' for bit in frac)):
        print(" * Error: La entrada debe tener hasta 23 caracteres y ser '0' o '1'")
        frac = input()
    frac = frac + '0' * (23 - len(frac))

    fraccion = convertFraction(frac)
    exponente = int(exp, 2)
    print(" -Número ingresado",s,exp,frac)
    print(exponente)
    print(fraccion)
    if(exponente == 0):
        resultado = (-1**int(s))*(2**(-126))*(fraccion)
    elif(exponente>254):
        if(s=="0"):
            resultado = "+ ∞"
        else:
            resultado = "- ∞"
    else:
        resultado = ((-1) ** int(s))*(2**(exponente-127))*(1+fraccion)

    print(" * El número en decimal es:",resultado)

# Convertir a decimal el binario en formato IEEE 754 2**-n
def convertFraction( frac):
    decimal = 0
    for i in range(len(frac)):
        est = -(i + 1)
        decimal += int(frac[i]) * (2 ** -(i + 1))
    return decimal


print("CONVERSIONES - HOJA DE TRABAJO 5")
while True:
    print("\n - MENÚ - ")
    print("  1. Decimal a binario")
    print("  2. Binario a decimal")
    print("  3. Decimal a Binario IEEE 754")
    print("  4. Binario IEEE 754 a Decimal")
    print("  5. Salir")

    opcion = input("Ingrese el número de opción que desea realizar: ")
    if opcion == '1':
        entero_a_binario()

    elif opcion == '2':
        binario_a_decimal()

    elif opcion == '3':
        decimal = float(input("Ingrese el número decimal que desea convertir a binario IEEE 754: "))
        # Implementación para convertir decimal a binario IEEE 754
        resultado = bin(decimal)
        print("El resultado es:", resultado)
    elif opcion == '4':
        convertToIEE754()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
