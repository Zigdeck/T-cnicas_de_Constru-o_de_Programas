class Music:

    def __init__(self, instrumento, volume_inicial, volume_atual, bpm, oitava):
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_atual
        self.bpm = bpm
        self.oitava = oitava

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
        
