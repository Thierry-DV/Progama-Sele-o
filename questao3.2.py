import xml.etree.ElementTree as ET

def calcular_faturamento(dados):
    # Extrai os valores de faturamento da lista de elementos <row>
    faturamento = [float(row.find('valor').text) for row in dados.findall('row')]

    if not faturamento:
        print("Nenhum dado de faturamento encontrado.")
        return

    # Filtra os valores válidos (maior que 0)
    valores_validos = [valor for valor in faturamento if valor > 0]

    if not valores_validos:
        print("Nenhum valor de faturamento válido.")
        return

    menor = min(valores_validos)
    maior = max(valores_validos)
    media = sum(valores_validos) / len(valores_validos)
    
    dias_acima_media = sum(1 for valor in faturamento if valor > media)

    print(f"Menor valor de faturamento: {menor:.2f}")
    print(f"Maior valor de faturamento: {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

def main():
    try:
        # Carrega o arquivo XML
        tree = ET.parse('dados2.xml')
        root = tree.getroot()

        calcular_faturamento(root)
    
    except FileNotFoundError:
        print("Arquivo 'dados.xml' não encontrado.")
        return
    except ET.ParseError as e:
        print(f"Erro ao decodificar o arquivo XML: {e}")
        return

if __name__ == "__main__":
    main()
