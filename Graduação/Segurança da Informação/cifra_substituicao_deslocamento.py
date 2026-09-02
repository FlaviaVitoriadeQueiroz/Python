# Algoritmo de Criptografia por Substituição com Deslocamento (Cifra de César)
# Baseado no modelo de cifra simétrica e nas técnicas de substituição
# apresentadas por STALLINGS (2015), Capítulo 2 - Técnicas Clássicas de Encriptação.

def criptografar(texto, chave):
    
    resultado = ""
    for letra in texto:
        if letra.isalpha() and letra.isascii():
            # Trata apenas letras do alfabeto padrão (a-z, A-Z)
            base = ord('A') if letra.isupper() else ord('a')
            posicao = (ord(letra) - base + chave) % 26
            nova_letra = chr(posicao + base)
            resultado += nova_letra
        else:
            # Espaços, pontuação, números e letras acentuadas (á, ã, ç...)
            # permanecem inalterados
            resultado += letra
    return resultado


def descriptografar(texto_cifrado, chave):
    return criptografar(texto_cifrado, -chave)


# Exemplo 
if __name__ == "__main__":
    poema = """Devo comparar-te a um dia de verao?
Tu es mais bela e mais serena ainda:
Ventos fortes sacodem os botoes de maio,
E o tempo do verao dura pouco, ainda que linda."""

    chave = 3  # numero de posicoes que cada letra sera deslocada

    poema_criptografado = criptografar(poema, chave)
    poema_descriptografado = descriptografar(poema_criptografado, chave)

    print("=== TEXTO ORIGINAL ===")
    print(poema)
    print("\n=== TEXTO CRIPTOGRAFADO (chave =", chave, ") ===")
    print(poema_criptografado)
    print("\n=== TEXTO DESCRIPTOGRAFADO ===")
    print(poema_descriptografado)
