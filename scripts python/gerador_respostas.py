import random
import csv

def gerar_resposta_likert(media=3.5):
    """Gera uma resposta de 1 a 5 com distribuição ajustada para atingir a média e melhorar a dispersão."""
    valores = [1, 2, 3, 4, 5]
    pesos = [1 / ((media - v) ** 2 + 1) for v in valores]
    total = sum(pesos)
    probabilidades = [p / total for p in pesos]
    return random.choices(valores, weights=probabilidades, k=1)[0]

# Número de respondentes simulados
num_respondentes = 137

# Faixas de médias para cada coluna
medias_colunas = {
    "Clareza": (4.0, 4.5),
    "Organizacao": (4.0, 4.5),
    "Cobertura": (3.9, 4.3),
    "Velocidade": (1.4, 2.6),
    "Confianca": (4.6, 4.9),
}

# Lista para armazenar as respostas
respostas = []

for _ in range(num_respondentes):
    linha = []
    for coluna in ["Clareza", "Organizacao", "Cobertura", "Velocidade", "Confianca"]:
        media_min, media_max = medias_colunas[coluna]
        media = random.uniform(media_min, media_max)
        resposta = gerar_resposta_likert(media)
        linha.append(resposta)
    respostas.append(linha)

# Salva no CSV
with open("planilha_teste.csv", "w", newline="") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(["Clareza", "Organizacao", "Cobertura", "Velocidade", "Confianca"])
    writer.writerows(respostas)

print("Arquivo 'planilha_teste.csv' salvo com sucesso!")
