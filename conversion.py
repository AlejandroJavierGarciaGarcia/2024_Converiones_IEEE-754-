# Alejandro García - 231136
# Función de converión de binario IEEE 754 a decimal

def convertToIEE754(value):
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

    print(s, exp, frac)

# Convertir a decimal el binario en formato IEEE 754 2**-n
def convertFraction( frac):
    decimal = 0
    for i in range(len(frac)):
        est = -(i + 1)
        decimal += int(frac[i]) * (2 ** -(i + 1))
    return decimal
