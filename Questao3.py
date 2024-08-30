import json

def calcular_faturamento(dados):
    faturamento = dados.get('faturamento', [])

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
    # Lê o conteúdo do arquivo JSON
    try:
        with open('test.json', 'r') as file:
            content = file.read()
            if not content.strip():
                print("Arquivo 'test.json' está vazio.")
                return
            print("Conteúdo do arquivo JSON:")
            print(content)
            dados = json.loads(content)
    except FileNotFoundError:
        print("Arquivo 'test.json' não encontrado.")
        return
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")
        return

    calcular_faturamento(dados)

if __name__ == "__main__":
    main()
