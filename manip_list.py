
data = ["ucup","asep","bambang"]

# mengambil data
print(data[1])

# menghitung panjang data
print(len(data))

# menambahkan data sesuai posisi
data.insert(1,"bagus")
print(data)

# menabhkan data di posisi terakhir
data.append("ujang")
print(data)

# menambhkan list baru ke list lama
data_baru = ['lala','kiki']
data.extend(data_baru)
print(data)

# mengubah data
data[2] = "lala"
print(data)

data.remove("ucup")
print(data)

data.pop()
print(data)