# Ini asumsinya program ini diluar folder DaftarCSV
# Folder DaftarCSV isinya semua csv
import argparse
import os
import time
import datetime

# ==============================Bagian Load Data=============================
# Fungsi untuk mengecek path file

Login = False
role = 'none'
user_id = 0
user_username = 'none'

#KAMUS
ID_ = 0
nama = 1
deskripsi = 2 
jumlahItem = 3
rarity = 4
tahun_ditemukan = 5
#================================

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
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str)            # Input nama folder
    args = parser.parse_args()

    temp_array = array
    for i in range(panjang_array):
        if path_csv == "%s/user.csv" % args.nama_folder and i == 0:                                                    
            temp_array[i] = int(temp_array[i])
        elif path_csv == "%s/gadget.csv" % args.nama_folder and (i == 3 or i == 5):
            temp_array[i] = int(temp_array[i])
        elif path_csv == "%s/consumable.csv" % args.nama_folder and i == 3:
            temp_array[i] = int(temp_array[i])
        elif (path_csv == "%s/consumable_history.csv" % args.nama_folder or path_csv == "%s/gadget_borrow_history.csv" % args.nama_folder) and i == 4:     # Aku asumsi IDnya ada huruf misalnya CH1, CH2
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


# Fungsi untuk cek validitas path folder
def load_data():
    global user_header, user_data, gadget_header, gadget_data, consumable_header, consumable_data
    global gadget_borrow_history_header, gadget_borrow_history
    global consumable_history_header, consumable_history, gadget_return_history_header, gadget_return_history

    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', type=str)            # Input nama folder
    args = parser.parse_args()

    if not is_valid_file(args.nama_folder):                 # Jika nama folder tidak ada, output error
        return (False)
    else:
        user_header = csv_header("%s/user.csv" % args.nama_folder, 6)
        user_data = load_csv("%s/user.csv" % args.nama_folder)
        gadget_header = csv_header("%s/gadget.csv" % args.nama_folder, 5)
        gadget_data = load_csv("%s/gadget.csv" % args.nama_folder)
        consumable_header = csv_header("%s/consumable.csv" % args.nama_folder, 5)
        consumable_data = load_csv("%s/consumable.csv" % args.nama_folder)
        consumable_history_header = csv_header("%s/consumable_history.csv" % args.nama_folder, 5)
        consumable_history = load_csv("%s/consumable_history.csv" % args.nama_folder)
        gadget_borrow_history_header = csv_header("%s/gadget_borrow_history.csv" % args.nama_folder, 6)    # Aku jadiin komentar dlu karna blum kepake
        gadget_borrow_history = load_csv("%s/gadget_borrow_history.csv" % args.nama_folder)                # Aku jadiin komentar dlu karna blum kepake
        gadget_return_history_header = csv_header("%s/gadget_return_history.csv" %args.nama_folder, 3)
        gadget_return_history = load_csv("%s/gadget_return_history.csv" % args.nama_folder)
        return (True)
    

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F01 : Register ======================================================================================

def register (user_data, user_header):
    unique = True
    new_user_idx = user_data[-1][0] + 1
    raw_new_user_nama = input("Masukkan nama = ")
    new_user_username = input("Masukkan username = ")
    new_user_password = input("Masukkan password = ")
    new_user_alamat = input("Masukkan alamat = ")
    new_user_role = 'user'

    new_user_nama = raw_new_user_nama.title()

    for data in user_data :
        if new_user_username == data[1]:
            unique = False
    
    if unique == True :
        new_user = [new_user_idx, new_user_username, new_user_nama, new_user_alamat, new_user_password, new_user_role]

        user_data.append(new_user)

        string_data = ";".join(user_header) + "\n"
        for arr_data in user_data :
            arr_data_all_string = [str(var) for var in arr_data]
            string_data += ";".join(arr_data_all_string)
            string_data += "\n"

        
    elif unique == False :
        print ("Username sudah digunakan. Silahkan input username berbeda")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F02 : Login =======================================================================================

def login(user_data) :
    global role
    global user_id, user_username
    fill_username = input("Masukkan username = ")
    fill_password = input("Masukkan password = ")
    role = 'none'
    user_id = 0
    for data in user_data :
        if fill_username == data[1]:
            if fill_password == data[4]:
                if data[5] == 'user':
                    role = 'user'
                    user_id = data[0]
                    user_username = data[1]
                    Login = True
                elif data[5] == 'admin':
                    role = 'admin'
                    user_id = data[0]
                    user_username = data[1]
                    Login = True
                break
            else :
                Login = False
        else :
            Login = False
    if Login == True :
        print ("Halo " + str(fill_username) + "! Selamat datang di Kantong Ajaib" )
        return role, user_id
    else :
        print ("Username atau Password salah. Silahkan Ulangi")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F03 : Pencarian gadget berdasarkan rarity =====================================================

def carirarity(gadget_data) :
    Rare = str(input("Masukkan rarity = "))
    Found = False
    print ("Hasil Pencarian \n")
    for data in gadget_data :
        if Rare == data[4]:
            Found = True
            print ("Nama            : " , data[1])
            print ("Deskripsi       : " , data[2])
            print ("Jumlah          : " , data[3], "buah")
            print ("Rarity          : " , data[4])
            print ("Tahun Ditemukan : " , data[5], "\n")    
    if Found == False :
        print ("Barang Tidak Ditemukan \n")  

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F04 : Pencarian gadget berdasarkan tahun =====================================================

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F05 : Menambah Item ==============================================================================

def input_ID(gadget_data_ID, consumable_data_ID):
    ID = input("Masukkan ID :")
    isNotValid = True
    while isNotValid:
        if (ID[0] != "G" and ID[0] != "C") or (int(ID[1]) < 1):
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

# Fungsi yang me-return jumlah yang valid
def input_jumlah():
    jumlah = int(input("Masukkan jumlah: "))
    while jumlah <= 0:
        print("Masukkan jumlah yang valid! Jumlah harus lebih besar dari 0")
        print()
        jumlah = int(input("Masukkan jumlah: "))
    return(jumlah)

# Fungsi yang me-return rarity yang valid
def input_rarity():
    array_rarity = ["S", "A", "B", "C", "s", "a", "b", "c"]
    rarity = input("Masukkan rarity: ")
    while rarity not in array_rarity:
        print("Masukkan rarity yang valid! Rarity yang valid adalah S, A, B, atau C")
        print()
        rarity = input("Masukkan rarity: ")
    return(rarity.title())

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
    jumlah = input_jumlah()
    rarity = input_rarity()
    item_baru = [ID, nama_item, deskripsi, jumlah, rarity]
    if ID[0] == "G":
        tahun = input("Masukkan tahun ditemukan: ")
        item_baru.append(tahun)
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
    return
  
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F06 : Menghapus Item ==============================================================================

def cek_valid_id(data,id):
    found = False
    idx = 0 # inisiasi
    while (found == False) and (idx < len(data)):
        if (data[idx][ID_] == id):
            found = True
        else:
            idx = idx + 1
    return found

def cari_indeks_id(data,id):
    for i in range (len(data)):
        if (data[i][ID_] == id ):
            return i

def validasi_hapus(indeks,array_data,item):
    validasi = input("Apakah anda yakin ingin menghapus " + str(item) + " (Y/N)?")

    if (validasi == "Y"):
        array_data.pop(indeks)
        print("\nItem telah berhasil dihapus dari database.")

    else:
        print("\nItem dibatalkan untuk dihapus dari database.")

def hapusitem(data_gadget,data_consumable): # F6
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
        print("\nTidak ada item dengan ID tersebut")
    return (data_consumable,data_gadget)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F07 : Mengubah Jumlah Item ==========================================================================

def hasilubahitem(hasil,jumlah,item,jumlah_item_awal): # fungsi antara 7
        if (hasil > 0):
            if (jumlah > 0):
                print("")
                print(jumlah, item, "berhasilkan ditambahkan. Stok sekarang:", hasil)

            else: # jumlah < 0
                print("")
                print(abs(jumlah), item, "berhasil dibuang. Stok sekarang:", hasil)

        else: # hasil < 0
            print("")
            print(abs(jumlah), item, "gagal dibuang karena stok kurang. Stok sekarang:", jumlah_item_awal, "(<", abs(jumlah), ")" )

def ubahjumlah(data_gadget,data_consumable): 
    id = input("\nMasukkan ID: ")

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
        print("\nTidak ada item dengan ID tersebut!")

    return (data_consumable,data_gadget)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# F08 : Meminjam Gadget =================================================================================

def validDate(date_text):
    isDateValid = True
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError :
        isDateValid = False

    if(isDateValid):
        return True
    else:
        return False

def cari_id_username(data,username):
    for i in range(len(data)):
        if(data[i][1] == username):
            return data[i][0]

def pinjamGadget():
    id_item = input("Masukan ID item: ")
    jumlah = int(input("Jumlah Peminjaman: "))
    while True:
        tanggal = input("Tanggal Peminjaman: ")

        if (validDate(tanggal) == True):
            if (cek_valid_id(gadget_data,id_item) == True):
                indeks = cari_indeks_id(gadget_data,id_item)
                item = gadget_data[indeks][nama]
                dikembalikan = 0
                if (gadget_borrow_history == []):
                    id_gadget_borrow_history = "PjG_1"
                else:
                    before_id_gadget_borrow_history = gadget_borrow_history[len(gadget_borrow_history)-1][0] # sesuaiin nama variabel, samain nama variablenya
                    id_gadget_borrow_history_nomor = int(before_id_gadget_borrow_history[3:]) + 1
                    id_gadget_borrow_history = "PjG_" + str(id_gadget_borrow_history_nomor)

                while ((gadget_data[indeks][jumlahItem] - jumlah) < 0 ): # sesuaiin nama variabel, samain nama variablenya
                    print("stok", item, "tidak mencukupi")
                    print("Silahkan masukkan jumlah item kembali!")
                    jumlah = int(input("Jumlah: "))

                gadget_data[indeks][jumlahItem] = gadget_data[indeks][jumlahItem] - jumlah # sesuaiin nama variabel, samain nama variablenya
                gadget_borrow_history.append([id_gadget_borrow_history,user_id,id_item,tanggal,jumlah,dikembalikan]) # sesuaiin nama variabel, samain nama variablenya
                print("Item", item, "(x",jumlah,") telah berhasil diambil!")
                return

            else:
                print("ERROR, item gadget tidak ditemukan")
                id_item = input("Masukan ID item: ")
                jumlah = int(input("Jumlah: "))
        else:
            print("Tanggal permintaan tidak valid")


# F10 : Meminta Consumable ==============================================================================

def mintaConsumable():
    id_item = input("Masukan ID item: ")
    jumlah = int(input("Jumlah: "))
    while True:
        tanggal = input("Tanggal permintaan: ")

        if (validDate(tanggal) == True):
            if (cek_valid_id(consumable_data,id_item) == True):
                indeks = cari_indeks_id(consumable_data,id_item)
                item = consumable_data[indeks][nama]
                if (consumable_history == []):
                    id_consumable_history = "PC_1"
                else:
                    before_id_consumable_history = consumable_history[len(consumable_history)-1][0] # sesuaiin nama variabel, samain nama variablenya
                    id_consumable_history_nomor = int(before_id_consumable_history[3:]) + 1
                    id_consumable_history = "PC_" + str(id_consumable_history_nomor)

                while ((consumable_data[indeks][jumlahItem] - jumlah) < 0 ): # sesuaiin nama variabel, samain nama variablenya
                    print("stok", item, "tidak mencukupi")
                    print("Silahkan masukkan jumlah item kembali!")
                    jumlah = int(input("Jumlah: "))

                consumable_data[indeks][jumlahItem] = consumable_data[indeks][jumlahItem] - jumlah # sesuaiin nama variabel, samain nama variablenya
                consumable_history.append([id_consumable_history,user_id,id_item,tanggal,jumlah]) # sesuaiin nama variabel, samain nama variablenya
                print("Item", item, "(x",jumlah,") telah berhasil diambil!")
                return

            else:
                print("ERROR, item consumable tidak ditemukan")
                id_item = input("Masukan ID item: ")
                jumlah = int(input("Jumlah: "))
        else:
            print("Tanggal permintaan tidak valid")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# F11 : Riwayat Peminjaman Gadget ==================================================================

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
def obtain_array_tanggal_peminjaman_gadget(array):
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
        arr_tanggal = convert_line_to_data (tanggal, len(tanggal), "/")
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

# Fungsi yang mencetak riwayat peminjaman suatu gadget
def cetak_history_peminjaman(gadget_borrow_history, indeks_mulai, indeks_akhir):
    print()
    for i in range(indeks_mulai, indeks_akhir):
        nama_peminjam = 'none'
        nama_gadget = 'none'
        for j in range (len(user_data)):
            if int(gadget_borrow_history[i][1]) == user_data[j][0] :
                nama_peminjam = user_data[j][1]
        for j in range (len(gadget_data)):
            if gadget_borrow_history[i][2] == gadget_data[j][0] :
                nama_gadget = gadget_data[j][1]
        print("ID Peminjaman :", gadget_borrow_history[i][0])
        print("Nama Peminjam :", nama_peminjam)
        print("Nama Gadget :", nama_gadget)
        print("Tanggal Peminjaman   :", gadget_borrow_history[i][3])
        print("Jumlah               :", gadget_borrow_history[i][4])
        print()

# Prosedur riwayatpinjam
def riwayatpinjam(gadget_borrow_history):
    if gadget_borrow_history == []:
        print("Tidak ada riwayat peminjaman Gadget")
    else:
        gadget_borrow_history = sort_tanggal(obtain_array_tanggal_peminjaman_gadget(gadget_borrow_history), gadget_borrow_history)
        if len(gadget_borrow_history) <= 5:
            cetak_history_peminjaman(gadget_borrow_history, 0, len(gadget_borrow_history))
        else:
            cetak_history_peminjaman(gadget_borrow_history, 0, 5)
            cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            while cetaklagi not in "YyNn":
                print("Input salah!")
                cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            if cetaklagi in "Yy":
                if len(gadget_borrow_history) <= 10:
                    cetak_history_peminjaman(gadget_borrow_history, 5, len(gadget_borrow_history))
                else:
                    cetak_history_peminjaman(gadget_borrow_history, 5, 10)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F12 : Riwayat Pengembalian Gadget ==================================================================

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
            cetak_history_pengembalian(gadget_return_history, 0, len(gadget_return_history))
        else:
            cetak_history_pengembalian(gadget_return_history, 0, 5)
            cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            while cetaklagi not in "YyNn":
                print("Input salah!")
                cetaklagi = input("Ingin mencetak beberapa data lagi? Y/N :")
            if cetaklagi in "Yy":
                if len(gadget_return_history) <= 10:
                    cetak_history_pengembalian(gadget_return_history, 5, len(gadget_return_history))
                else:
                    cetak_history_pengembalian(gadget_return_history, 5, 10)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# F13 : Riwayat Pengambilan Consumable ==================================================================

def obtain_array_tanggal_pengembalian_consumable(array):
    date = []
    for i in range(len(array)):
        date.append(array[i][3])
    return(date)

# Fungsi yang mencetak riwayat pengambilan suatu consumable
def cetak_history_pengambilan(consumable_history, indeks_mulai, indeks_akhir):
    print()
    for i in range(indeks_mulai, indeks_akhir):
        nama_pengambil = 'none'
        nama_consumable = 'none'
        for j in range (len(user_data)):
            if int(consumable_history[i][1]) == user_data[j][0] :
                nama_pengambil = user_data[j][1]
        for j in range (len(consumable_data)):
            if consumable_history[i][2] == consumable_data[j][0] :
                nama_consumable = consumable_data[j][1]
        print("ID Pengembalian :", consumable_history[i][0])
        print("Nama Pengambil :", nama_pengambil)
        print("Nama Consumable :", nama_consumable)
        print("Tanggal Pengembalian :", consumable_history[i][3])
        print("Jumlah               :", consumable_history[i][4])
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# F15 : Save Data ========================================================================

def convert_datas_to_string(datas, header):
    string_data = ";".join(header) + "\n"
    for arr_data in datas :
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def write_csv(nama_file,datas,header,path):
    f = open(os.path.join(path,nama_file),"w")
    f.write(convert_datas_to_string(datas,header))
    f.close()

def cek_folder(nama_folder):
    if os.path.isdir(nama_folder):
        return True
    else:
        return False

def save():
    nama_folder = input("Masukkan nama folder penyimpanan: ")
    if (cek_folder(nama_folder) == True):
        write_csv("gadget.csv",gadget_data,csv_header("gadget.csv",6),nama_folder)                      
        write_csv("consumable.csv",consumable_data,csv_header("consumable.csv",5),nama_folder)          
        write_csv("user.csv",user_data,csv_header("user.csv",6),nama_folder)
        write_csv("gadget_return_history.csv",gadget_return_history,csv_header("gadget_return_history.csv",3),nama_folder)
        write_csv("consumable_history.csv",consumable_history,csv_header("consumable_history.csv",6),nama_folder)
        write_csv("gadget_borrow_history.csv",gadget_borrow_history,csv_header("gadget_borrow_history.csv",6),nama_folder)

    else:
        os.mkdir(nama_folder)
        write_csv("gadget.csv",gadget_data,csv_header("gadget.csv",6),nama_folder)                      
        write_csv("consumable.csv",consumable_data,csv_header("consumable.csv",5),nama_folder)          
        write_csv("user.csv",user_data,csv_header("user.csv",6),nama_folder)
        write_csv("gadget_return_history.csv",gadget_return_history,csv_header("gadget_return_history.csv",3),nama_folder)
        write_csv("consumable_history.csv",consumable_history,csv_header("consumable_history.csv",6),nama_folder)
        write_csv("gadget_borrow_history.csv",gadget_borrow_history,csv_header("gadget_borrow_history.csv",6),nama_folder)

# F16 : Help ==============================================================================
def Help () :
    print ("================= HELP ================= \n")
    print ("===== untuk user dan admin ===== ")
    print ("login      - untuk melakukan login ke dalam sistem")
    print ("carirarity - untuk menampilkan gadget dengan rarity tertentu")
    print ("caritahun  - untuk menampilkan gadget dalam rentang waktu (tahun) tertentu")
    print ("carirarity - untuk menampilkan gadget dengan rarity tertentu")
    print ("save       - untuk menyimpan data setelah melakukan perubahan")
    print ("exit       - untuk keluar dari sistem \n")
    print ("===== khusus user ===== ")
    print ("pinjam     - untuk melakukan pemimjaman gadget")
    print ("kembalikan - untuk melakukan pengembalian gadget yang dipinjam")
    print ("minta      - untuk meminta consumable yang tersedia \n")
    print ("===== khusus admin ===== ")
    print ("register   - untuk melakukan registrasi user baru")
    print ("tambahitem - untuk menambahkan item ke inventory")
    print ("hapusitem  - untuk menghapus item dari inventory")
    print ("ubahjumlah - untuk mengubah jumlah suatu item pada inventory")
    print ("riwayatpinjam  - untuk melihat riwayat peminjaman gadget")
    print ("riwayatkembali - untuk melihat riwayat pengembalian gadget")
    print ("riwayatambil   - untuk melihat riwayat pengambilan consumable")



# F17 Exit ============================================== 

def Exit () :
    save_reminder = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)")
    while save_reminder not in "YyNn" :
        print ("Input salah! Input Kembali")
        save_reminder = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)")
    if save_reminder == "y" or save_reminder == 'Y' :
        save()
        print ("\nTerima kasih telah menggunakan kantong ajaib!\n")
    elif save_reminder == 'n' or save_reminder == 'N' :
        print ("\nTerima kasih telah menggunakan kantong ajaib!\n")


# ======================================== Program Utama ============================================== 

def Program_utama ():
    print ("\nSilahkan Login terlebih dahulu")
    print ("Silahkan ketik 'help' untuk melihat panduan")
    Program = str(input("\n>>>"))
    while Program != 'exit' :
        if Program == 'register':
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk register")
            elif role == 'admin' :
                register(user_data, user_header)
        elif Program == 'login' :
            login(user_data)
        elif Program == 'carirarity' :
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' or role == 'admin' :
                masihMau = True
                while masihMau:
                    carirarity(gadget_data)
                    masih = input("Masih ingin mencari rarity gadget? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin mencari rarity gadget? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'caritahun' :
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            if role == 'user' or role == 'admin' :
                masihMau = True
                while masihMau:
                    caritahun(gadget_data)
                    masih = input("Masih ingin mencari tahun gadget? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin mencari tahun gadget? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'tambahitem' :
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Menambah item")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    tambahitem()
                    masih = input("Masih ingin menambahkan item? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin menambahkan item? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'hapusitem':
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Menghapus item")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    hapusitem(gadget_data, consumable_data)
                    masih = input("Masih ingin menghapus item? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin menghapus item? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'ubahjumlah':
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Mengubah jumlah item")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    ubahjumlah(gadget_data, consumable_data)
                    masih = input("Masih ingin Mengubah jumlah item? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin Mengubah jumlah item? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'pinjam':
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'admin' :
                print ("Anda tidak memiliki akses untuk meminjam gadget")
            elif role == 'user' :
                masihMau = True
                while masihMau:
                    pinjamGadget()
                    masih = input("Masih ingin meminjam gadget? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin meminjam gadget? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'minta':
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'admin' :
                print ("Anda tidak memiliki akses untuk meminta Consumable")
            elif role == 'user' :
                masihMau = True
                while masihMau:
                    mintaConsumable()
                    masih = input("Masih ingin meminta Consumable? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin meminta Consumable? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == "riwayatpinjam":
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Melihat riwayat Peminjaman Gadget")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    riwayatpinjam(gadget_borrow_history)
                    masih = input("Masih ingin Melihat riwayat Peminjaman Gadget? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin Melihat riwayat Peminjaman Gadget? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == "riwayatambil":
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Melihat riwayat pengambilan consumable")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    riwayatambil(consumable_history)
                    masih = input("Masih ingin menambahkan item? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin menambahkan item? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == "riwayatkembali":
            if role == 'none' :
                print ("Silahkan login terlebih dahulu")
            elif role == 'user' :
                print ("Anda tidak memiliki akses untuk Melihat riwayat pengembalian gadget")
            elif role == 'admin' :
                masihMau = True
                while masihMau:
                    riwayakembali(gadget_return_history)
                    masih = input("Masih ingin menambahkan item? Y/N :")
                    while masih not in "YyNn":
                        print("Input salah! Input kembali!")
                        masih = input("Masih ingin menambahkan item? Y/N :")
                    if masih in "Nn":
                        masihMau = False
        elif Program == 'save' :
            save()
        elif Program == "help" :
            Help()
        else :
            print ("Input tidak diketahui")
            print ("Silahkan ketik 'help' untuk melihat panduan")
        Program = str(input("\n>>>"))
    if Program == 'exit' :
        Exit ()


# =========================================== Program =================================================

if not load_data():
    print("Tidak ada nama folder yang diberikan!")
    print("Usage : python kantongajaib.py <nama_folder>")
else :
    print("Loading...")
    time.sleep(3)
    print ("")
    print("Selamat datang di %s" % '"Kantong Ajaib!"')
    time.sleep(1)
    Program_utama()
    

    