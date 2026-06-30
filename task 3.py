price_list = { 
    "ayam", 150000,
    "sapi", 12000,
    "babi", 10000,
}

jumlah_a = 0
jumlah_s = 0
jumlah_b = 0
total_a = 0
total_s = 0
total_b = 0

print("Silakan pilih daging yang tersedia:")
print ("1. Ayam (min. 5kg) : Diskon 10%")
print("2. Sapi (min. 2kg) : Diskon 15%")
print("3. Babi (min. 3kg) : Diskon 12%")    
print("Jika ingin berhenti, ketik 'cukup'.")

while True:
    daging = str(input ("Anda ingin beli daging apa? ").lower())

    if daging == 'cukup':
        print("Terimakasih, mari kita hitung total belanja anda.")
        total = total_a + total_s + total_b
        print("\n" + "="*45)
        print("             STRUK PEMBELANJAAN")
        print("="*45)
        print(f"Ayam ({jumlah_a}kg)     : Rp. {total_a:}")
        print(f"Sapi ({jumlah_s}kg)     : Rp. {total_s:}")
        print(f"Babi ({jumlah_b}kg)     : Rp. {total_b:}")
        print("-"*45)
        print(f"TOTAL AKHIR      : Rp. {total:}")
        print("="*45)
        print("  Terima Kasih telah berbelanja!  ")
        break
    
    elif daging not in price_list:
        print("Maaf, daging yang Anda pilih tidak tersedia.")
        print("Silakan pilih daging yang tersedia: ayam, sapi, atau babi.")
        print("Jika ingin berhenti, ketik 'cukup'.\n\n")
        continue

    else:
        if daging == 'ayam':
            beli = float(input ("Anda ingin beli berapa Kg ayam? "))
            jumlah_a += beli
            print (f"Sekarang anda membeli {jumlah_a} Kg ayam.")
            if jumlah_a>=5:
                print ("Anda mendapatkan diskon 10%.")
                diskon_a=0.10
            else:
                print ("Tidak ada diskon untuk pembelian ini.")
                diskon_a=0
            total_a = price_list['ayam'] * jumlah_a - (price_list[daging] * jumlah_a * diskon_a)
            print (f"Total harga ayam yang harus dibayar adalah Rp. {total_a}.\n\n")

        elif daging == "sapi":
            beli = float(input ("Anda ingin beli berapa Kg sapi? "))
            jumlah_s += beli
            print (f"Sekarang anda membeli {jumlah_s} Kg sapi.")
            if jumlah_s >=2:
                print ("Anda mendapatkan diskon 15%.")
                diskon=0.15
            else:
                print ("Tidak ada diskon untuk pembelian ini.")
                diskon=0
            total_s = price_list['sapi'] * jumlah_s - (price_list[daging] * jumlah_s * diskon)
            print (f"Total harga sapi yang harus dibayar adalah Rp. {total_s}.\n\n")
        
        else:
            beli = float(input ("Anda ingin beli berapa Kg babi? "))
            jumlah_b += beli
            print (f"Sekarang anda membeli {jumlah_b} Kg babi.")
            if jumlah_b >=3:
                print ("Anda mendapatkan diskon 12%.")
                diskon=0.12
            else:
                print ("Tidak ada diskon untuk pembelian ini.")
                diskon=0
            total_b = price_list['babi'] * jumlah_b - (price_list[daging] * jumlah_b * diskon)
            print (f"Total harga babi yang harus dibayar adalah Rp. {total_b}.\n\n")
            

    
