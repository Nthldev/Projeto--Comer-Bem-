import csv

# Abra o arquivo CSV
with open('culinarias_data.csv', encoding='utf-8') as csvfile:
    # Leia o arquivo CSV usando DictReader
    reader = csv.DictReader(csvfile)
    
    # Crie um dicionário vazio para armazenar os dados
    restaurantes = {}
    
    # Itere sobre cada linha do arquivo CSV
    for row in reader:
        # Obtenha o valor da coluna 'culinarias'
        culinaria = row['culinarias']
        
        # Se a culinária ainda não estiver no dicionário, crie uma nova lista vazia
        if culinaria not in restaurantes:
            restaurantes[culinaria] = []
        
        # Adicione um novo dicionário à lista para esta culinária
        restaurantes[culinaria].append({
            'nome': row['nome'],
            'endereço': row['endereço'],
            'telefone': row['telefone'],
            'avaliação': row['avaliação']
        })

# Imprima o dicionário resultante
#print(restaurantes)

def restaurantes_porlinha(dicionario):
    for culinaria in dicionario:
        print(culinaria)
        for item in dicionario[culinaria]:
            print (item)

#restaurantes_porlinha(restaurantes)
