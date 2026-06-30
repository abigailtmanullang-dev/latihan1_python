import json

with open("harga.json", "r") as file:
    data = json.load(file)

def muat_data_menu():
    return data

def tampilkan_menu(data_menu):
    print("\n" + "="*45)
    print("                 JENIS DAGING")
    print("="*45)
    for key, value in data_menu["menu"].items():
        print(f"{key}. {value['nama']} (Rp. {value['harga']})")
    print("\n")

def hitung_diskon(jumlah, min_jumlah):
    if jumlah >= min_jumlah:
        if min_jumlah == 5: return 0.10  
        if min_jumlah == 2: return 0.15  
        if min_jumlah == 3: return 0.12  
    return 0

def jalankan_kasir():

    jumlah_a, jumlah_s, jumlah_b = 0, 0, 0
    total_a, total_s, total_b = 0, 0, 0
    harga_asli_a, harga_asli_s, harga_asli_b = 0, 0, 0

    data_menu = muat_data_menu()
    
    while True:
        tampilkan_menu(data_menu)
        pilihan = input("Masukkan pilihan menu (1/2/3) atau ketik 'cukup': ").lower()
        
        if pilihan == 'cukup':
            total = total_a + total_s + total_b
            print("\n" + "="*45)
            print("            STRUK PEMBELANJAAN")
            print("="*45)
            print (f"   ANDA MENDAPAT DISKON UNTUK PEMBELIAN")
            print("-"*45)
            if total_a >= 5:
                print(f"Ayam                    : 10%")
            else:
                print(f"Ayam                    : 0%")
            if total_s >= 2:
                print(f"Sapi                    : 15%")
            else:
                print(f"Sapi                    : 0%")
            if total_b >= 3:
                print(f"Babi                    : 12%")
            else:
                print(f"Babi                    : 0%")
            print("-"*45)
            print (f"   RINCIAN BELANJA ANDA SETELAH DISKON")
            print("-"*45)
            print(f"Ayam ({jumlah_a}kg) x  Rp. 10000    : Rp. {harga_asli_a:.0f}")
            print(f"Sapi ({jumlah_s}kg)  x  Rp. 12000    : Rp. {harga_asli_s:.0f}")
            print(f"Babi ({jumlah_b}kg)  x  Rp. 8000     : Rp. {harga_asli_b:.0f}")
            print("-"*45)
            print (f"   RINCIAN BELANJA ANDA SETELAH DISKON")
            print("-"*45)
            print(f"Ayam                : Rp. {total_a:.0f}")
            print(f"Sapi                : Rp. {total_s:.0f}")
            print(f"Babi                : Rp. {total_b:.0f}")
            print("-"*45)
            print(f"TOTAL AKHIR      : Rp. {total:.0f}")
            print("="*45)    
            break
            
        elif pilihan not in data_menu["menu"]:
            print("Maaf, menu tidak tersedia.")
            continue
        
        else:
            beli = float(input(f"Beli berapa kg {data_menu['menu'][pilihan]['nama']}? "))
            harga_per_kg = data_menu['menu'][pilihan]['harga']
            
            if pilihan == '1':
                jumlah_a += beli
                diskon = hitung_diskon(jumlah_a, 5)
                harga_asli_a= (jumlah_a * harga_per_kg) 
                total_a = (harga_asli_a) * (1 - diskon)
            elif pilihan == '2':
                jumlah_s += beli
                diskon = hitung_diskon(jumlah_s, 2)
                harga_asli_s= (jumlah_s* harga_per_kg) 
                total_s = (harga_asli_s) * (1 - diskon)
            elif pilihan == '3':
                jumlah_b += beli
                diskon = hitung_diskon(jumlah_b, 3)
                harga_asli_b= (jumlah_b * harga_per_kg) 
                total_b = (harga_asli_b) * (1 - diskon)
            
            total = total_a + total_s + total_b
            print("\n" + "="*45)
            print("            BELANJA ANDA SAAT INI")
            print("="*45)
            print (f"   ANDA MENDAPAT DISKON UNTUK PEMBELIAN")
            print("-"*45)
            if total_a >= 5:
                print(f"Ayam                    : 10%")
            else:
                print(f"Ayam                    : 0%")
            if total_s >= 2:
                print(f"Sapi                    : 15%")
            else:
                print(f"Sapi                    : 0%")
            if total_b >= 3:
                print(f"Babi                    : 12%")
            else:
                print(f"Babi                    : 0%")
            print("-"*45)
            print (f"   RINCIAN BELANJA ANDA SEBELUM DISKON")
            print("-"*45)
            print(f"Ayam ({jumlah_a}kg) x  Rp. 10000    : Rp. {harga_asli_a:.0f}")
            print(f"Sapi ({jumlah_s}kg)  x  Rp. 12000    : Rp. {harga_asli_s:.0f}")
            print(f"Babi ({jumlah_b}kg)  x  Rp. 8000     : Rp. {harga_asli_b:.0f}")
            print("-"*45)
            print (f"   RINCIAN BELANJA ANDA SETELAH DISKON")
            print("-"*45)
            print(f"Ayam             : Rp. {total_a:.0f}")
            print(f"Sapi             : Rp. {total_s:.0f}")
            print(f"Babi             : Rp. {total_b:.0f}")
            print("-"*45)
            print(f"TOTAL AKHIR      : Rp. {total:.0f}")
            print("="*45)

            
        
if __name__ == "__main__":
    jalankan_kasir()