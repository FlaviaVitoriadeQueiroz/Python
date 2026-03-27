import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

# Função para criar gráficos padronizados
def criar_grafico(caracteristicas, valores, titulo):
    # Ordenar valores
    ordem = np.argsort(valores)
    caracteristicas_ordenadas = [caracteristicas[i] for i in ordem]
    valores_ordenados = [valores[i] for i in ordem]

    # Criar figura 
    plt.figure(figsize=(10, 5))

    # NOVO: controle de posição + largura automática
    x = np.arange(len(valores_ordenados))
    largura = 0.6 if len(valores_ordenados) > 6 else 0.4

    # Criar barras
    plt.bar(x, valores_ordenados,
            width=largura,
            color="#e754a6", edgecolor="#FF81C4",
            linewidth=2)

    # Ajustar nomes no eixo x
    plt.xticks(x, caracteristicas_ordenadas, rotation=45, color="#000000")

    # Títulos e rótulos
    plt.title(titulo, fontsize=18, fontname="Segoe UI",
              color="#333333", fontweight="bold")
    plt.xlabel("Características", fontsize=12, fontname="Segoe UI",
               color="#333333", fontweight="bold")
    plt.ylabel("Número de Respostas", fontsize=12, fontname="Segoe UI",
               color="#333333", fontweight="bold")

    # Eixos
    plt.yticks(color="#000000")
    plt.ylim(0, 5)

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Remover bordas desnecessárias
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color("#dddddd")
    ax.spines['bottom'].set_color("#dddddd")

    # Valores nas barras
    for i, v in enumerate(valores_ordenados):
        plt.text(i, v + 0.1, str(v),
                 ha='center', va='bottom',
                 fontsize=10, fontname="Segoe UI",
                 color="#333333", fontweight="bold")

    # Grid
    plt.grid(axis='y', color="#dddddd", linestyle='--', alpha=0.7)

    # Ajuste final
    plt.tight_layout()
    plt.show()


# Meus pontos fortes
caracteristicas1 = ["Estudiosa", "Inteligente", "Dedicada", "Organizada",
                    "Sincera", "Meticulosa", "Divertida", "Gentil"]
valores1 = [5, 4, 3, 1, 2, 1, 3, 4]

criar_grafico(caracteristicas1, valores1, "Meus Pontos Fortes")


# Pontos a melhorar
caracteristicas2 = ["Autocobrança excessiva", "Vulnerável", "Insensível", "Brava"]
valores2 = [3, 3, 1, 4]

criar_grafico(caracteristicas2, valores2, "Pontos a Melhorar")


# Características que me definem
caracteristicas3 = ["Personalidade forte", "Racionalidade", "Lealdade", "Estudiosa"]
valores3 = [4, 1, 1, 1]

criar_grafico(caracteristicas3, valores3, "Características que me Definem")
