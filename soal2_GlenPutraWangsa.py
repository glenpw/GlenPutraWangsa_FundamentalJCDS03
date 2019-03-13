# soal 2
hitung = 0
antrian = [25, 25, 100]

def tickets(peopleInLine):
    hitung2 = 0
    def counter(fn, theList) :
        newList = []
        for item in theList :
            if(fn(item)):
                newList.append(item)
        return newList

    dualima = counter(lambda item: item == 25, peopleInLine)
    limapuluh = counter(lambda item: item == 50, peopleInLine)
    seratus = counter(lambda item: item == 100, peopleInLine)

    if (len(seratus) == 0):
        for n in range(len(dualima)):
            hitung = limapuluh[0] - dualima[n]
    elif (len(limapuluh) == 0):
        for n in range(len(dualima)):
            hitung = seratus[0] - dualima[n]
    else:
        for n in range(len(dualima)):
            for i in range(len(limapuluh)):
                hitung = seratus[0] - limapuluh[i]
            hitung2 = hitung - dualima[n]

    if (hitung2-25 == 0):
        print("NO")
    else:
        print("YES")

tickets(antrian)
