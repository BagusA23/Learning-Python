
angka1 = int(input('masukan angka pertama '))
operator = input('pilih salah satu operator ini + - / * : ')
angka2 = int(input('masukan angka pertama '))

if operator == '+':
    hasil = angka1 + angka2

    
elif operator == '-':
    hasil = angka1 - angka2

    
elif operator == '/':
    hasil = angka1 / angka2


elif operator == '*':
    hasil = angka1 * angka2

    
else:
    print('operator yang anda masukan salah')
    
print(hasil)