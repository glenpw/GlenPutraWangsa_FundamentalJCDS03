# soal 3

size = int(input("Masukkan size: "))
z = ""
disp = 0
arr = [1]
hitung = 1

def angka():
    disp = 1
    for y in range(size):
        disp += 2
    return disp

def dispBintang(n):
    z = ''
    disp = 1 
    for num in range(n):
        for num1 in range(n-num-1):
            z += "  "
        for num2 in range(num+1):
            z += " {} ".format(disp)
            disp += 2
            arr.append(disp)
        z += "\n"
    print(z)

def rowSumOddNumbers(n) :  
    dispBintang(n)
    for i in range(n):
        hitung = 0
        for n in range(i+1):
            if (i == 0):
                hitung = 1
            else:
                hitung += arr[n+i]
        print(hitung)

rowSumOddNumbers(size)


