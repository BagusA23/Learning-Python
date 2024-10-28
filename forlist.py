
kumpulan_angka = [1,2,3,4,5,6,7,8,9]

for angka in kumpulan_angka:
    print(f"angka {angka}")
    
nama = ["dadang","dudung","lalang"]

for siapa in nama:
    print(f"kamu adalah {siapa}")
    
peserta1 = ['kiki',30,"perempuan"]
peserta2 = ["lala,",22,"perempuan"]

total_peserta = [peserta1,peserta2]

for peserta in total_peserta:
    print(f"nama kamu {peserta[0]}")
    print(f"umur kamu {peserta[1]}")
    print(f"jenis kelamin mu {peserta[2]}\n")
    
    
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"kumpulan angka {kumpulan_angka[i]}\n")
    
# while 
print("while loop")
kumpulan_angka = [1,2,3,4,5,6,7,8,9]
panjang = len(kumpulan_angka)
i = 0 

while i < panjang:
    print(f"kumpulan angka {kumpulan_angka[i]}\n")
    i+= 1
    
#list comprehensiod


print("list comprehansiod")

kumpulan_angka = [1,2,3,4,5,6,7,8,9]

[print(i) for i in kumpulan_angka]

#list enumare

print("list enumarete")

for index, data in enumerate(kumpulan_angka):
    print(f"index {index}, data {data}")