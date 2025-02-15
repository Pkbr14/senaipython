#montar um programa com um loope que  fique pedindo para  digitar a senha correta ate que a a pessoa digite a senha correta
senha = "abcd1234"
password = input("coloque a senha: ")


while password != senha:
     password = input("digite a senha: ")
     print("senha correta!!")
     if password != senha:
         print("senha invalida")


      
