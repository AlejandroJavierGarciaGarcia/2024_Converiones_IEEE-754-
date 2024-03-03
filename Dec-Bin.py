#Función para pasar un número decimal a binario
#Estuardo Castro 23890

def entero_a_binario():
    num = int(input("Ingresa un número entero: "))
    if num >= 0 and num <= 255:
        binario = format(num, '08b')
        print(f"El número binario de 8 bits es: {binario}")
    else:
        print("El número debe estar en el rango de 0 a 255.")