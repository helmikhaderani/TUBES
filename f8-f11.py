f = open("gadget.csv","r")
gadget_lines = f.readlines()
f.close()
gadget = [gadget_line.replace("\n", "") for gadget_line in gadget_lines]

d = open("consumable.csv","r")
consumable_lines = d.readlines()
d.close()
consumable = [consumable_line.replace("\n", "") for consumable_line in consumable_lines]

c = open("consumable_history.csv","r")
chistory_lines = c.readlines()
c.close()
chistory = [chistory_line.replace("\n", "") for chistory_line in chistory_lines]

b = open("gadget_borrow_history.csv","r")
gborrow_lines = b.readlines()
b.close()
gborrow = [gborrow_line.replace("\n", "") for gborrow_line in gborrow_lines]

a = open("gadget_return_history.csv","r")
greturn_lines = a.readlines()
a.close()
greturn = [greturn_line.replace("\n", "") for greturn_line in greturn_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(len(array_data)):
    if(i == jumlah):
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
header_Chistory = hapusindeks0(chistory)
header_gborrow = hapusindeks0(gborrow)
header_greturn = hapusindeks0(greturn)

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

data_chistory = []
for line in chistory:
    array_of_data_chistory = convert_line_to_data(line)
    real_values_of_chistory = convert_array_data_to_real_values(array_of_data_chistory)
    data_chistory.append(real_values_of_chistory)

data_gborrow = []
for line in gborrow:
    array_of_data_gborrow = convert_line_to_data(line)
    real_values_of_gborrow = convert_array_data_to_real_values(array_of_data_gborrow)
    data_gborrow.append(real_values_of_gborrow)

data_greturn = []
for line in greturn :
    array_of_data_greturn = convert_line_to_data(line)
    real_values_of_greturn  = convert_array_data_to_real_values(array_of_data_greturn)
    data_greturn .append(real_values_of_greturn )

cpy_data_gadget = data_gadget
cpy_data_consumable = data_consumable
cpy_data_chistory = data_chistory
cpy_data_gborrow = data_gborrow
cpy_data_greturn = data_greturn

#f8/10

def hasilpeminjaman(hasil,jumlahitem,item,):
        if (hasil > 0):
            if (jumlahitem > 0):
                print(jumlahitem, item, "berhasil didapatkan")

            else: # jumlahitem < 0
                print("gagal")

        else: # hasil < 0
            print(item, "gagal didapatkan, stok kurang" )


def peminjaman_gadget():
    print(">>> peminjamangadget")
    while True:
        ID = input("Masukkan ID: ")
        found = False

        idx1 = 0 # inisiasi
        while (found == False) and (idx1 < len(cpy_data_gadget)):
            if (cpy_data_gadget[idx1][id] == ID):
                found = True
                indeks = idx1
            else:
                idx1 = idx1 + 1

        idx2 = 0 # inisiasi
        while (found == False) and (idx2 < len(cpy_data_consumable)):
            if (cpy_data_consumable[idx2][id] == ID):
                found = True
                indeks = idx2
            else:
                idx2 = idx2 + 1

        if (found == True):
            jumlahitem = int(input("Masukkan Jumlah: "))
            tanggal = input("Masukkan Tanggal : ")
            if (cpy_data_gadget[indeks][id] == ID):
                item = cpy_data_gadget[indeks][nama]
                jumlah_item_awal = cpy_data_gadget[indeks][jumlah]
                hasil = jumlah_item_awal - jumlahitem
                if (hasil >= 0):
                    cpy_data_gadget[indeks][jumlah] = hasil
                    cpy_data_gborrow[indeks][jumlah] = hasil , [indeks][tanggal_peminjaman]= tanggal , [indeks][id_gadget] = ID
                hasilpeminjaman(hasil,jumlahitem,item,)

            elif (cpy_data_consumable[indeks][id] == ID):
                item = cpy_data_consumable[indeks][nama]
                jumlah_item_awal = cpy_data_consumable[indeks][jumlah]
                hasil = jumlah_item_awal - jumlahitem
                if (hasil >= 0):
                    cpy_data_consumable[indeks][jumlah] = hasil
                    cpy_data_chistory[indeks][jumlah] = hasil , [indeks][tanggal_peminjaman]= tanggal , [indeks][id_consumable] = ID
                hasilpeminjaman(hasil,jumlahitem,item)
        else: # found == False
            print("Tidak ada item dengan ID tersebut!")

#f9

        if (hasil > 0):
            if (jumlahitem > 0):
                print(jumlahitem, item, "berhasil didapatkan")

            else: # jumlahitem < 0
                print("gagal")

        else: # hasil < 0
            print(item, "gagal didapatkan, stok kurang" )

def pengembalian_gadget():
    print(">>> pengembaliangadget")
    while True:
        ID = input("Masukkan ID: ")
        found = False

        idx1 = 0 # inisiasi
        while (found == False) and (idx1 < len(cpy_data_gadget)):
            if (cpy_data_gborrow[idx1][ID] == id):
                found = True
                indeks = idx1
            else:
                idx1 = idx1 + 1

        if (found == True):
            tanggal = input("Masukkan Tanggal : ")
            if (cpy_data_gborrow[indeks][id] == ID):
                item = cpy_data_gborrow[indeks][id_gadget]
                jumlah_item_dipinjam = cpy_data_gborrow[indeks][jumlah]
                jumlah_item_awal = cpy_data_gadget[indeks][jumlah]
                hasil = jumlah_item_dipinjam - jumlah_item_awal
                id_riwayat = cpy_data_gborrow[indeks][id]
                if (hasil >= 0):
                    cpy_data_gadget[indeks][jumlah] = hasil
                    cpy_data_gborrow[indeks][is_returned] = "sudah dikembalikan"
                    cpy_data_greturn[indeks][id_peminjaman] = id_riwayat , [indeks][tanggal_pengembalian] = tanggal
                print (jumlah_item_dipinjam, item, "berhasil dikembalikan")

        else: # found == False
            print("Tidak ada item dengan ID tersebut!")

#f11

def melihatriwa