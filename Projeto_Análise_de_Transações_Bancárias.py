{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMLGN/w060muGZRB7p3HHc6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FlaviaVitoriadeQueiroz/Introducao-a-Python/blob/main/Projeto_An%C3%A1lise_de_Transa%C3%A7%C3%B5es_Banc%C3%A1rias.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "52ueolS41be3",
        "outputId": "e68c482d-5577-4ec1-ce99-e2147bbc8a80"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['1000', 'Crédito', '786.83', 'Educação']\n",
            "['1003', 'Crédito', '870.23', 'Saúde']\n",
            "['1000', 'Crédito', '681.74', 'Saúde']\n",
            "['1003', 'Crédito', '106.1', 'Transporte']\n",
            "['1006', 'Débito', '147.16', 'Salário']\n",
            "['1007', 'Crédito', '787.84', 'Lazer']\n",
            "['1001', 'Crédito', '24.61', 'Alimentar']\n",
            "['1010', 'Crédito', '239.61', 'Salário']\n",
            "['1010', 'Débito', '921.39', 'Lazer']\n",
            "['1007', 'Crédito', '335.32', 'Lazer']\n",
            "['1010', 'Débito', '766.97', 'Saúde']\n",
            "['1000', 'Crédito', '79.37', 'Educação']\n",
            "['1001', 'Crédito', '56.28', 'Saúde']\n",
            "['1010', 'Débito', '70.23', 'Saúde']\n",
            "['1010', 'Débito', '395.46', 'Lazer']\n",
            "['1008', 'Débito', '956.07', 'Salário']\n",
            "['1001', 'Débito', '198.36', 'Saúde']\n",
            "['1002', 'Crédito', '908.2', 'Saúde']\n",
            "['1009', 'Crédito', '655.54', 'Educação']\n",
            "['1001', 'Débito', '810.33', 'Saúde']\n",
            "['1002', 'Débito', '457.15', 'Educação']\n",
            "['1008', 'Crédito', '764.96', 'Salário']\n",
            "['1002', 'Crédito', '119.98', 'Lazer']\n",
            "['1006', 'Débito', '153.65', 'Saúde']\n",
            "['1004', 'Débito', '642.67', 'Lazer']\n",
            "['1010', 'Crédito', '427.11', 'Salário']\n",
            "['1002', 'Débito', '424.46', 'Alimentar']\n",
            "['1009', 'Débito', '125.3', 'Transporte']\n",
            "['1009', 'Crédito', '623.6', 'Salário']\n",
            "['1003', 'Crédito', '250.25', 'Alimentar']\n",
            "['1007', 'Crédito', '897.07', 'Lazer']\n",
            "['1001', 'Débito', '589.2', 'Transporte']\n",
            "['1000', 'Débito', '307.27', 'Salário']\n",
            "['1004', 'Crédito', '161.05', 'Educação']\n",
            "['1005', 'Débito', '352.43', 'Educação']\n",
            "['1009', 'Crédito', '320.66', 'Salário']\n",
            "['1003', 'Crédito', '74.62', 'Saúde']\n",
            "['1010', 'Débito', '64.75', 'Educação']\n",
            "['1003', 'Crédito', '562.31', 'Saúde']\n",
            "['1008', 'Débito', '675.15', 'Transporte']\n",
            "['1008', 'Débito', '220.92', 'Educação']\n",
            "['1008', 'Crédito', '183.77', 'Alimentar']\n",
            "['1010', 'Débito', '209.41', 'Salário']\n",
            "['1002', 'Débito', '958.59', 'Alimentar']\n",
            "['1009', 'Crédito', '684.11', 'Salário']\n",
            "['1004', 'Crédito', '150.2', 'Alimentar']\n",
            "['1010', 'Débito', '433.72', 'Lazer']\n",
            "['1006', 'Débito', '180.62', 'Educação']\n",
            "['1005', 'Crédito', '296.39', 'Alimentar']\n",
            "['1003', 'Débito', '31.77', 'Alimentar']\n",
            "Salário: R$1619.91\n",
            "Lazer: R$2393.24\n",
            "Saúde: R$1999.54\n",
            "Educação: R$1275.87\n",
            "Alimentar: R$1414.82\n",
            "Transporte: R$1389.65\n"
          ]
        }
      ],
      "source": [
        "import csv #permite ler e escrever arquivos .csv\n",
        "import random #gera valores aleatórios\n",
        "\n",
        "tipos = ['Crédito', 'Débito']\n",
        "categorias = ['Alimentar', 'Transporte', 'Saúde', 'Lazer', 'Salário', 'Educação']\n",
        "\n",
        "#open abre um novo arquivo para escrever, nele deve haver nome e modo de abertura\n",
        "#with abre um arquivo e fecha automaticamente/context manager\n",
        "#'transacoes.csv' é o nome do arquivo\n",
        "#'w' é de write, significa que vou subescrever no arquivo, se ele não existir é criado, se existir será apagado e refeito do 0\n",
        "  # há outras opções como: 'r' read, 'a' append\n",
        "#newline serve para não ter espaço em branco entre as linhas do arquivo .csv, o que geralmente é bem comum\n",
        "#as serve para acessar o arquivo dentro de with\n",
        "with open(\"transacoes.csv\", mode=\"w\", newline=\"\") as arquivo:\n",
        "  escrever = csv.writer(arquivo)\n",
        "  escrever.writerow([\"cliente_id\", \"tipo\", \"valor\", \"categoria\"]) #writer row = escreva uma linha\n",
        "  for i in range(50):\n",
        "        cliente_id = random.randint(1000, 1010) #random é uma biblioteca que serve para sortear números #randint = random + int → número inteiro aleatório\n",
        "        tipo = random.choice(tipos) #sortei um item de uma lsita\n",
        "        valor = round(random.uniform(10, 1000), 2) #uniform = valores décimas\n",
        "        categoria = random.choice(categorias)\n",
        "        escrever.writerow([cliente_id, tipo, valor, categoria])\n",
        "\n",
        "with open(\"transacoes.csv\", mode=\"r\") as arquivo:\n",
        "    leitor = csv.reader(arquivo)\n",
        "    next(leitor)  # pula o cabeçalho\n",
        "    for linha in leitor: #mostra cada linha da planilha\n",
        "        print(linha)\n",
        "\n",
        "totais = {} #criou-se um dicionário vazio\n",
        "\n",
        "with open(\"transacoes.csv\", mode=\"r\") as arquivo: #estamos abrindo o arquivo que foi gerado no bloco d ecódigos acima para leitura\n",
        "    leitor = csv.reader(arquivo)\n",
        "    next(leitor) #pula a primeira linha, o cabeçario\n",
        "    for linha in leitor: #vai ler linha por linha do arquivo\n",
        "        tipo = linha[1] #estamos pegando os dados da lista\n",
        "        valor = float(linha[2])\n",
        "        categoria = linha[3]\n",
        "        if tipo == \"Débito\":\n",
        "            if categoria not in totais: #verifica se a categoria já está no dicionáro\n",
        "                totais[categoria] = 0 #se não estiver coloca 0\n",
        "            totais[categoria] += valor #se já estiver soma\n",
        "for cat, total in totais.items(): #cat = categoria #total.items bai pegar tudo que tiver\n",
        "    print(f\"{cat}: R${total:.2f}\")"
      ]
    }
  ]
}