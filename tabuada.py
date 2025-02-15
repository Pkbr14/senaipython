#Tabuada

tabuada = 2
contador = 1
resultado = 0
#enquanto o resultado da tabuada não for 20 não pare p loop
 
while tabuada <= 10:
    resultado = tabuada * contador
    print(tabuada, "x",contador, "=",resultado)
    contador += 1

    if contador == 11:
        tabuada += 1
        contador = 1
        
       

       