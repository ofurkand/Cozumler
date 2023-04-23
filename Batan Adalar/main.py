ada = [[1, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 1, 1],
       [0, 0, 1, 0, 1, 0],
       [1, 1, 0, None, 1, 0],
       [1, 0, 1, 1, 0, 0],
       [1, 0, 0, 0, 0, 1]]
karalar = []
silinecekler = []

maksimum = 0
for i in ada:
    if len(i) > maksimum: maksimum = len(i)

for i in range(len(ada)):
    if len(ada[i]) < maksimum:
        for j in range(len(ada[i]), maksimum):
            ada[i].insert(j, None)
            silinecekler.append([i, j])
    for j in range(len(ada[i])):
        if ada[i][j] == None:
            silinecekler.append([i, j])


def kontrol(i, j):
    if ada[i][j] == 1 and not [i, j] in karalar:
        karalar.append([i, j])
        if j < len(ada[i]) - 1:
            kontrol(i, j + 1)
        if i < len(ada) - 1:
            kontrol(i + 1, j)
        if j > 0:
            kontrol(i, j - 1)
        if i > 0:
            kontrol(i - 1, j)
        return
    else:
        return


for i in range(len(ada)):
    for j in range(len(ada[i])):
        if ada[i][j] == 1 and [i, j] not in karalar and ((i == 0 or i == len(ada) - 1 or j == 0 or j == len(ada[i]) - 1) or ([int(i + 1), j] in silinecekler or [i, int(j + 1)] in silinecekler or [int(i - 1),j] in silinecekler or [i,int(j - 1)] in silinecekler)):
            kontrol(i, j)
yeniada = []
for i in range(len(ada)):
    liste = []
    for j in range(len(ada[i])):
        if [i, j] in karalar:
            liste.append(1)
        elif [i, j] in silinecekler:
            liste.append(None)
        else:
            liste.append(0)
    yeniada.append(liste)

for i in yeniada:
    print(i)
