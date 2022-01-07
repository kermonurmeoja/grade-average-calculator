hinnete_tabel = [['eesti keel', 5, 4, 3, 4, 4, 3, 4, 4],
                 ['matemaatika', 4, 4, 5, 5, 4, 5, 5, 4, 5],
                 ['keemia', 4, 3, 3, 2, 3, 4],
                 ['kirjandus', 5, 5, 5, 4, 5, 5, 4],
                 ['bioloogia', 4, 5, 4, 4, 3, 5, 5, 5]]
eesti_keel = hinnete_tabel[0]
matem = hinnete_tabel[1]
keemia = hinnete_tabel[2]
kirjandus = hinnete_tabel[3]
bio = hinnete_tabel[4]

def keskminehinne(aine):
    i = 1
    summa = 0
    hinded = aine[1:(len(aine))]
    for hinne in hinded:
      summa = summa + aine[i]
      i = i + 1
    vastus = summa / (len(aine) - 1)
    return float(vastus)

print(eesti_keel[0] + ": " + str(round(keskminehinne(eesti_keel), 2)))
print(matem[0] + ": " + str(round(keskminehinne(matem), 2)))
print(keemia[0] + ": " + str(round(keskminehinne(keemia), 2)))
print(kirjandus[0] + ": " + str(round(keskminehinne(kirjandus), 2)))
print(bio[0] + ": " + str(round(keskminehinne(bio), 2)))
