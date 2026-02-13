print("Bem vindo ao cadastro")
cadastros = int(input("Quantos cadastros?"))

for i in range(cadastros):
    usuario = (input("Digite seu nome:"))
    idade = int(input("Digite sua idade:"))

    if idade >= 18:
        print("Boa, maior de idade já")
        print("O", usuario,"tem", idade, "anos, sendo maior de idade")

    else:
        print("Ainda não")
        print("O", usuario, "tem", idade, "anos, sendo menor de idade") 




