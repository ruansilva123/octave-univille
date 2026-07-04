"""
Variáveis globais do programa
"""
lx = 0      # Comprimento da transversal com passagem de calor quadrada - metros
ly = 0      # Comprimento da espessura do tijolo - metros
k = 0       # Condutividade térmica - W/(m*K)
a = 0       # Difusão térmica - m2/s


"""
Constantes do programa
"""
TEMPERATURA_INICIAL = 25.0      # Temperatura inicial do tijolo - °C
TEMOPERATURA_DOS_GASES = 350    # Temperatura constante dos gases - °C


def definir_valores_iniciais():
    """
    Função para definir as variáveis iniciais do programa
    """
    # Definição das variáveis globais do programa
    global a, lx, ly, k

    print("Insira o tamanho da transversal com passagem de calor quadrada (em metros): ")
    lx = float(input())

    print("Insira o tamanho da espessura do tijolo (em metros): ")
    ly = float(input())

    print("Insira o valor da condutividade térmica (em W/(m*K)): ")
    k = float(input())

    print("Insira o valor da difusão térmica (em m2/s): ")
    a = float(input()) * pow(10, -7)

    



if __name__ == "__main__":
    """
    Função principal do programa que dará início à execução do código
    e centralizará a execução das funções do programa
    """
    definir_valores_iniciais()