from musicProperties import Music

texto = "ElaBPM-BPM-borar uma lista-+++ (informal, em porT+tuguês) dos req--++uisitos que o sisBPM+tema deveBPM+ possuir no pT-onto de vista dos autor"
instrumento = "Violao"
volume_inicial = 10
bpm = 50
oitava = 5

m1 = Music(instrumento, volume_inicial, volume_inicial, bpm, oitava)
print(f"instumento: {m1.instrumento}")
print(f"volume: {m1.volume_inicial}")
print(f"bpm: {m1.bpm}")
print(f"oitava: {m1.oitava}")
i = 0

""" Teste para reproduzir o texto e ver o resultado no console """
while i < len(texto):
    if texto[i:i+3] == "BPM":
        m1.tratamento_caractere(texto[i:i+4])
        i += 4
    elif texto[i:i+2] == "T+" or texto[i:i+2] == "T-":
        m1.tratamento_caractere(texto[i:i+2])
        i += 2
    else:
        m1.tratamento_caractere(texto[i])
        i += 1
