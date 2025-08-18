{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbgHnraN482j4VvvxiCgVK",
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
        "<a href=\"https://colab.research.google.com/github/FlaviaVitoriadeQueiroz/Introducao-a-Python/blob/main/Fun%C3%A7%C3%B5es.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        },
        "id": "y62UXCZSJiaz",
        "outputId": "f74fd652-a9db-4b9a-8c16-1071b61b16ba"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<function __main__.hello()>"
            ],
            "text/html": [
              "<div style=\"max-width:800px; border: 1px solid var(--colab-border-color);\"><style>\n",
              "      pre.function-repr-contents {\n",
              "        overflow-x: auto;\n",
              "        padding: 8px 12px;\n",
              "        max-height: 500px;\n",
              "      }\n",
              "\n",
              "      pre.function-repr-contents.function-repr-contents-collapsed {\n",
              "        cursor: pointer;\n",
              "        max-height: 100px;\n",
              "      }\n",
              "    </style>\n",
              "    <pre style=\"white-space: initial; background:\n",
              "         var(--colab-secondary-surface-color); padding: 8px 12px;\n",
              "         border-bottom: 1px solid var(--colab-border-color);\"><b>hello</b><br/>def hello()</pre><pre class=\"function-repr-contents function-repr-contents-collapsed\" style=\"\"><a class=\"filepath\" style=\"display:none\" href=\"#\">/content/&lt;ipython-input-1-c7869a778465&gt;</a>&lt;no docstring&gt;</pre></div>"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "#trechos de códigos reutilizáveis\n",
        "#dar um nome a um bloco de comandos e executar esses blocos\n",
        "\n",
        "def hello():\n",
        "  print(\"oie\")\n",
        "hello"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def maior(x, y):\n",
        "  if x > y:\n",
        "    print(x)\n",
        "  else:\n",
        "    print(y)\n",
        "\n",
        "maior (4,7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VKJbzcV0Nqu4",
        "outputId": "0a69817d-9531-4b3e-e0af-9d16cef6f68c"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def menor(x, y):\n",
        "  if x < y:\n",
        "    print(x)\n",
        "  else:\n",
        "    print(y)\n",
        "\n",
        "menor (4,7)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oxqVL_dyN7Yn",
        "outputId": "3a7ea6e2-2b8b-4ae0-f220-a126af480bed"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def soma(x, y):\n",
        "  total = x + y\n",
        "  print(total)\n",
        "\n",
        "soma(18, 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A3I1iG0kQQ3J",
        "outputId": "2b694d4d-1f60-4b67-bf89-51d55abd8fcb"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "27\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def sub(x, y):\n",
        "  total = x - y\n",
        "  print(total)\n",
        "\n",
        "sub(18, 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1ZNgPPx1QnWM",
        "outputId": "ebf215b2-58e8-46a2-8c77-7dff51dd0456"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def divisão(x, y):\n",
        "  total = x / y\n",
        "  print(total)\n",
        "\n",
        "divisão(18, 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HGjDtoMSQsx5",
        "outputId": "9869c03f-8ac7-4e78-cb23-9b889c4b60e2"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def multi(x, y):\n",
        "  total = x * y\n",
        "  print(total)\n",
        "\n",
        "multi(18, 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pFquUdyNQznf",
        "outputId": "d0a81a00-47f9-4c89-b118-852882ba5931"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "162\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#escopo local\n",
        "def soma(x, y):\n",
        "  total = x + y\n",
        "  print('soma total:', total)\n",
        "\n",
        "total = 40\n",
        "soma(18, 9)\n",
        "print(\"total\", total)\n",
        "total = 40"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vJ2jCxxWRO6L",
        "outputId": "3d750f04-afcd-49c6-ea98-b42fc4521a0b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "soma total: 27\n",
            "total 40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#variáveis globais\n",
        "def soma(x, y):\n",
        "  global total\n",
        "  total = x + y\n",
        "  print('soma total:', total)\n",
        "\n",
        "global total\n",
        "total = 40\n",
        "soma(18, 9)\n",
        "print(\"total\", total)\n",
        "total = 40"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VrpX_vbGSfC8",
        "outputId": "9fc87adb-96c0-432f-e346-53ec1d1adf56"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "soma total: 27\n",
            "total 27\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def soma(x, y):\n",
        "  total = x + y\n",
        "  return total\n",
        "\n",
        "soma(18, 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jmSytYaoTTm9",
        "outputId": "4cdc760b-b918-4fb6-f84a-c2ecfb020388"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "27"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def soma(x, y):\n",
        "  total = x + y\n",
        "  return total\n",
        "\n",
        "s=soma(18, 9)\n",
        "print('soma =', s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "khcgVJQJTjtr",
        "outputId": "08a527f3-94e3-428a-c64f-24198f722339"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "soma = 27\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#valor padrão\n",
        "def soma(x, y = 9):\n",
        "  total = x + y\n",
        "  print(total)\n",
        "\n",
        "soma(9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zENWLi3ZVl1x",
        "outputId": "eb23c040-2fa0-47c5-a8dd-b905ce2e36b8"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#valor padrão\n",
        "def calcular_juros (valor, taxa = 10):\n",
        "  juros = valor * taxa / 100\n",
        "  return juros\n",
        "\n",
        "calcular_juros(500)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ttBnq1DlT2sX",
        "outputId": "e07d1058-86cd-4f33-9959-f5bed5a0c5a6"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "50.0"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def lista( L= [4, 16, 89, 87,]):\n",
        "  L.sort()\n",
        "  print(L)\n",
        "\n",
        "lista()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uZ0leSqhWf5T",
        "outputId": "bd3e62d7-39f9-4ded-8fdc-1e8d4b1a6352"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[4, 16, 87, 89]\n"
          ]
        }
      ]
    }
  ]
}
