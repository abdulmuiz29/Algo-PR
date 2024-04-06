# OPERASI KONDISI

# Kondisi True atau False bisa dihasilkan dari banyak hal antara lain :
# 1) Input nilai boolean
# 2) Hasil dari operasi matematika
# 3) Hasil dari operasi komparasi
# 4) Hasil dari operasi logika
# 5) Hasil dari inputan kondisi programmer sendiri

# syntaxnya :
# if{statement kondisi} :
# {indentasi} {code}
# Keterangan : jangan ditulis {}, indentasi = tab 1x atau spasi 4x

if True:
    print("halo")
if False:
    print("halo")

a = 5
b = 6
if a + b == 11:
    print("mantul")

a = 4
b = 6
if(a>b):
    print("oke")

a = 5
b = 6
if a > b and a == 1:
    print("a")

# STATEMENT

# STATEMENT IF-ELSE
# ketika ingin menjalankan program yang merupakan negasi dari kondisi awal
a = 1
b = 2
if a < b: #true
    print('a lebih kecil dari b')
else: #false
    print('a lebih besar dari b')

# STATEMENT IF-ELIF-ELSE (kondisi bertingkat)
# ketika ingin menjalankan program yang bukan negasi dari kondisi awal/tambahan kondisi aja
a = 1
b = 2
if a < b:
    print("a lebih kecil daripada b")
elif a == b:
    print("a sama dengan 1")
else :
    print("a lebih besar daripada b")

# KONDISI BERSARANG
# percabangan dalam percabangan
a = 1
if a > 0:
    if a < -5:
        print("benar")
    else:
        print("salah")


