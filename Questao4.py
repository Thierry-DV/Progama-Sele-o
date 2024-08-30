def calcular_percentuais(faturamento_por_estado):
    # Calcula o total de faturamento
    total_faturamento = sum(faturamento_por_estado.values())

    if total_faturamento == 0:
        print("O total de faturamento é zero, não é possível calcular percentuais.")
        return

    # Calcula e exibe o percentual de representação de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_por_estado.items()}
    
    print(f"{'Estado':<10} {'Faturamento':<15} {'Percentual (%)':<15}")
    print("-" * 40)
    for estado, valor in faturamento_por_estado.items():
        percentual = percentuais[estado]
        print(f"{estado:<10} R${valor:,.2f}      {percentual:.2f}%")

def main():
    # Dados de faturamento por estado
    faturamento_por_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    calcular_percentuais(faturamento_por_estado)

if __name__ == "__main__":
    main()
