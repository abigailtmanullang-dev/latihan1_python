a = 25000
print ("Harga 1 Kg ayam adalah Rp.", a)

b = int(input ("Anda ingin beli berapa Kg ayam? "))

if b > 5:
    print ("Anda mendapatkan diskon 7000")
    c = 7000

elif b >= 2:
    print ("Anda mendapatkan diskon 5000")
    c = 5000

else:
    print ("Anda tidak mendapatkan diskon")
    c = 0

d= a * b - c
print ("Total harga yang harus dibayar adalah Rp.", d)
e = int(input ("Masukkan jumlah uang yang anda miliki: Rp. "))


if e < d:
    print ("Uang anda tidak cukup untuk membeli ayam.")

else:
    f = e-d
    print ("Uang kembalian anda adalah Rp.", f)

