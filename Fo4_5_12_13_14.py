# Ini asumsinya program ini diluar folder DaftarCSV
# Folder DaftarCSV isinya semua csv
import argparse
import os
import time

# ==============================Bagian Load Data=============================
# Fungsi untuk mengecek path file
def is_valid_file(arg):
    if not os.path.exists(arg):
        return(False)
    else:
        return(True)

# Fungsi untuk konversi
def convert_line_to_data(array, banyak_kategori, pemisah):
    list = []
    for teks in array:
        for karakter in teks:
            list.append(karakter)
    arraybaru = []
    count = 1
    string = list[0]
    list[0] = pemisah
    for i in range(banyak_kategori):
        while (list[count] != pemisah) and (count < len(list) - 1):
            string += list[count]
            list[count] = pemisah
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
        elif (path_csv == "DaftarCSV/consumable_history.csv" or path_csv == "DaftarCSV/gadget_borrow_history.csv") and i == 4:     # Aku asumsi IDnya ada huruf misalnya CH1, CH2
            temp_array[i] = int(temp_array[i])
    return(temp_array)


# Fungsi untuk load csv
def csv_header(path_csv, banyak_kategori):
    f = open(path_csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header, banyak_kategori, ";")
    return(header)

def load_csv(path_csv):
    f = open(path_csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header, len(raw_header), ";")

    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line, len(header), ";")
        real_value = convert_array_data_to_real_value(path_csv, array_of_data, len(header))
        datas.append(real_value)
    return(datas)

# Fungsi untuk menampung data ke variabel
def tampung_data():
    global user_header, user_data, gadget_header, gadget_data, consumable_header, consumable_data
    # global gadget_borrow_history_header, gadget_borrow_history
    global consumable_history_header, consumable_history, gadget_return_history_header, gadget_return_history
    user_header = csv_header("DaftarCSV/user.csv", 6)
    user_data = load_csv("DaftarCSV/user.csv")
    gadget_header = csv_header("DaftarCSV/gadget.csv", 5)
    gadget_data = load_csv("DaftarCSV/gadget.csv")
    consumable_header = csv_header("DaftarCSV/consumable.csv", 5)
    consumable_data = load_csv("DaftarCSV/consumable.csv")
    consumable_history_header = csv_header("DaftarCSV/consumable_history.csv", 5)
    consumable_history = load_csv("DaftarCSV/consumable_history.csv")
    #gadget_borrow_history_header = csv_header("DaftarCSV/gadget_borrow_history.csv", 6)    # Aku jadiin komentar dlu karna blum kepake
    #gadget_borrow_history = load_csv("DaftarCSV/gadget_borrow_history.csv")                # Aku jadiin komentar dlu karna blum kepake
    gadget_return_history_header = csv_header("DaftarCSV/gadget_return_history.csv", 3)
    gadget_return_history = load_csv("DaftarCSV/gadget_return_history.csv")


# Fungsi untuk cek validitas path folder
def load_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str)            # Input nama folder
    args = parser.parse_args()

    if not is_valid_file(args.nama_folder):                 # Jika nama folder tidak ada, output error
        print("Tidak ada nama folder yang diberikan!")
        print("Usage : python kantongajaib.py <nama_folder>")
    else:                                                   # Jika nama folder ada, load semua csv
        print("Loading...")
        time.sleep(3)
        tampung_data()
        print("Selamat datang di %s" % '"Warung kopi"')
        time.sleep(1)
        program_utama()
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
        if ID[0] != "G" and ID[0] != "C":
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

# ================================Bagian Melihat Riwayat Pengambilan Consumable=======================================
# Fungsi yang mencari indeks lokasi nilai maks sebuah elemen dalam array dari indeks_mulai sampai indeks_akhir
def findIMax(array, indeks_mulai, indeks_akhir):
    IMax = indeks_mulai
    Maks = int(array[indeks_mulai])
    for i in range(indeks_mulai, indeks_akhir):
        if int(array[i]) > Maks:
            Maks = int(array[i])
            IMax = i
    return(IMax)

# Fungsi yang menghasilkan hanya daftar tanggal dari riwayat pengambilan Consumable
def obtain_array_tanggal_pengembalian_consumable(array):
    date = []
    for i in range(len(array)):
        date.append(array[i][3])
    return(date)

# Fungsi yang mengurutkan tanggal secara descending
def sort_tanggal(array_tanggal, array_histori):
    arr_tgl = []
    arr_bln = []
    arr_thn = []
    for tanggal in array_tanggal:
        arr_tanggal = convert_line_to_data(tanggal, len(tanggal), "/")
        arr_tgl.append(arr_tanggal[0])
        arr_bln.append(arr_tanggal[1])
        arr_thn.append(arr_tanggal[2])

    # Mengurutkan tahun
    for i in range(len(array_tanggal)):
        indeks = findIMax(arr_thn, i, len(arr_thn))
        arr_thn[i], arr_thn[indeks] = arr_thn[indeks], arr_thn[i]
        arr_bln[i], arr_bln[indeks] = arr_bln[indeks], arr_bln[i]
        arr_tgl[i], arr_tgl[indeks] = arr_tgl[indeks], arr_tgl[i]
        array_tanggal[i], array_tanggal[indeks] = array_tanggal[indeks], array_tanggal[i]
        array_histori[i], array_histori[indeks] = array_histori[indeks], array_histori[i]

    # Mengurutkan bulan
    for k in range(len(array_tanggal)):
        for i in range(len(array_tanggal) - 1):
            if (int(arr_bln[i]) < int(arr_bln[i + 1])) and (int(arr_thn[i]) == int(arr_thn[i + 1])):
                arr_thn[i], arr_thn[i + 1] = arr_thn[i + 1], arr_thn[i]
                arr_bln[i], arr_bln[i + 1] = arr_bln[i + 1], arr_bln[i]
                arr_tgl[i], arr_tgl[i + 1] = arr_tgl[i + 1], arr_tgl[i]
                array_tanggal[i], array_tanggal[i + 1] = array_tanggal[i + 1], array_tanggal[i]
                array_histori[i], array_histori[i + 1] = array_histori[i + 1], array_histori[i]

    # Mengurutkan hari
    for k in range(len(array_tanggal)):
        for i in range(len(array_tanggal) - 1):
            if (int(arr_tgl[i]) < int(arr_tgl[i + 1])) and (int(arr_bln[i]) == int(arr_bln[i + 1])) and (int(arr_thn[i]) == int(arr_thn[i + 1])):
                arr_thn[i], arr_thn[i + 1] = arr_thn[i + 1], arr_thn[i]
                arr_bln[i], arr_bln[i + 1] = arr_bln[i + 1], arr_bln[i]
                arr_tgl[i], arr_tgl[i + 1] = arr_tgl[i + 1], arr_tgl[i]
                array_tanggal[i], array_tanggal[i + 1] = array_tanggal[i + 1], array_tanggal[i]
                array_histori[i], array_histori[i + 1] = array_histori[i + 1], array_histori[i]
    return(array_histori)

# Fungsi yang mencetak riwayat pengambilan suatu consumable
def cetak_history_pengambilan(consumable_history, indeks_mulai, indeks_akhir):
    print()
    for i in range(indeks_mulai, indeks_akhir):
        print("ID Pengembalian :", consumable_history[i][0])
        print("Nama Pengambil :", consumable_history[i][1])
        print("Nama Gadget :", consumable_history[i][2])
        print("Tanggal Pengembalian :", consumable_history[i][3])
        print()

# Prosedur riwayatambil
def riwayatambil(consumable_history):
    if consumable_history == []:
        print("Tidak ada riwayat pengambilan Consumable")
    else:
        consumable_history = sort_tanggal(obtain_array_tanggal_pengembalian_consumable(consumable_history), consumable_history)
        if len(consumable_history) <= 5:
            cetak_history_pengambilan(consumable_history, 0, len(consumable_history))
        else:
            cetak_history_pengambilan(consumable_history, 0, 5)
            cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            while cetaklagi not in "YyNn":
                print("Input salah!")
                cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            if cetaklagi in "Yy":
                if len(consumable_history) <= 10:
                    cetak_history_pengambilan(consumable_history, 5, len(consumable_history))
                else:
                    cetak_history_pengambilan(consumable_history, 5, 10)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ================================Bagian Melihat Riwayat Pengembalian Gadget=======================================

# Fungsi yang menghasilkan hanya daftar tanggal dari riwayat pengembalian gadget
def obtain_array_tanggal_pengembalian_gadget(array):
    date = []
    for i in range(len(array)):
        date.append(array[i][2])
    return(date)

# Fungsi yang mencetak riwayat pengambilan suatu consumable
def cetak_history_pengembalian(gadget_history, indeks_mulai, indeks_akhir):
    print()
    for i in range(indeks_mulai, indeks_akhir):
        print("ID Pengembalian :", gadget_history[i][0])
        print("ID Peminjaman :", gadget_history[i][1])
        print("Tanggal Pengembalian :", gadget_history[i][2])
        print()

# prosedur riwayatkembali
def riwayakembali(gadget_return_history):
    if gadget_return_history == []:
        print("Tidak ada riwayat pengambilan Consumable")
    else:
        gadget_return_history = sort_tanggal(obtain_array_tanggal_pengembalian_gadget(gadget_return_history), gadget_return_history)
        if len(gadget_return_history) <= 5:
            cetak_history_pengembalian(gadget_return_history, 0, len(consumable_history))
        else:
            cetak_history_pengembalian(gadget_return_history, 0, 5)
            cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            while cetaklagi not in "YyNn":
                print("Input salah!")
                cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            if cetaklagi in "Yy":
                if len(consumable_history) <= 10:
                    cetak_history_pengambilan(consumable_history, 5, len(consumable_history))
                else:
                    cetak_history_pengambilan(consumable_history, 5, 10)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## ================================Bagian Program Utama=======================================
def program_utama():
    perintah = input(">>>")
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
    elif perintah == "riwayatambil":
        masihMau = True
        while masihMau:
            riwayatambil(consumable_history)
            masih = input("Masih ingin melihat histori pengambilan consumable? Y/N :")
            while masih not in "YyNn":
                print("Input salah! Input kembali!")
                masih = input("Masih ingin melihat histori pengambilan consumable? Y/N :")
            if masih in "Nn":
                masihMau = False
    elif perintah == "riwayatkembali":
        masihMau = True
        while masihMau:
            riwayakembali(gadget_return_history)
            masih = input("Masih ingin melihat histori pengambilan consumable? Y/N :")
            while masih not in "YyNn":
                print("Input salah! Input kembali!")
                masih = input("Masih ingin melihat histori pengambilan consumable? Y/N :")
            if masih in "Nn":
                masihMau = False
    print("Makasih bro")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

load_data()
