class Music:

    def __init__(self, instrumento, volume, bpm, oitava):
        self.instrumento = instrumento
        self.volume = volume
        self.bpm = bpm
        self.oitava = oitava

    def volume_changed(self, termo):
        if termo == "+":
            self.volume *= 2
        elif termo == "-":
            self.volume = self.volume

    def bpm_changed(self, termo):
        if termo == "BPM+":
            self.bpm += 50
        elif termo == "BPM-":
            self.bpm -= 50

    def oitava_changed(self, termo):
        if termo == "T+":
            self.oitava += 1
        elif termo == "T-":
            self.oitava -= 1