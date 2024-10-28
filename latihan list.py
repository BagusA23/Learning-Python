
list_buku = []

while True:
    print("\nmasukan data buku ")
    judul = input("masukan judul buku \t: ")
    penulis =  input("masukan penulis buku \t: ")
    
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*20)
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t|{buku[0]}\t|{buku[1]}")
        
    lanjut = input("apakah anda ingin lanjut {y/n} : ")
    
    if lanjut == "n":
        break

print("PROGRAM SELESAI")