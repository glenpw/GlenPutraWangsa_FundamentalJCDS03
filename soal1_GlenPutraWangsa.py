# soal 1
p0 = 0
percent = 0
aug = 0
p = 0
counter = 0

def nbYear(p0,percent, aug, p):
    pTemp = int(p0 + (p0 * (percent/100)) + aug)
    counter = 1
    while (pTemp<p):
        pTemp = int(pTemp + (pTemp * (percent/100)) + aug)
        counter += 1
    print("It will need {} entire years".format(counter))

p0 = int(input("population (0): "))
percent = int(input("percent (%): "))
aug  = int(input("inhabitants coming or leaving each year: "))
p = int(input("population to surpass: "))

nbYear(p0, percent, aug, p)   
