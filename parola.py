import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    try:
        sifre_uzunlugu = int(input("Şifre uzunluğu: "))
        break  
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

sifre = ""
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)