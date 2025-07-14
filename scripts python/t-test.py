from scipy.stats import ttest_ind_from_stats

# Dados
media_nao_ia = 3.601459854
dp_nao_ia = 0.4517581876 
n_nao_ia = 137

media_ia = 2.897810219
dp_ia = 0.4797303308
n_ia = 137

# Teste t 
t_stat, p_value = ttest_ind_from_stats(
    mean1=media_nao_ia, std1=dp_nao_ia, nobs1=n_nao_ia,
    mean2=media_ia, std2=dp_ia, nobs2=n_ia,
    equal_var = True  # False se as variâncias forem diferentes e True se forem iguais/muito próximas (aplique levene para saber)
)

print("Estatistica t:", round(t_stat, 4))
print("Valor-p:", round(p_value, 4))
print("Valor-p:", "{:.2e}".format(p_value))
