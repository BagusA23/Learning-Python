
data0 = [1,2]
data1 = [3,4]

list1 = [data0,data1]
print(f"ini adalah list 1 {list1}")

print(list1[0][0])

pesera1 = ["ucup", 23,"laki-laki"]
pesera2 = ["asep", 21,"laki-laki"]
pesera3 = ["lala", 27,"perempuan"]

list_peserta = [pesera1,pesera2,pesera3]
print(hex(id(list_peserta)))
print(list_peserta)

# for peserta in list_peserta:
#     print(f"nama\t {peserta[0]}")
#     print(f"umur\t {peserta[1]}")
#     print(f"gender\t {peserta[2]}\n")
    

list_copy = list_peserta.copy()
print(hex(id(list_copy)))

list_peserta[0][2] = [9]
print(list_peserta)
print(hex(id(list_peserta[0])))
print(hex(id(list_copy[0])))

from copy import deepcopy

list_peserta = [pesera1,pesera2,pesera3]
print("depp copy")
print(hex(id(list_peserta)))