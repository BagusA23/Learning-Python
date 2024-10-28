
promp1 = int(input("masukan angka pertama : "))
promp2 = input("Pilih salah satu + - * / =")
promp3 = int(input("masukan angka kedua : "))

if promp2 == '+':
    hasil = promp1 + promp3

elif promp2 == '-':
    hasil = promp1 - promp3
    
elif promp2 == '*':
    hasil = promp1 * promp3
    
elif promp2 == '/':
    if promp3 != 0:
        hasil = promp1 / promp3
    else:
        print("maaf pembagian 0  tidak bisa dilakukan")
        exit()
    
else:
    print("maaf operator tidak ada")
    exit()
    
print("hasil nya adalah : ", hasil)