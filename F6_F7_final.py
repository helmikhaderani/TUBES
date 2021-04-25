# fungsi menghapus gadget atau comsumable
ID = 0
nama = 1
deskripsi = 2 
jumlahItem = 3
rarity = 4
tahun_ditemukan = 5

# ==============================Bagian Load Data=============================
def convert_line_to_data(array, banyak_kategori):
    list = []
    for teks in array:
        for karakter in teks:
            list.append(karakter)
    arraybaru = []
    count = 1
    string = list[0]
    list[0] = ";"
    for i in range(banyak_kategori):
        while (list[count] != ";") and (count < len(list) - 1):
            string += list[count]
            list[count] = ";"
            count += 1
        if count == len(list) - 1:
            string += list[count]
            arraybaru.append(string)
            return (arraybaru)
        arraybaru.append(string)
        string = ""
        count += 1
    return(arraybaru)

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(len(array_data)):
    if(i == jumlahItem):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == tahun_ditemukan):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def csv_header(path_csv, banyak_kategori):
    f = open(path_csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header, banyak_kategori)
    return(header)

def load_csv(path_csv):
    f = open(path_csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header, len(raw_header))

    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line, len(header))
        real_value = convert_array_data_to_real_values(array_of_data)
        datas.append(real_value)
    return(datas)
# ==============================Load gadget.csv dan consumable.csv=============================

gadget = load_csv("gadget.csv")
consumable = load_csv("consumable.csv")

# ================================= Fungsi Antara 6 dan 7 =====================================

def cek_valid_id(data,id):
    found = False
    idx = 0 # inisiasi
    while (found == False) and (idx < len(data)):
        if (data[idx][ID] == id):
            found = True
        else:
            idx = idx + 1
    return found

def cari_indeks_id(data,id):
    for i in range (len(data)):
        if (data[i][ID] == id ):
            return i

# ============================== Fungsi Antara 6 =============================

def validasi_hapus(indeks,array_data,item):
    validasi = input("Apakah anda yakin ingin menghapus " + str(item) + " (Y/N)?")

    if (validasi == "Y"):
        array_data.pop(indeks)
        print("Item telah berhasil dihapus dari database.")

    else:
        print("Item dibatalkan untuk dihapus dari database.")

# =============================== hapus item =================================
def hapusitem(data_gadget,data_consumable): # F6
    print(">>> hapusitem")
    while True:
        id = input("Masukan ID item: ")

        
        if (cek_valid_id(data_gadget,id) == True):
            indeks = cari_indeks_id(data_gadget,id)
            item = data_gadget[indeks][nama]
            array_data = data_gadget
            validasi_hapus(indeks,array_data,item)

        elif (cek_valid_id(data_consumable,id) == True):
            indeks = cari_indeks_id(data_consumable,id)
            item = data_consumable[indeks][nama]
            array_data = data_consumable
            validasi_hapus(indeks,array_data,item)

        else:
            print("Tidak ada item dengan ID tersebut")
        
        exit = input("Apakah anda sudah menghapus semua gadget atau consumable yang diinginkan (Y/N)?")

        if (exit == "Y"): # jika ingin keluar dari fungsi hapus item
            break
    return (data_consumable,data_gadget)

# ============================== fungsi antara 7 =============================

def hasilubahitem(hasil,jumlah,item,jumlah_item_awal): # fungsi antara 7
        if (hasil > 0):
            if (jumlah > 0):
                print(jumlah, item, "berhasilkan ditambahkan. Stok sekarang:", hasil)

            else: # jumlah < 0
                print(abs(jumlah), item, "berhasil dibuang. Stok sekarang:", hasil)

        else: # hasil < 0
            print(abs(jumlah), item, "gagal dibuang karena stok kurang. Stok sekarang:", jumlah_item_awal, "(<", abs(jumlah), ")" )

# ============================== fungsi 7 =============================

def ubahjumlah(data_gadget,data_consumable): 
    print(">>> ubahjumlah")
    while True:
        id = input("Masukkan ID: ")

        if ((cek_valid_id(data_gadget,id) == True) or (cek_valid_id(data_consumable,id) == True)):
            jumlah = int(input("Masukkan Jumlah: "))
            if (cek_valid_id(data_gadget,id) == True):
                indeks = cari_indeks_id(data_gadget,id)
                item = data_gadget[indeks][nama]
                jumlah_item_awal = data_gadget[indeks][jumlahItem]
                hasil = jumlah_item_awal + jumlah
                if (hasil > 0):
                    data_gadget[indeks][jumlahItem] = hasil
                hasilubahitem(hasil,jumlah,item,jumlah_item_awal) # prosedure hasil ubah item

            elif (cek_valid_id(data_consumable,id) == True):
                indeks = cari_indeks_id(data_consumable,id)
                item = data_consumable[indeks][nama]
                jumlah_item_awal = data_consumable[indeks][jumlahItem]
                hasil = jumlah_item_awal + jumlah
                if (hasil > 0):
                    data_consumable[indeks][jumlahItem] = hasil
                hasilubahitem(hasil,jumlah,item,jumlah_item_awal) # prosedure hasil ubah item

        else: # found == False
            print("Tidak ada item dengan ID tersebut!")
        
        exit = input("Apakah anda sudah mengubah jumlah semua gadget atau consumable yang diinginkan (Y/N)?")

        if(exit == "Y"):
            break

    return (data_consumable,data_gadget)

hapusitem(gadget,consumable)
ubahjumlah(gadget,consumable)
print(gadget)
print(consumable)