
a = ["bagus","ucup","lala","dadang"]
print(a)

b = a
print(b)

a[1] = "asep"
b.sort()
print(a)
print(b)

print(hex(id(a)))
print(hex(id(b)))

# membuat list dengan copy

c = a.copy()
print(hex(id(c)))

print(a)
print(b)
print(c)

c[1] = "kiki"
print(a)
print(b)
print(c)