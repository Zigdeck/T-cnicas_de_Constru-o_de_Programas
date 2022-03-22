from musicProperties import MusicProperties
from textConverter import TextConverter
from musicManager import MusicManager

texto = "auElaBPM-BPM-borarkkkT-kkkkk uma lista-+++ (informal, em po?rT+tuguês) do?s req--++uisitoaus que o sisauBPM+t..ema deveBPM+ possuir no pT-onto de vista dos autor"

texto1 = TextConverter(texto)
musica = MusicManager(texto1.tratar_e_devolver(), "Violão", 10, 10, 50, 5)
musica.leitura_texto()


