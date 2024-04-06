# Operator Aritmatika

a = 45.05
b = 21.34
print(a+b)

x = 5
y = 8
z = x + y
print(z)

r = True  # nilai true = 1, nilai false = 0 
s = False
print(r+s)
print(float(True))
print(r-s)
print(r*s)

print(a**b)
# istilah // adalah floor division

x = 62.3
y = 5
print(x//y)

# ASSIGNMENT OPERATOR
a = 5
a = a + 3
print(a)
# asynchronus

a += 3
a -= 3
a /= 2
a *= 4 
a **= 2
a %= 2
print(a)

variabel = a == 2 # tanda == adalah menyamadengankan nilai
print(variabel)

# STRING CONCATENATION
teks1 = "Hello"
teks2 = "world"
print(teks1+teks2)
print(teks1,teks2)
# perlu diperhatikan ketika memakai koma, apakah kita memanggil function atau tidak

# STRING REPLICATION
print(teks1*3)
print((teks1+"\n")*3) # backslash \ (new line)

# DATA CONVERSION (CASTING)
a = -5
print(str(a),type(str(a)))
print(float(a),type(float(a)))
print(bool(a),type(bool(a)))

# STRING SLICING 
a = "Hello"  # Dimulai dari indeks 0
print(a[2])
print(a[2:])
print(a[:4])
print(a[3:5])
print(a[::-1])

# STRING CHECKING
a = "Halo Nama Saya Budi"
print("Budi" in a)
print("Budi" not in a)

print([a]) # Dijadikan dalam satu array (Wadah)
print(list(a)) # Dicasting per huruf

# STRING METHOD
a = "Hello World"
print(a.upper())  # upper = huruf kapital
print(a.lower())  # lower = huruf kecil
print(a.split())
print(a.replace("o", "i"))

print(a.split("o"))

# NILAI ASCI
print(ord("A"))
print(chr(49))
print(chr(32)) # blank space
