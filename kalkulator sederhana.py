angka1 = int(input('Masukan angka pertama: '))
operator = input('Pilih salah satu operator ini: + - / * : ')
angka2 = int(input('Masukan angka kedua: '))

if operator == '+':
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')

elif operator == '-':
    hasil = angka1 - angka2
    print(f'{angka1} - {angka2} = {hasil}')

elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f'{angka1} / {angka2} = {hasil}')
    else:
        print('Pembagian dengan nol tidak diperbolehkan')

elif operator == '*':
    hasil = angka1 * angka2
    print(f'{angka1} * {angka2} = {hasil}')

else:
    print('Operator yang Anda masukan salah')