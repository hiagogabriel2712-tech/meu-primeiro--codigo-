# Projeto de Lógica de Programação - Hiago
# Objetivo: Calcular faturamento e lucro focado em crescimento financeiro

faturamento = 150000  # Exemplo de ganho da empresa
custos = 45000        # Exemplo de despesas da empresa

# O cálculo do lucro
lucro_liquido = faturamento - custos

# Exibindo os resultados na tela
print(f"Faturamento Total: R$ {faturamento}")
print(f"Custos Operacionais: R$ {custos}")
print(f"Lucro Líquido Real: R$ {lucro_liquido}")

if lucro_liquido > 100000:
    print("Resultado: Meta de alta performance alcançada com sucesso!")
else:
    print("Resultado: Analisar custos para aumentar a margem de lucro.")
