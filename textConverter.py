import random


class TextConverter:
    def __init__(self, texto):
        self.texto = texto

    def tratar_e_devolver(self):
        self.texto_to_upper()
        self.converte_notas()
        return self.texto

    # Tranforma todos as letras minúsculas em maiúsculas
    def texto_to_upper(self):
        texto_aux = ""
        for i in range(0, len(self.texto)):
            if "a" <= self.texto[i] <= "z":
                texto_aux += self.texto[i].upper()
            else:
                texto_aux += self.texto[i]
        self.texto = texto_aux

    def converte_notas(self):
        texto_aux = ""
        i = 0
        nota_anterior = ""
        while i < len(self.texto):
            # Caso contenha "BPM+" ou "BPM-", mantém isso no texto
            if self.texto[i:i+3] == "BPM":
                texto_aux += self.texto[i:i+4]
                i += 4
            # Caso o caractere esteja no intervalo de A a G, chama o método para procurar a nota correspondente
            elif "A" <= self.texto[i] <= "G":
                nota_atual = self.classificar_caractere_de_nota(self.texto[i])
                texto_aux += nota_atual
                nota_anterior = nota_atual
                i += 1
            # Caso seja as outras vogais...
            elif self.texto[i] == "O" or self.texto[i] == "I" or self.texto[i] == "U":
                # Se antes era A ou G, repete a última nota
                if nota_anterior == "A" or "G":
                    texto_aux += nota_anterior
                # Caso contrário, pausa
                else:
                    texto_aux += " "
                i += 1
            # Caso ? ou ., chama método de gerar letra randomica e logo em seguida chama
            # método de procurar a nota correspondente
            elif self.texto[i] == "?" or self.texto[i] == ".":
                letra_rand = self.gerar_nota_randomica()
                nota_atual1 = self.classificar_caractere_de_nota(letra_rand)
                texto_aux += nota_atual1
                i += 1
            # Caso T+ ou T-, grava no texto e pula para o próximo caractere
            elif self.texto[i:i+2] == "T+" or self.texto[i:i+2] == "T-":
                texto_aux += self.texto[i:i+2]
                i += 2
            # Caso '\n", grava no texto e pula 2 caracteres
            elif self.texto[i] == "\n":
                texto_aux += "\n"
                i += 2
            elif self.texto[i] == " ":
                texto_aux += " "
                i += 1
            # Caso contrário, ignora o caractere
            else:
                i += 1
        self.texto = texto_aux

    # Quando tivermos a biblioteca musical temos que trocar o retorno de cada letra
    # de acordo com a biblioteca
    def classificar_caractere_de_nota(self, carac):
        retorno = ""
        if carac == "A":
            retorno = "L"  # L simboliza Lá
        elif carac == "B":
            retorno = "S"  # S simboliza Si
        elif carac == "C":
            retorno = "D"  # D simboliza Dó
        elif carac == "D":
            retorno = "R"  # R simboliza Ré
        elif carac == "E":
            retorno = "M"  # M simboliza Mi
        elif carac == "F":
            retorno = "F"  # F simboliza Fá
        elif carac == "G":
            retorno = "s"  # s simboliza Sol
        return retorno

    def gerar_nota_randomica(self):
        num = random.randint(0, 7)
        retorno = ""
        if num == 0:
            retorno = "A"
        if num == 1:
            retorno = "B"
        if num == 2:
            retorno = "C"
        if num == 3:
            retorno = "D"
        if num == 4:
            retorno = "E"
        if num == 5:
            retorno = "F"
        if num == 6:
            retorno = "G"
        return retorno
