# fungsi menghapus gadget atau comsumable
ID = 0
nama = 1
deskripsi = 2 
jumlahItem = 3
rarity = 4
tahun_ditemukan = 5

f = open("gadget.csv","r")
gadget_lines = f.readlines()
f.close()
gadget = [gadget_line.replace("\n", "") for gadget_line in gadget_lines]

d = open("consumable.csv","r")
consumable_lines = d.readlines()
d.close()
consumable = [consumable_line.replace("\n", "") for consumable_line in consumable_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(len(array_data)):
    if(i == jumlahItem):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == tahun_ditemukan):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def convert_line_to_data(line): 
    raw_array_of_data = line.split(";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def hapusindeks0(array):
    array_header = array.pop(0)
    header = convert_line_to_data(array_header)
    return header
    
header_gadget = hapusindeks0(gadget)
header_consumable = hapusindeks0(consumable)

data_gadget = []
for line in gadget:
    array_of_data_gadget = convert_line_to_data(line)
    real_values_of_gadget = convert_array_data_to_real_values(array_of_data_gadget)
    data_gadget.append(real_values_of_gadget)

data_consumable = []
for line in consumable:
    array_of_data_consumable = convert_line_to_data(line)
    real_values_of_consumable = convert_array_data_to_real_values(array_of_data_consumable)
    data_consumable.append(real_values_of_consumable)

cpy_data_gadget = data_gadget
cpy_data_consumable = data_consumable

def hapusitem(): # F6
    print(">>> hapusitem")
    while True:
        id = input("Masukan ID item: ")
        found = False

        idx1 = 0 # inisiasi
        while (found == False) and (idx1 < len(cpy_data_gadget)):
            if (cpy_data_gadget[idx1][ID] == id):
                found = True
                indeks = idx1
            else:
                idx1 = idx1 + 1

        idx2 = 0 # inisiasi
        while (found == False) and (idx2 < len(cpy_data_consumable)):
            if (cpy_data_consumable[idx2][ID] == id):
                found = True
                indeks = idx2
            else:
                idx2 = idx2 + 1

        if (found == True):
            if (cpy_data_gadget[indeks][ID] == id):
                item = cpy_data_gadget[indeks][nama]
                array_data = cpy_data_gadget
            elif (cpy_data_consumable[indeks][ID] == id):
                item = cpy_data_consumable[indeks][nama]
                array_data = cpy_data_consumable

            validasi = input("Apakah anda yakin ingin menghapus " + str(item) + " (Y/N)?")

            if (validasi == "Y"):
                array_data.pop(indeks)
                print("Item telah berhasil dihapus dari database.")

            else:
                print("Item dibatalkan untuk dihapus dari database.")

        else: # found == false
            print("Tidak ada item dengan ID tersebut")
        
        exit = input("Apakah anda sudah menghapus semua gadget atau consumable yang diinginkan (Y/N)?")

        if (exit == "Y"): # jika ingin keluar dari fungsi hapus item
            break

def hasilubahitem(hasil,jumlah,item,jumlah_item_awal): # fungsi antara 7
        if (hasil > 0):
            if (jumlah > 0):
                print(jumlah, item, "berhasilkan ditambahkan. Stok sekarang:", hasil)

            else: # jumlah < 0
                print(abs(jumlah), item, "berhasil dibuang. Stok sekarang:", hasil)

        else: # hasil < 0
            print(abs(jumlah), item, "gagal dibuang karena stok kurang. Stok sekarang:", jumlah_item_awal, "(<", abs(jumlah), ")" )

def ubahjumlah(): #F7
    print(">>> ubahjumlah")
    while True:
        id = input("Masukkan ID: ")
        found = False

        idx1 = 0 # inisiasi
        while (found == False) and (idx1 < len(cpy_data_gadget)):
            if (cpy_data_gadget[idx1][ID] == id):
                found = True
                indeks = idx1
            else:
                idx1 = idx1 + 1

        idx2 = 0 # inisiasi
        while (found == False) and (idx2 < len(cpy_data_consumable)):
            if (cpy_data_consumable[idx2][ID] == id):
                found = True
                indeks = idx2
            else:
                idx2 = idx2 + 1

        if (found == True):
            jumlah = int(input("Masukkan Jumlah: "))
            if (cpy_data_gadget[indeks][ID] == id):
                item = cpy_data_gadget[indeks][nama]
                jumlah_item_awal = cpy_data_gadget[indeks][jumlahItem]
                hasil = jumlah_item_awal + jumlah
                if (hasil > 0):
                    cpy_data_gadget[indeks][jumlahItem] = hasil
                hasilubahitem(hasil,jumlah,item,jumlah_item_awal) # prosedure hasil ubah item

            elif (cpy_data_consumable[indeks][0] == id):
                item = cpy_data_consumable[indeks][nama]
                jumlah_item_awal = cpy_data_consumable[indeks][jumlahItem]
                hasil = jumlah_item_awal + jumlah
                if (hasil > 0):
                    cpy_data_consumable[indeks][jumlahItem] = hasil
                hasilubahitem(hasil,jumlah,item,jumlah_item_awal) # prosedure hasil ubah item

        else: # found == False
            print("Tidak ada item dengan ID tersebut!")
        
        exit = input("Apakah anda sudah mengubah jumlah semua gadget atau consumable yang diinginkan (Y/N)?")

        if(exit == "Y"):
            break

