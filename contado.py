limite = 101
contador = 0
sair= False # true ou false
while sair == False:
    print("contando. ", contador)
    contador += 1
    resposta = input("Desejar parar o contador? S/N: ")
    if (resposta.upper() == "N"):
        sair = False
    else:
        sair = True
        
print("final da contagem !!!")