data1 = [1,2]
data2 = [3,4]

data_a = [data1,data2,10]
data_a_copy = data_a.copy()

print(f"data = {data_a}")

# mengambil data di nested list

data = data_a[0][0]
print(f"mengambil data {data}")

# addres

print(f"addres data {hex(id(data_a))}")
print(f"addres data {hex(id(data_a_copy))}")

print("mengambil data dari addres")

print(f"addres data {hex(id(data_a[0]))}")
print(f"addres data {hex(id(data_a_copy[0]))}")

data_a[1][0] = 5
data_a[2] = 9
print(f"data = {data_a}")
print(f"data = {data_a_copy}")

from copy import deepcopy

data_a = [data1,data2,]
dep_data = deepcopy(data_a)
print(f"addres data {hex(id(data_a))}")
print(f"addres data {hex(id(dep_data))}")

print("==================================")
data_a[1][0] = 30
print(f"addres data {hex(id(data_a[0]))}")
print(f"addres data {hex(id(dep_data[0]))}")

print(f"data = {data_a}")
print(f"data = {dep_data}")