morse = input("Digite o código Morse separado por espaços: ").strip() #.strip() remove espaços extras no começo ou fim

dicionario = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
     " ": "/"
} #esquema de chave - valor

resultado = ""

palavras = morse.split(" / ") #separando palavras por " / "

for palavra in palavras:
    letras = palavra.split() #separando letras por espaço
    for codigo in letras:
        resultado += dicionario.get(codigo, "código desconhecido") #traduzindo cada código Morse .get pega o valor da chave
    resultado += " "  

print("Texto:", resultado.strip())
