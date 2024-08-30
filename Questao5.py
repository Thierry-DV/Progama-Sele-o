def inverter_string(s):
    string_invertida = []
    for i in range(len(s) - 1, -1, -1):
        string_invertida.append(s[i])
    return ''.join(string_invertida)

def main():
    entrada = input("Digite a string que deseja inverter: ")
    resultado = inverter_string(entrada)
    print(f"String original: {entrada}")
    print(f"String invertida: {resultado}")

if __name__ == "__main__":
    main()
