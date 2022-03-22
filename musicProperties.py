import random


class MusicProperties:

    def __init__(self, instrumento, volume_inicial, volume_atual, bpm, oitava):
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_atual
        self.bpm = bpm
        self.oitava = oitava

    def selecao_de_procedimento(self, termo):
        if termo == "BPM+" or termo == "BPM-":
            self.volume_changed(termo)
        elif termo == "T+" or termo == "T-":
            self.oitava_changed(termo)
        elif termo == "+" or termo == "-":
            self.volume_changed(termo)
        elif termo == "\n":
            self.instrumento_changed()

    def volume_changed(self, termo):
        if termo == "BPM+":
            self.volume_atual *= 2
        elif termo == "BPM-":
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

    def instrumento_changed(self):
        num = random.randint(0, 4)
        if num == 0:
            self.instrumento = "Violão"
        if num == 1:
            self.instrumento = "Guitarra"
        if num == 2:
            self.instrumento = "Piano"
        if num == 3:
            self.instrumento = "Flauta"
        print(f"Intrumento mudou para: {self.instrumento}")
