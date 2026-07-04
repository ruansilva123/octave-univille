"""
Variáveis globais do programa
"""
lx = 0      # Comprimento da transversal quadrada com passagem de calor - metros
ly = 0      # Comprimento da espessura do tijolo - metros
k = 0       # Condutividade térmica - W/(m*K)
a = 0       # Difusão térmica - m2/s
T_i = 0     # Temperatura inicial do tijolo - °C
T_g = 0     # Temperatura constante dos gases - °C
h_gas = 0   # Coeficiente convecção dos gases - W/(m2*K)
T_a = 0     # Temperatura ambiente - °C
h_ar = 0    # Coeficiente convecção do ar - W/(m2*K)
nx = 0      # Número de nós no eixo x dentro da área de lx * ly (abertura de saída do gas * espessura do tijolo)
ny = 0      # Número de nós no eixo y dentro da área de lx * ly (abertura de saída do gas * espessura do tijolo)
dx = 0      # Distância da malha no eixo x
dy = 0      # Distância da malha no eixo y


"""
Constantes com os valores dados pelo enunciado do problema.
"""
TRANSVERSAL_QUADRADA = 0.3
ESPESSURA_TIJOL0 = 0.15
CONDUCTIVIDADE_TERMICA = 0.85
DIFUSAO_TERMICA = 5.5 * pow(10, -7)
TEMPERATURA_INICIAL = 25.0
TEMPERATURA_DOS_GASES = 350.0
COEFICIENTE_CONVECCAO = 100.0
TEMPERATURA_AMBIENTE = 25.0
COEFICIENTE_CONVECCAO_AMBIENTE = 5.0
NUMERO_DE_NOS_X = 7
NUMERO_DE_NOS_Y = 4


def definir_valores_iniciais_estaticamente():
    """
    Função para definir as variáveis iniciais do programa de forma estática
    """
    # Definição das variáveis globais do programa
    global a, lx, ly, k, T_i, T_g, h_gas, T_a, h_ar, nx, ny

    lx = TRANSVERSAL_QUADRADA
    ly = ESPESSURA_TIJOL0
    k = CONDUCTIVIDADE_TERMICA
    a = DIFUSAO_TERMICA
    T_i = TEMPERATURA_INICIAL
    T_g = TEMPERATURA_DOS_GASES
    h_gas = COEFICIENTE_CONVECCAO
    T_a = TEMPERATURA_AMBIENTE
    h_ar = COEFICIENTE_CONVECCAO_AMBIENTE
    nx = NUMERO_DE_NOS_X
    ny = NUMERO_DE_NOS_Y


def definir_valores_iniciais_dinamicamente():
    """
    Função para definir as variáveis iniciais do programa de forma dinâmica
    """
    # Definição das variáveis globais do programa
    global a, lx, ly, k, T_i, T_g, h_gas, T_a, h_ar, nx, ny

    print("Insira o tamanho da transversal quadrada com passagem de calor (em metros): ")
    lx = float(input())

    print("Insira o tamanho da espessura do tijolo (em metros): ")
    ly = float(input())

    print("Insira o valor da condutividade térmica (em W/(m*K)): ")
    k = float(input())

    print("Insira o valor da difusão térmica (em m2/s): ")
    a = float(input()) * pow(10, -7)

    print("Insira a temperatura inicial do tijolo (em °C): ")
    T_i = float(input())

    print("Insira a temperatura constante dos gases (em °C): ")
    T_g = float(input())

    print("Insira o valor do coeficiente de convecção (em W/(m2*K)): ")
    h_gas = float(input())

    print("Insira a temperatura ambiente (em °C): ")
    T_a = float(input())

    print("Insira o valor do coeficiente da superfície externa (em W/(m2*K)): ")
    h_ar = float(input())

    print("Insira o número de nós no eixo x: ")
    nx = int(input())

    print("Insira o número de nós no eixo y: ")
    ny = int(input())


def calcular_distancia_malha():
    """
    Função para calcular a distância da malha no eixo x e no eixo y
    """
    # Definição das variáveis globais do programa
    global dx, dy

    dx = lx / (nx - 1)
    dy = ly / (ny - 1)


if __name__ == "__main__":
    """
    Função principal do programa que dará início à execução do código
    e centralizará a execução das funções do programa
    """
    option = int(
        input(
            "Escolha uma das opçĩes abaixo:"
            "\n1 - Definir valores iniciais estaticamente"
            "\n2 - Definir valores iniciais dinamicamente"
            "\nOpção: "
        )
    )

    if option == 1:
        definir_valores_iniciais_estaticamente()
    elif option == 2:
        definir_valores_iniciais_dinamicamente()
    else:
        print("Opção inválida...")

    calcular_distancia_malha()