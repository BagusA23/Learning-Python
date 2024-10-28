data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

angka = [i**4 for i in range(0,10)]
print(angka)

list_if = [i for i in range(0,10) if i != 5]
print(list_if)

list_if = [i for i in range(0,10) if i%2 == 0]
print(list_if)

list_if = [i for i in range(0,10) if i%2 != 0]
print(list_if)