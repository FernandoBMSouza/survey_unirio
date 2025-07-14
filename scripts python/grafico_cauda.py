import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ---------------------------
# 1. Simulando os dados reais
# ---------------------------

# Dados do survey
media_ia = 2.897810219
desvio_ia = 0.4797303308
n_ia = 137

media_manual = 3.601459854
desvio_manual = 0.4517581876
n_manual = 137

# Gerando dados simulados com distribuição normal
# np.random.seed(42)  # para reprodutibilidade
# grupo_ia = np.random.normal(loc=media_ia, scale=desvio_ia, size=n_ia)
# grupo_manual = np.random.normal(loc=media_manual, scale=desvio_manual, size=n_manual)

grupo_ia = [ 4.2, 2.6, 2.6, 3.4, 2.2, 3.0, 3.2, 3.6, 3.2, 2.2, 2.8, 2.4, 2.8, 3.0, 2.6, 2.8, 3.0, 3.2, 2.8, 3.0,
    2.8, 3.0, 3.2, 3.6, 2.6, 3.0, 2.8, 2.4, 2.8, 2.6, 3.2, 3.0, 3.2, 2.4, 3.0, 3.2, 3.2, 3.2, 2.8, 2.8,
    2.4, 3.6, 2.2, 2.6, 3.0, 2.6, 2.4, 3.2, 3.2, 1.6, 2.8, 2.4, 3.4, 2.6, 2.2, 2.4, 2.6, 2.4, 2.8, 3.2,
    2.8, 3.2, 3.4, 2.8, 3.0, 3.0, 2.8, 2.8, 2.8, 3.0, 3.2, 2.4, 3.8, 2.2, 2.6, 2.6, 2.8, 2.6, 4.2, 2.4,
    2.6, 2.6, 2.4, 3.2, 2.2, 3.0, 3.6, 3.0, 2.6, 3.2, 3.8, 2.6, 3.0, 3.6, 3.6, 3.8, 4.2, 2.2, 3.2, 3.6,
    4.2, 2.6, 2.4, 2.6, 3.0, 2.4, 3.0, 2.8, 2.8, 3.0, 3.4, 3.4, 2.4, 3.0, 2.6, 2.6, 2.0, 3.2, 3.2, 3.0,
    2.6, 2.8, 3.0, 2.4, 2.6, 3.0, 3.2, 2.8, 3.6, 2.0, 3.0, 3.4, 1.6, 3.2, 3.2, 3.2, 2.4
]  # 137 valores reais aqui
grupo_manual = [4, 2.8, 3.2, 3.2, 4.2, 3.6, 3.4, 3.4, 3.8, 3.2, 3.4, 3.2, 3.4, 3.2, 3, 4.4, 4, 3.6,
    3.8, 3.2, 3.6, 4, 3.6, 3.4, 4.2, 3.6, 3.8, 3.4, 3.2, 2.6, 3, 2.6, 3.4, 4, 3.2, 4,
    3.8, 3.2, 4, 3.6, 3.8, 3.4, 3.8, 2.8, 3.6, 3.4, 3.4, 3.6, 4.4, 3.8, 3, 3, 3.8, 3.2,
    3.8, 3.2, 3, 4.2, 3.4, 3, 3.2, 2.8, 4, 3.6, 3.8, 4, 4.2, 4.4, 3.8, 3.4, 3.6, 3.8,
    4, 4.2, 3.8, 3.8, 4, 4, 3.4, 4, 4.2, 3.2, 3.8, 3, 3.6, 4.2, 3.2, 4.2, 3.6, 3.2,
    3.8, 3, 3.6, 3.8, 3.6, 3.2, 2.6, 3.6, 4.4, 4.2, 4, 3, 3.6, 3.4, 3.4, 3.4, 3.4,
    3.6, 3.2, 3.4, 3.8, 4.4, 3.2, 3.6, 3.4, 4, 4.4, 4, 3.2, 4.2, 3.8, 4, 3.2, 4.6,
    4, 4.6, 4, 3.6, 3.6, 4, 3.8, 3, 4, 3.4, 4.2, 2.8, 2.6
]  # 137 valores reais aqui

# Convertendo as listas para arrays NumPy
grupo_ia = np.array(grupo_ia)
grupo_manual = np.array(grupo_manual)

# ---------------------------
# 2. Testes estatísticos
# ---------------------------

# Teste de normalidade
ks_ia = stats.kstest(grupo_ia, 'norm', args=(grupo_ia.mean(), grupo_ia.std()))
ks_manual = stats.kstest(grupo_manual, 'norm', args=(grupo_manual.mean(), grupo_manual.std()))
print(f"KS - IA: p = {ks_ia.pvalue:.4f}")
print(f"KS - Manual: p = {ks_manual.pvalue:.4f}")

# Teste de homogeneidade de variâncias (Levene)
levene = stats.levene(grupo_ia, grupo_manual)
print(f"Levene: p = {levene.pvalue:.4f}")

# Teste t de Student (bicaudal)
t_stat, p_value = stats.ttest_ind(grupo_ia, grupo_manual, equal_var=True)
print(f"Teste t: t = {t_stat:.2f}, p = {p_value:.4f}")

# Conclusão do teste
alpha = 0.05
if p_value < alpha:
    print("Resultado: Rejeita H0 - Existe diferença significativa entre IA e Manual")
else:
    print("Resultado: Não rejeita H0 - Não há diferença significativa")

# ---------------------------
# 3. Gráfico do teste t - Bicaudal
# ---------------------------

# Parâmetros do gráfico
df = n_ia + n_manual - 2  # graus de liberdade
x = np.linspace(-4, 4, 300)
y = stats.t.pdf(x, df)

# t crítico para bicaudal (α/2 em cada cauda)
t_crit = stats.t.ppf(1 - alpha/2, df)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição t', color='black')

# Região crítica (caudas)
plt.fill_between(x, 0, y, where=(x <= -t_crit) | (x >= t_crit), color='red', alpha=0.3, label='Região crítica (α = 0.05)')

# Linha do t observado
plt.axvline(t_stat, color='blue', linestyle='--', label=f't observado = {t_stat:.2f}')
plt.axvline(-t_stat, color='blue', linestyle='--', alpha=0.3)

# Configurações do gráfico
plt.title('Distribuição t - Teste Bicaudal')
plt.xlabel('t')
plt.ylabel('Densidade de probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
