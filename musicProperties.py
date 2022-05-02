class MusicProperties:

    def __init__(self, instrumento, volume_inicial, volume_atual, bpm, oitava_atual, oitava_inicial):
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_atual
        self.bpm = bpm
        self.oitava_atual = oitava_atual
        self.oitava_inicial = oitava_inicial

    def selecao_de_procedimento(self, termo):
        if termo in ["!", ";", ",", "o", "O", "i", "I", "u", "U", "\n"]:
            if termo == "!":
                self.instrumento_changed(0, False)
            elif termo in ["o", "O", "i", "I", "u", "U"]:
                self.instrumento_changed(1, False)
            elif termo == "\n":
                self.instrumento_changed(2, False)
            elif termo == ";":
                self.instrumento_changed(3, False)
            elif termo == ",":
                self.instrumento_changed(4, False)
        elif "0" <= termo <= "9":
            self.instrumento_changed(termo, True)
        elif termo == " ":
            self.volume_changed()
        elif termo == "?":
            self.oitava_changed()

    def volume_changed(self):
        self.volume_atual *= 2
        if self.volume_atual > 200:
            self.volume_atual = self.volume_inicial
        print(f"volume mudou para: {self.volume_atual}")

    def oitava_changed(self):
        self.oitava_atual += 1
        if self.oitava_atual > 8:
            self.oitava_atual = self.oitava_inicial
        print(f"oitava mudou para: {self.oitava_atual}")

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

    def instrumento_changed(self, num, flag):
        if flag:
            self.instrumento = "Instrumento atual + " + num
        else:
            if num == 0:
                self.instrumento = "Agogo #114"
            elif num == 1:
                self.instrumento = "Harpsichord #7"
            elif num == 2:
                self.instrumento = "Tubular Bells #15"
            elif num == 3:
                self.instrumento = "Pan Flute #76"
            elif num == 4:
                self.instrumento = "Church Organ #20"
        print(f"Intrumento mudou para: {self.instrumento}")
