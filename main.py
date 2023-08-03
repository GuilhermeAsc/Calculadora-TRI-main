# Calculadora que faz a média do TRI ENEM
# Boa sorte a todos os alunos!!!
# Feito para Júlia Anelli :)

#By  asC-_

# Função para validar a nota e garantir que esteja entre 0 e 1000
def validar_nota(nota_str):
    nota = float(nota_str)
    while nota < 0 or nota > 1000:
        print("Por favor, insira uma nota válida!")
        nota = float(input("Digite a nota (0 a 1000): "))
    return nota

# Função para calcular a média do TRI ENEM de acordo com a universidade
def calcular_media_tri_enem(pesos, notas):
    soma_das_notas = sum(peso * nota for peso, nota in zip(pesos, notas))
    return soma_das_notas / sum(pesos)

# Dicionário com as universidades e seus pesos
universidades = {
    "A": {
        "nome": "UNIRIO",
        "pesos": [1, 1, 1, 1, 3],
    },
    "B": {
        "nome": "UFRJ",
        "pesos": [1, 2, 2, 1, 3],
    },
    "C": {
        "nome": "UFF",
        "pesos": [1, 3, 2, 1, 2],
    },
    "D": {
        "nome": "UFMG",
        "pesos": [1, 1, 1, 1, 1],
    },
}

# Entrada da escolha da universidade
escolha_universitaria = input("Escolha qual universidade você gostaria de calcular sua nota (A-UNIRIO, B-UFRJ, C-UFF, D-UFMG): ")

if escolha_universitaria in universidades:
    universidade = universidades[escolha_universitaria]
    print(f"Vamos calcular sua nota média na Universidade {universidade['nome']}!")

    notas = []
    for i, materia in enumerate(["Ciências humanas", "Ciências da natureza", "Linguagens e códigos", "Matemática", "Redação"]):
        nota_str = input(f"Digite sua nota de {materia}: ")
        nota = validar_nota(nota_str)
        notas.append(nota)

    media_tri_enem = calcular_media_tri_enem(universidade['pesos'], notas)
    print(f"Sua média do ENEM para a {universidade['nome']} é de {media_tri_enem:.1f}")
    print("Nos vemos numa próxima e boa sorte na chamada!")
else:
    print("Universidade inválida. Por favor, escolha entre A, B, C ou D.")







    