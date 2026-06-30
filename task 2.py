a = 25000
print ("Harga 1 Kg ayam adalah Rp.", a)

for i in range(1000000):
    b = input("Masukkan jumlah ayam (kg) atau ketik 'cukup' untuk selesai: ")

    if b.lower() == 'cukup':
        print("Proses dihentikan.")
        break
    
    try:
        jumlah = float(b)
        print(f"Anda memasukkan {b} kg.")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

print("Terima kasih telah berbelanja.")
    

c = int(input ("Ini pertanyaan sebenarnya, beli berapa kg ayam? "))
if c > 5:
    print ("Anda mendapatkan diskon 7000")
    d= 7000

elif c >= 2:
    print ("Anda mendapatkan diskon 5000")
    d = 5000

else:
    print ("Anda tidak mendapatkan diskon")
    d = 0

e= a * c - d
print ("Total harga yang harus dibayar adalah Rp.", e)
f = int(input ("Masukkan jumlah uang yang anda miliki: Rp. "))


if f < e:
    print ("Uang anda tidak cukup untuk membeli ayam.")
else:
    g = f-e
    print ("Uang kembalian anda adalah Rp.", g)

