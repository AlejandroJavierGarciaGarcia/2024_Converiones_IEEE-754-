def FloatToBinary():
    S = ""
    EXP = ""
    Frac = ""

    Float = input()

    # separa el signo
    if (Float.startswith("-")):
        S = "1"
    else:
        S = "0"

    # verifica que el número es un decimal
    try:
        Float = abs(float(Float))
    except:
        return "* Error. No es un decimal representable"

    zeros = 0
    Int = int(Float) # Se puede usar la función de decimal a binario aquí
    if Int == 0:
        zerosindecimal= True
        zeros += 1
    else:
        zerosindecimal = False
    Int = str(format(Int, "b"))

    # convierte el decimal a binario
    decimal = ""
    quotient = Float - int(Float)
    zerosafter126 = 0
    while quotient > 0 and len(decimal) + len(Int) - 1 + zerosafter126 - zeros < 23:
        quotient *= 2
        if (quotient >= 1):
            decimal += "1"
            quotient -= 1
            zerosindecimal = False
        else:
            decimal += "0"
            if zerosindecimal:
                zeros += 1
                if zeros > 126:
                    zerosafter126 += 1


    
    #print(Int + "." + decimal)

    # Construye el exponente
    if zeros > 0:
        exp = 127 - zeros
        if (exp < 0):
            exp = 0
    else:
        exp = len(Int) - 1 + 127
        if exp >= 255:
            exp = 255
            print( "∞ infinity")

    exp = str(format(exp, "b"))
    for i in range(8 - len(exp)):
        EXP += "0"

    EXP += exp

    # Construye la fracción
    frac = Int + decimal
    if zeros > 0:
        frac = frac.partition("0" * (zeros - zerosafter126))[2]
        for i in range(23):
            if i >= len(frac) - 1:
                Frac += "0"
            else:
                Frac += frac[i +  1]
    else:
        for i in range(23):
            if i >= len(frac) - 1:
                Frac += "0"
            else:
                Frac += frac[i + 1]

        if Float >= 2**129 - 2**105:
            Frac = "1"*23

    if EXP.find("1") == -1 and Frac.find("1") == -1:
        print("0 empty")
    
    return S + " " + EXP + " " + Frac
    



    
    

    
    
