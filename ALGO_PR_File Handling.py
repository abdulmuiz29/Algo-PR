# f = open("FileHandlingCoba.txt", "x")   # membuat file
# WRITE
f = open("FileHandlingCoba.txt", "w")
konten = "Muiz Keren"
f.write(konten)

# APPEND
f = open("FileHandlingCoba.txt", "a")
konten = "\nKelas ALGO"
f.write(konten)

# READ
f = open("FileHandlingCoba.txt", "r")
print(f.read())
# print(f.readline())   # nampilin string biasa
# print(f.readlines())    # tipe data list jadi array
f.close()   # menghindari kerusakan dalam txt dan juga agar tidak memberatkan alokasi penyimpanan (memori)





