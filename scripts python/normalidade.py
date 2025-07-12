from scipy.stats import shapiro, kstest, norm

# Lista de médias de qualidade para geradas por IA
usa_ia = [
    4.2, 2.6, 2.6, 3.4, 2.2, 3.0, 3.2, 3.6, 3.2, 2.2, 2.8, 2.4, 2.8, 3.0, 2.6, 2.8, 3.0, 3.2, 2.8, 3.0,
    2.8, 3.0, 3.2, 3.6, 2.6, 3.0, 2.8, 2.4, 2.8, 2.6, 3.2, 3.0, 3.2, 2.4, 3.0, 3.2, 3.2, 3.2, 2.8, 2.8,
    2.4, 3.6, 2.2, 2.6, 3.0, 2.6, 2.4, 3.2, 3.2, 1.6, 2.8, 2.4, 3.4, 2.6, 2.2, 2.4, 2.6, 2.4, 2.8, 3.2,
    2.8, 3.2, 3.4, 2.8, 3.0, 3.0, 2.8, 2.8, 2.8, 3.0, 3.2, 2.4, 3.8, 2.2, 2.6, 2.6, 2.8, 2.6, 4.2, 2.4,
    2.6, 2.6, 2.4, 3.2, 2.2, 3.0, 3.6, 3.0, 2.6, 3.2, 3.8, 2.6, 3.0, 3.6, 3.6, 3.8, 4.2, 2.2, 3.2, 3.6,
    4.2, 2.6, 2.4, 2.6, 3.0, 2.4, 3.0, 2.8, 2.8, 3.0, 3.4, 3.4, 2.4, 3.0, 2.6, 2.6, 2.0, 3.2, 3.2, 3.0,
    2.6, 2.8, 3.0, 2.4, 2.6, 3.0, 3.2, 2.8, 3.6, 2.0, 3.0, 3.4, 1.6, 3.2, 3.2, 3.2, 2.4
]

# Lista de médias de qualidade para geradas por IA
nao_ia = [
    4, 2.8, 3.2, 3.2, 4.2, 3.6, 3.4, 3.4, 3.8, 3.2, 3.4, 3.2, 3.4, 3.2, 3, 4.4, 4, 3.6,
    3.8, 3.2, 3.6, 4, 3.6, 3.4, 4.2, 3.6, 3.8, 3.4, 3.2, 2.6, 3, 2.6, 3.4, 4, 3.2, 4,
    3.8, 3.2, 4, 3.6, 3.8, 3.4, 3.8, 2.8, 3.6, 3.4, 3.4, 3.6, 4.4, 3.8, 3, 3, 3.8, 3.2,
    3.8, 3.2, 3, 4.2, 3.4, 3, 3.2, 2.8, 4, 3.6, 3.8, 4, 4.2, 4.4, 3.8, 3.4, 3.6, 3.8,
    4, 4.2, 3.8, 3.8, 4, 4, 3.4, 4, 4.2, 3.2, 3.8, 3, 3.6, 4.2, 3.2, 4.2, 3.6, 3.2,
    3.8, 3, 3.6, 3.8, 3.6, 3.2, 2.6, 3.6, 4.4, 4.2, 4, 3, 3.6, 3.4, 3.4, 3.4, 3.4,
    3.6, 3.2, 3.4, 3.8, 4.4, 3.2, 3.6, 3.4, 4, 4.4, 4, 3.2, 4.2, 3.8, 4, 3.2, 4.6,
    4, 4.6, 4, 3.6, 3.6, 4, 3.8, 3, 4, 3.4, 4.2, 2.8, 2.6
]

# -------------------------------------------
# TESTE DE NORMALIDADE - SHAPIRO-WILK
# -------------------------------------------
print("\nTeste de normalidade - Shapiro-Wilk:")

shapiro_ia = shapiro(usa_ia)
shapiro_nao_ia = shapiro(nao_ia)

print(f"Usa IA:      W = {shapiro_ia.statistic:.4f}, p = {shapiro_ia.pvalue:.4f}")
print(f"Não Usa IA:  W = {shapiro_nao_ia.statistic:.4f}, p = {shapiro_nao_ia.pvalue:.4f}")

# -------------------------------------------
# TESTE DE NORMALIDADE - Kolmogorov-Smirnov
# -------------------------------------------
# Normalizar os dados para aplicar kstest (média = 0, desvio = 1)
from scipy.stats import zscore

z_ia = zscore(usa_ia)
z_nao_ia = zscore(nao_ia)

print("\nTeste de normalidade - Kolmogorov-Smirnov:")
ks_ia = kstest(z_ia, 'norm')
ks_nao_ia = kstest(z_nao_ia, 'norm')

print(f"Usa IA:      KS = {ks_ia.statistic:.4f}, p = {ks_ia.pvalue:.4f}")
print(f"Não Usa IA:  KS = {ks_nao_ia.statistic:.4f}, p = {ks_nao_ia.pvalue:.4f}")