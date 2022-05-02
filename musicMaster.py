from textConverter import TextConverter
from musicManager import MusicManager


class MusicMaster:
    def __init__(self, texto, instrumento, volume_inicial, bpm, oitava_inicial):
        self.texto = texto
        self.instrumento = instrumento
        self.volume_inicial = volume_inicial
        self.volume_atual = volume_inicial
        self.bpm = bpm
        self.oitava_inicial = oitava_inicial
        self.oitava_atual = oitava_inicial

    def converter(self):
        texto1 = TextConverter(self.texto)
        musica = MusicManager(texto1.tratar_e_devolver(), self.instrumento, self.volume_inicial, self.volume_atual, self.bpm, self.oitava_atual, self.oitava_inicial)
        musica.leitura_texto()
