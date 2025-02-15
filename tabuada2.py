tabuada = 2 
contador = 1

while tabuada <= 10:
    print('')
    print("tabuada do", tabuada)
    print('')
    while contador <= 10:
        resultado = tabuada * contador
        print(tabuada,"x",contador,"=",resultado)
        contador+= 1
    tabuada += 1
    contador = 1