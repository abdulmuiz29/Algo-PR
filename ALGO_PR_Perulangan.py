# kondisi = True

# while kondisi:
#     print('aku tampan')
#     kondisi = False

# print('meong!')

# while True:
#     print('hai')
#     continue
#     print('aku tampan')

# break = memberhentikan pengulangan
# continue = memberhentikan pengulangan yang ada di bawahnya

list = [1, 2, 3, 4, 5, 6]
for idx, i in enumerate(list):
    print(f"perulangan ke-{idx + 1} adalah {i}")

for i in range(1, 5): # start dari 1, end < 5
    print(i)

list = [1, 2, 3, 4, 5, 6]
for i in range(0, len(list)):
    print(list[i])

list = [1, 2, 3, 4, 5, 6]
while i in range(0,3):
    list.append(i)

print(list)

#   NESTED LOOP
# 1. while dalam while
# 2. for dalam for

i = 1
while i < 5:
    j = 1
    while j < 5:
        print(i * j, end=" ")
        j += 1
    i += 1
    print()
print("\n")

for i in range(0,5):
    for j in range(0,5):
        print(f"Pasangan {i} adalah {j}")


