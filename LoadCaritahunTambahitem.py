# Ini asumsinya program ini diluar folder DaftarCSV
# Folder DaftarCSV isinya semua csv
import argparse
import os

# ==============================Bagian Load Data=============================
# Fungsi untuk mengecek path file
def is_valid_file(arg):
    if not os.path.exists(arg):
        return(False)
    else:
        return(True)

# Fungsi untuk konversi
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

def convert_array_data_to_real_value(path_csv, array, panjang_array):           # Ini belum lengkap
    temp_array = array
    for i in range(panjang_array):
        if path_csv == "DaftarCSV/user.csv" and i == 0:                                                        #Cuma berlaku buat user.csv
            temp_array[i] = int(temp_array[i])
        elif path_csv == "DaftarCSV/gadget.csv" and (i == 3 or i == 5):
            temp_array[i] = int(temp_array[i])
        elif path_csv == "DaftarCSV/consumable.csv" and i == 3:
            temp_array[i] = int(temp_array[i])
    return(temp_array)


# Fungsi untuk load csv
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
        real_value = convert_array_data_to_real_value(path_csv, array_of_data, len(header))
        datas.append(real_value)
    return(datas)

# Fungsi untuk cek validitas path folder
def load_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str)            # Input nama folder
    args = parser.parse_args()

    if not is_valid_file(args.nama_folder):                 # Jika nama folder tidak ada, output error
        return(False)
    else:
                                         # Jika nama folder ada, load semua csv
        user_header = csv_header("DaftarCSV/user.csv", 6)
        user_data = load_csv("DaftarCSV/user.csv")
        gadget_header = csv_header("DaftarCSV/gadget.csv", 5)
        gadget_data = load_csv("DaftarCSV/gadget.csv")
        consumable_header = csv_header("DaftarCSV/consumable.csv", 5)
        consumable_data = load_csv("DaftarCSV/consumable.csv")
        return(user_header, user_data, gadget_header, gadget_data, consumable_header, consumable_data)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ================================Bagian Cari Tahun=======================================
# Fungsi untuk cetak informasi gadget
def cetak_info_gadget(array_info_gadget):
    print("Nama :", array_info_gadget[1])
    print("Deskripsi :", array_info_gadget[2])
    print("Jumlah :", array_info_gadget[3], " buah")
    print("Rarity :", array_info_gadget[4])
    print("Tahun :", array_info_gadget[5])
    print()

# Fungsi untuk mencari informasi gadget sesuai tahun dan kategori
def caritahun(array_gadget):
    tahun = int(input("Masukkan tahun: "))
    kat = input("Masukkan kategori: ")
    frekuensi = 0
    while kat not in "<=" and kat not in ">=":
        print("Input kategori salah! Input Ulang!")
        print()
        tahun = int(input("Masukkan tahun: "))
        kat = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian:")
    print()
    for i in range(len(array_gadget)):
        if kat == ">" and array_gadget[i][5] > tahun:
            cetak_info_gadget(array_gadget[i])
            frekuensi += 1
        elif kat == ">=" and array_gadget[i][5] >= tahun:
            cetak_info_gadget(array_gadget[i])
            frekuensi += 1
        elif kat == "<" and array_gadget[i][5] < tahun:
            cetak_info_gadget(array_gadget[i])
            frekuensi += 1
        elif kat == "<=" and array_gadget[i][5] <= tahun:
            cetak_info_gadget(array_gadget[i])
            frekuensi += 1
        elif kat == "=" and array_gadget[i][5] == tahun:
            cetak_info_gadget(array_gadget[i])
            frekuensi += 1
    if frekuensi == 0:
        print("Tidak ada gadget yang ditemukan")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ================================Bagian Tambah Item=======================================
# Fungsi yang me-return ID yang valid dan unik
def input_ID(gadget_data_ID, consumable_data_ID):
    ID = input("Masukkan ID :")
    isNotValid = True
    while isNotValid:
        if ID[0] not in "GC":
            print()
            print("Gagal menambahkan item karena ID tidak valid")
            print("Input ulang")
            print()
            ID = input("Masukkan ID :")
        else:
            yangsama = 0
            if ID[0] == "G":
                for i in range(len(gadget_data_ID)):
                    if gadget_data_ID[i] == ID:
                        yangsama += 1
            elif ID[0] == "C":
                for i in range(len(consumable_data_ID)):
                    if consumable_data_ID[i] == ID:
                        yangsama += 1
            if yangsama == 0:
                isNotValid = False
            else:
                print()
                print("Gagal menambahkan item karena ID sudah ada")
                print("Input ID lagi!")
                print()
                ID = input("Masukkan ID :")
    return(ID)

# Fungsi yang mengurutkan ID barang
def sort_ID(array_barang_ID, array_barang):
    arrindeks = []

    for arr in array_barang_ID:
        indeks = int(arr[1:len(arr)])
        arrindeks.append(indeks)
    for i in range(len(arrindeks)):
        for j in range(len(arrindeks) - 1):
            if arrindeks[j] > arrindeks[j + 1]:
                arrindeks[j], arrindeks[j + 1] = arrindeks[j + 1], arrindeks[j]
                array_barang[j], array_barang[j + 1] = array_barang[j + 1], array_barang[j]
    return(array_barang)

# Prosedur tambah item
def tambahitem():
    gadget_data_ID = []
    consumable_data_ID = []
    for data_1_gadget in gadget_data:
        gadget_data_ID.append(data_1_gadget[0])
    for data_1_consum in consumable_data:
        consumable_data_ID.append(data_1_consum[0])

    ID = input_ID(gadget_data_ID, consumable_data_ID)
    nama_item = input("Masukkan Nama: ")
    deskripsi = input("Masukkan Deskripsi: ")
    jumlah = input("Jumlah: ")
    rarity = input("Rarity: ")
    item_baru = [ID, nama_item, deskripsi, jumlah, rarity]
    if ID[0] == "G":
        gadget_data_ID.append(ID)
        gadget_data.append(item_baru)
        sort_ID(gadget_data_ID, gadget_data)
    elif ID[0] == "C":
        consumable_data_ID.append(ID)
        consumable_data.append(item_baru)
        sort_ID(consumable_data_ID, consumable_data)
    print()
    print("Item telah berhasil ditambahkan ke database")
    print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if not load_data():
    print("Tidak ada nama folder yang diberikan!")
    print("Usage : python kantongajaib.py <nama_folder>")
else:
    print("Loading...")
    user_header, user_data = load_data()[0], load_data()[1]
    gadget_header, gadget_data = load_data()[2], load_data()[3]
    consumable_header, consumable_data = load_data()[4], load_data()[5]
    print("Selamat datang di %s" % '"Warung kopi"')
    perintah = input()
    if perintah == "caritahun":
        masihMau = True
        while masihMau:
            caritahun(gadget_data)
            masih = input("Masih ingin mencari tahun gadget? Y/N :")
            while masih not in "YyNn":
                print("Input salah! Input kembali!")
                masih = input("Masih ingin mencari tahun gadget? Y/N :")
            if masih in "Nn":
                masihMau = False
    elif perintah == "tambahitem":
        masihMau = True
        while masihMau:
            tambahitem()
            masih = input("Masih ingin menambahkan item? Y/N :")
            while masih not in "YyNn":
                print("Input salah! Input kembali!")
                masih = input("Masih ingin menambahkan item? Y/N :")
            if masih in "Nn":
                masihMau = False
    print("Makasih bro")
