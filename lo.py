count  = int(input('masukan angka '))
sisi = 5
while True:
    if count % 2:
        print('*'*count)
        count +=1
        
    else:
        count += 1
        continue
    
    if count > sisi:
        break