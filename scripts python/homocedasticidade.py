import matplotlib.pyplot as plt
import numpy as np

# Dados
usa_ia = [4.2, 2.6, 2.6, 3.4, 2.2, 3.0, 3.2, 3.6, 3.2, 2.2, 2.8, 2.4, 2.8, 3.0, 2.6, 2.8, 3.0, 3.2, 2.8, 3.0,
    2.8, 3.0, 3.2, 3.6, 2.6, 3.0, 2.8, 2.4, 2.8, 2.6, 3.2, 3.0, 3.2, 2.4, 3.0, 3.2, 3.2, 3.2, 2.8, 2.8,
    2.4, 3.6, 2.2, 2.6, 3.0, 2.6, 2.4, 3.2, 3.2, 1.6, 2.8, 2.4, 3.4, 2.6, 2.2, 2.4, 2.6, 2.4, 2.8, 3.2,
    2.8, 3.2, 3.4, 2.8, 3.0, 3.0, 2.8, 2.8, 2.8, 3.0, 3.2, 2.4, 3.8, 2.2, 2.6, 2.6, 2.8, 2.6, 4.2, 2.4,
    2.6, 2.6, 2.4, 3.2, 2.2, 3.0, 3.6, 3.0, 2.6, 3.2, 3.8, 2.6, 3.0, 3.6, 3.6, 3.8, 4.2, 2.2, 3.2, 3.6,
    4.2, 2.6, 2.4, 2.6, 3.0, 2.4, 3.0, 2.8, 2.8, 3.0, 3.4, 3.4, 2.4, 3.0, 2.6, 2.6, 2.0, 3.2, 3.2, 3.0,
    2.6, 2.8, 3.0, 2.4, 2.6, 3.0, 3.2, 2.8, 3.6, 2.0, 3.0, 3.4, 1.6, 3.2, 3.2, 3.2, 2.4
]
nao_usa_ia = [4, 2.8, 3.2, 3.2, 4.2, 3.6, 3.4, 3.4, 3.8, 3.2, 3.4, 3.2, 3.4, 3.2, 3, 4.4, 4, 3.6,
    3.8, 3.2, 3.6, 4, 3.6, 3.4, 4.2, 3.6, 3.8, 3.4, 3.2, 2.6, 3, 2.6, 3.4, 4, 3.2, 4,
    3.8, 3.2, 4, 3.6, 3.8, 3.4, 3.8, 2.8, 3.6, 3.4, 3.4, 3.6, 4.4, 3.8, 3, 3, 3.8, 3.2,
    3.8, 3.2, 3, 4.2, 3.4, 3, 3.2, 2.8, 4, 3.6, 3.8, 4, 4.2, 4.4, 3.8, 3.4, 3.6, 3.8,
    4, 4.2, 3.8, 3.8, 4, 4, 3.4, 4, 4.2, 3.2, 3.8, 3, 3.6, 4.2, 3.2, 4.2, 3.6, 3.2,
    3.8, 3, 3.6, 3.8, 3.6, 3.2, 2.6, 3.6, 4.4, 4.2, 4, 3, 3.6, 3.4, 3.4, 3.4, 3.4,
    3.6, 3.2, 3.4, 3.8, 4.4, 3.2, 3.6, 3.4, 4, 4.4, 4, 3.2, 4.2, 3.8, 4, 3.2, 4.6,
    4, 4.6, 4, 3.6, 3.6, 4, 3.8, 3, 4, 3.4, 4.2, 2.8, 2.6
]
# Juntar dados
valores = np.array(usa_ia + nao_usa_ia)
grupos = np.array(["IA"] * len(usa_ia) + ["Manual"] * len(nao_usa_ia))
# Cálculo das médias
media_ia = np.mean(usa_ia)
media_manual = np.mean(nao_usa_ia)
# Cálculo dos resíduos
residuos = np.array([
    valor - media_ia if grupo == "IA" else valor - media_manual
    for valor, grupo in zip(valores, grupos)
])
# Criação do gráfico
plt.figure(figsize=(10, 6))
# IA
plt.scatter(usa_ia, residuos[:len(usa_ia)], color="red", alpha=0.6, label="IA")
# Manual
plt.scatter(nao_usa_ia, residuos[len(usa_ia):], color="blue", alpha=0.6, label="Manual")

plt.axhline(0, color="gray", linestyle="--")
plt.title("Gráfico de Homocedasticidade")
plt.xlabel("Valor observado (qualidade percebida)")
plt.ylabel("Resíduo (diferença para a média do grupo)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
