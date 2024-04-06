# def penjumlahan(a, b):
#     print(a+b)

# #? Pemanggilan function
# penjumlahan(2, 9)

# def urutan(a, b):
#     print(a)
#     print(b)

# urutan(b=1, a=2)

# # NILAI DEFAULT
# def default(c = 1, d = 2):
#     print(c)
#     print(d)

# default(d = 7) 

# return itu menyimpan nilai dalam function, tidak langsung menampilkan nilai dalam terminal

# def penjumlahan(a = 2, b =1):
#     c = max(a,b)
#     print(c)
#     return c

# penjumlahan()

def factorial(n):
    if n == 1:      # BASE CASE
        return n    # Berhenti
    else:
        return n * factorial(n - 1)

print(factorial(5))

