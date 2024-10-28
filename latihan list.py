
# list_buku = []

# while True:
#     print("\nmasukan data buku ")
#     judul = input("masukan judul buku \t: ")
#     penulis =  input("masukan penulis buku \t: ")
    
#     buku_baru = [judul,penulis]
#     list_buku.append(buku_baru)
    
#     print("\n\n","="*20)
#     for index, buku in enumerate(list_buku):
#         print(f"{index+1}\t|{buku[0]}\t|{buku[1]}")
        
#     lanjut = input("apakah anda ingin lanjut {y/n} : ")
    
#     if lanjut == "n":
#         break

# print("PROGRAM SELESAI")
def tambah_buku(list_buku):
    print("\nMasukan data buku ")
    judul = input("Masukan judul buku \t: ")
    penulis =  input("Masukan penulis buku \t: ")
    
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

def tampilkan_buku(list_buku):
    print("\n\n","="*20)
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t|{buku[0]}\t|{buku[1]}")

def main():
    list_buku = []
    while True:
        tambah_buku(list_buku)
        tampilkan_buku(list_buku)
        lanjut = input("Apakah anda ingin lanjut {y/n} : ")
        if lanjut.lower() == "n":
            break
    print("PROGRAM SELESAI")

if __name__ == "__main__":
    main()