#include <stdio.h>

// Funçao para verificar se um numero pertence a sequência de Fibonacci
int pertenceFibonacci(int num) {
    int a = 0, b = 1, c = 0;

    if (num == 0) return 1; // O numero 0 pertence a sequencia de Fibonacci

    while (c < num) {
        c = a + b;
        a = b;
        b = c;
    }
    return (c == num) ? 1 : 0; // Retorna 1 se pertence, 0 caso contrario
}

int main() {
    int num;
    
    // Solicita ao usuario que informe um numero
    printf("Digite um numero para verificar se pertence a sequencia de Fibonacci: ");
    scanf("%d", &num);

    // Verifica e imprime a mensagem correspondente
    if (pertenceFibonacci(num)) {
        printf("%d pertence a sequencia de Fibonacci.\n", num);
    } else {
        printf("%d nao pertence a sequencia de Fibonacci.\n", num);
    }
    return 0;
}
