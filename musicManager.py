from musicProperties import MusicProperties


class MusicManager:
    def __init__(self, texto, instrumento, volume_inicial, volume_atual, bpm, oitava_atual, oitava_inicial):
        self.texto = texto
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_atual
        self.bpm = bpm
        self.oitava_atual = oitava_atual
        self.oitava_inicial = oitava_inicial
        self.musica = MusicProperties(instrumento, volume_inicial, volume_atual, bpm, oitava_atual, oitava_inicial)

    def leitura_texto(self):
        i = 0
        while i < len(self.texto):
            if self.texto[i] in ["L", "S", "D", "R", "M", "F", "s", "#"]:
                self.tocar_nota(self.texto[i])
                i += 1
            elif (self.texto[i] in ["\n", "?", ".", " ", "!", ";", ",", "o", "O", "i", "I", "u", "U"]) or ("0" <= self.texto[i] <= "9"):
                self.musica.selecao_de_procedimento(self.texto[i])
                i += 1
            elif self.texto[i] == "?" or "." or " ":
                self.musica.selecao_de_procedimento(self.texto[i])
                i += 1

            """
            elif self.texto[i:i+3] == "BPM":
                self.musica.selecao_de_procedimento(self.texto[i:i+4])
                i += 4
            elif self.texto[i] == "T":
                self.musica.selecao_de_procedimento(self.texto[i:i+2])
                i += 2
            elif self.texto[i] == "+" or self.texto[i] == "-":
                self.musica.selecao_de_procedimento(self.texto[i])
                i += 1
            elif self.texto[i:i+1] == "\n":
                self.musica.selecao_de_procedimento("\n")
                i += 2
            else:
                self.tocar_nota(self.texto[i])
                i += 1
            """

    @staticmethod
    def tocar_nota(nota):
        if nota == "L":
            print("Lá")         # Aqui tocaria a nota com a biblioteca
        elif nota == "S":
            print("Si")         # Aqui tocaria a nota com a biblioteca
        elif nota == "D":
            print("Dó")         # Aqui tocaria a nota com a biblioteca
        elif nota == "R":
            print("Ré")         # Aqui tocaria a nota com a biblioteca
        elif nota == "M":
            print("Mi")         # Aqui tocaria a nota com a biblioteca
        elif nota == "F":
            print("Fá")         # Aqui tocaria a nota com a biblioteca
        elif nota == "s":
            print("Sol")        # Aqui tocaria a nota com a biblioteca
        elif nota == "#":
            print("PAUSA")
