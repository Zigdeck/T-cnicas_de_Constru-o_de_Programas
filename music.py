class Music:

    def __init__(self, instrumento, volume_inicial, volume_atual, bpm, oitava):
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_atual
        self.bpm = bpm
        self.oitava = oitava

    def tratamento_caractere(self, caractere):
        if caractere == "+" or caractere == "-":
            self.volume_changed(caractere)
        elif caractere == "BPM+" or caractere == "BPM-":
            self.bpm_changed(caractere)
        elif caractere == "T+" or caractere == "T-":
            self.oitava_changed(caractere)
        elif caractere == "A" or "B" or "C" or "D" or "E" or "F" or "G":
            self.nota_changed(caractere)

    def nota_changed(self, termo):
        if termo.upper() == "A":
            print("Lá")
            # return "Lá"
        elif termo.upper() == "B":
            print("Si")
            # return "Si"
        elif termo.upper() == "C":
            print("Dó")
            # return "Dó"
        elif termo.upper() == "D":
            print("Ré")
            # return "Ré"
        elif termo.upper() == "E":
            print("Dó")
            # return "Dó"
        elif termo.upper() == "F":
            print("Fá")
            # return "Fá"
        elif termo.upper() == "G":
            print("Pausa")
            # return " "

    def volume_changed(self, termo):
        if termo == "+":
            self.volume_atual *= 2
        elif termo == "-":
            self.volume_atual = self.volume_inicial
        print(f"volume mudou para: {self.volume_atual}")

    def bpm_changed(self, termo):
        if termo == "BPM+":
            self.bpm += 50
            if self.bpm > 1000:
                self.bpm = 1000
                print("Valor maximo de bpm atingido")
        elif termo == "BPM-":
            self.bpm -= 50
            if self.bpm < 10:
                self.bpm = 10
                print("Valor minimo de bpm atingido")
        print(f"bpm mudou para: {self.bpm}")

    def oitava_changed(self, termo):
        if termo == "T+":
            self.oitava += 1
        elif termo == "T-":
            self.oitava -= 1
        print(f"oitava mudou para: {self.oitava}")
