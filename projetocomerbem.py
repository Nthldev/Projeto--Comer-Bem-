from data import *

print("Bem vindo ao Comer Bem!")
print("O app com a seleção dos melhores restaurantes do Rio.")

def mostrar_opcoes_culinaria():
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "W", "Y", "Z"]
    letra = input("Digite a letra inicial da culinária desejada: ").upper()
    if letra in alfabeto:
        opcoes = [culinaria for culinaria in restaurantes if culinaria.startswith(letra)]
        if len(opcoes) < 1:
            print("\nPerdão, não temos nenhuma culinária iniciando com esta letra\n")
            mostrar_opcoes_culinaria()
        else:
            print("Opções de culinárias disponíveis:")
            for opcao in opcoes:
                print(opcao)
    else:
        print("Perdão, não reconheço a letra digitada")
        mostrar_opcoes_culinaria()

def mostrar_restaurantes(culinaria):
    if culinaria in restaurantes:
        print()
        print(f"Restaurantes de culinária {culinaria}:")
        print()
        for restaurante in restaurantes[culinaria]:
            print(f"Nome: {restaurante['nome']}")
            print(f"Endereço: {restaurante['endereço']}")
            print(f"Telefone: {restaurante['telefone']}")
            print(f"Avaliação: {restaurante['avaliação']}")
            print()
    else:
        print(f"Nenhum restaurante encontrado para a culinária {culinaria}")

def programa_comer_bem():
    while True:
        mostrar_opcoes_culinaria()
        culinaria_escolhida = input("Escolha uma das opções de culinária (inclua os acentos): ").title()
        mostrar_restaurantes(culinaria_escolhida)
        repetir = input("Deseja realizar uma nova busca? Digite 's' para sim ou 'n' para encerrar: ").lower()
        if repetir == "n":
            print("Encerrando programa..Volte sempre!")
            break
        elif repetir != "s":
            print("Perdão, não entendi sua resposta. Seguem novamente as opções culinárias.")

# Inicializa o programa
programa_comer_bem()