import random

daice1 = int(input("サイコロの面の数は?:"))
daice2 = int(input("何回振りますか?:"))

daice_list = []

for count in range(0, daice2):
    daice_list.append(random.randint(1, daice1))
print(daice_list)
