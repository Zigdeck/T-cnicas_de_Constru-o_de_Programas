from music import Music

instrumento = "Violao"
volume_inicial = 10
bpm = 50
oitava = 5
termo = "+"

m1 = Music(instrumento, volume_inicial, volume_inicial, bpm, oitava)

print(f"instumento: {m1.instrumento}")
print(f"volume: {m1.volume_inicial}")
print(f"bpm: {m1.bpm}")
print(f"oitava: {m1.oitava}")

m1.volume_changed("-")
m1.volume_changed("-")

m1.bpm_changed("BPM-")
m1.bpm_changed("BPM+")



