# SEQUENCE = Rangkaian, susunan, koleksi.  
# Di dalam pemrograman, kita bisa menyimpan banyak data di dalam sebuah wadah yang dinamakan Array

# LIST 
# Karakternya : Kurung siku []
list = [1,2,3,4]
print(type(list))

# KNOWING LENGTH OF LIST
# Kita bisa menggunakan len() untuk mengetahui panjang data dalam array
print(len(list))

# ACCESSING OF VALUE OF LIST
# Slicing adalah metode untuk mengakses sebuah atau lebih nilai di dalam list, kita harus paham namanya index.
# Index start from 0 (kita menggunakan Numerikal untuk mengambil sebuah data)
Huruf = ["M", "U", "I", "Z"]
print(Huruf[2])

# ACCESSING MULTI-VALUE OF LIST
# Dalam slicing, kita bisa memberikan tanda :

# ADDING A VALUE TO LIST
# Kita bisa menggunakan fungsi append() ataupun insert()
# Append = Hanya memerlukan nilai untuk ditambahkan (ditambahkan di akhir)
# Insert = Memerlukan index sebagai letak nilai diletakkan dan nilai itu sendiri
list1 = [1, 2, 3, 4]
list1.append(5)
print(list1)

# list1.insert()

# UPDATING VALUE FROM
# list[index] = nilai baru
list1[1] = "Hallo"
print(list1)

# DELETING A VALUE FROM LIST
# Kita bisa menggunakan del atau remove atau pop
# del = mengambil index
# remove = mengambil nilai
# pop = mengambil index, bedanya pada penulisan

# Buat sebuah variabel yang isinya ada list 

list = [1, 2, 3, 4, 5, 6, 4, 2, 3, 2, 5, 4, 7, 8, 4, 2, 3, 4, 6, 8]
print(list[2:-5:4])
print(len(list)-1) # index

# DICTIONARY
# Wadah = {key : value}
# Karakteristik : 1. Menggunakan {}, 2. Semua tipe data bisa dimasukkan ke dalam dictionary

# UPDATE DICTIONARY
# cara : 1. wadah[key yang udah ada] = nilai baru
#        2. wadah.update[key yang udah ada : nilai baru]

dict = {
    "Herzlich Willkommen" : "Selamat makan",
    "Geburstag" : "Hari Ulang Tahun",
    "Auf Wiedersehen" : "Sampai Jumpa",
    "Arigato" : "Makasih"
}
print("Dictionary sebelum diubah", dict)
print(f"Dictionary sebelum diubah {dict}")
dict["Herzlich Willkommen"] = "Selamat Pagi"               # jenis 1
print(f"Dictionary sesudah diubah {dict}")
dict.update({"Herzlich Willkommen" : "Selamat Datang"})    # jenis 2
print(f"Kamus Baru {dict}")
dict["Gute Nacht"] = "Selamat Tidur" # Jika key ada maka update, jika key belum ada maka tambah
print(f"Kamus Baru Lagi {dict}")

# DELETE VALUE
# Cara : 1. del, 2. pop
del dict["Arigato"]
print(f"Kamus Terbaru {dict}")
dict.pop("Auf Wiedersehen")
print(f"Kamus Terbaru2 {dict}")

# NOT IN AND IN
dict2 = {"Halo" : "Dunia"}
print("Halo" in dict2)
print("Dunia" not in dict2)

# COPYING DICT
dict3 = dict2.copy()
print(dict3)

fruits = {
    "fruits1" : "Pisang",
    "fruits2" : ["Timun", "Strawberry"]
}
print(fruits["fruits2"][1])
