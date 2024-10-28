"""
    program nilai mahasiswa
    dibuat oleh     : bagus ardiansyah
    tanggal         : 02-11-2023
"""

bagus_npm = input("nomor induk mahasiswa : ")
bagus_nama = input("nama mahasiswa : ")

bagus_tugas_kelas1 = float(input("nilai tugas kelas 1 : "))
bagus_tugas_kelas2 = float(input("nilai tugas kelas 2 : "))
bagus_tugas_kelas3 = float(input("nilai tugas kelas 3 : "))
bagus_tugas_kelas4 = float(input("nilai tugas kelas 4 : "))
bagus_tugas_kelas5 = float(input("nilai tugas kelas 5 : "))
bagus_tugas_kelas6 = float(input("nilai tugas kelas 6 : "))
bagus_tugas_kelas7 = float(input("nilai tugas kelas 7 : "))

#tugas kelas 40%
hasil = (bagus_tugas_kelas1 + bagus_tugas_kelas2 + bagus_tugas_kelas3 + bagus_tugas_kelas4 + bagus_tugas_kelas5 + bagus_tugas_kelas6 + bagus_tugas_kelas7) / 7
bagus_rata_rata_hasil = hasil * 0.4
print("nilai tugas kelas : ", bagus_rata_rata_hasil)

#tugas mandiri 20%
bagus_tugas_mandiri = float(input("nilai tugas mandiri : "))
bagus_rata_rata_hasil1= bagus_tugas_mandiri * 0.2
print("nilai tugas mandiri [20%] ", bagus_rata_rata_hasil1)

#ujian tengah semester 20%
bagus_UTS = float(input("nilai ujian tengah semester : "))
bagus_UTS_hasil = bagus_UTS * 0.2
print("Nilai ujian tengah semester [20%] : ", bagus_UTS_hasil)

#nilai akhir semester 20%
bagus_nilai_akhir = float(input("Nilai ujian akhir semester : "))
bagus_nilai_akhir_hasil = bagus_nilai_akhir * 0.2
print("Nilai akhir semester [20%] : ",bagus_nilai_akhir_hasil)

#nilai akhir semua ditambahkan 
bagus_akhir = bagus_rata_rata_hasil + bagus_nilai_akhir_hasil + bagus_UTS_hasil + bagus_nilai_akhir_hasil
print("Nilai akhir mahasisiswa : ", bagus_akhir)


if bagus_akhir >= 81 and bagus_akhir <= 100:
    print("Nilai huruf = A")
    print("Predikat = sangat baik")

elif bagus_akhir >= 70 and bagus_akhir <=81:
    print("Nilai huruf = B")
    print("Predikat  = baik")

elif bagus_akhir >= 56 and bagus_akhir <=70:
    print("Nilai huruf = c")
    print("Predikat = cukup")

elif bagus_akhir >= 50 and bagus_akhir <= 40:
    print("Nilai huruf = D")
    print("Predikat = kurang baik")

else:
    print("Nilai huruf = E")
    print("Predikat = sangat kurang baik")