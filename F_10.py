# ======================================================================== untuk percobaan

data_username = load_csv("user.csv") # sesuaiin nama variabel, samain nama variablenya
data_consumable = load_csv('consumable.csv') # sesuaiin nama variabel, samain nama variablenya
data_consumable_history = load_csv('consumable_history.csv') # sesuaiin nama variabel, samain nama variablenya

# ========================================================================
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

def cek_valid_id(data,id):
    found = False
    idx = 0 # inisiasi
    while (found == False) and (idx < len(data)):
        if (data[idx][ID] == id):
            found = True
        else:
            idx = idx + 1
    return found

def cari_id_username(data,username):
    for i in range(len(data)):
        if(data[i][1] == username):
            return data[i][0]

# === fungsi antara sama di F6 dan F7 ========================================================
def cari_indeks_id(data,id):
    for i in range (len(data)):
        if (data[i][ID] == id ):
            return i
# ======================================= F 10 ================================================ 

def mintaConsumable():  # sesuaiin nama variabel, samain nama variablenya; di dalam fungsinya juga
    print(">>> Minta Consumable")
    while True:
        id_item = input("Masukan ID item: ")
        jumlah = int(input("Jumlah: "))
        while True:
            tanggal = input("Tanggal permintaan: ")

            if (validDate(tanggal) == True):
                if (cek_valid_id(data_consumable,id_item) == True):
                    id_user = cari_id_username(data_username,username)           # sesuaiin nama variabel, samain nama variablenya
                    indeks = cari_indeks_id(data_consumable,id_item)
                    item = data_consumable[indeks][nama]
                    if (data_consumable_history == []):
                        id_consumable_history = "PC_1"
                    else:
                        before_id_consumable_history = data_consumable_history[len(data_consumable_history)-1][0] # sesuaiin nama variabel, samain nama variablenya
                        id_consumable_history_nomor = int(before_id_consumable_history[3:]) + 1
                        id_consumable_history = "PC_" + str(id_consumable_history_nomor)

                    while ((data_consumable[indeks][jumlahItem] - jumlah) < 0 ): # sesuaiin nama variabel, samain nama variablenya
                        print("stok", item, "tidak mencukupi")
                        print("Silahkan masukkan jumlah item kembali!")
                        jumlah = int(input("Jumlah: "))

                    data_consumable[indeks][jumlahItem] = data_consumable[indeks][jumlahItem] - jumlah # sesuaiin nama variabel, samain nama variablenya
                    data_consumable_history.append([id_consumable_history,id_user,id_item,tanggal,jumlah]) # sesuaiin nama variabel, samain nama variablenya
                    print("Item", item, "(x",jumlah,") telah berhasil diambil!")

                else:
                    print("ERROR, item consumable tidak ditemukan")
            else:
                print("Tanggal permintaan tidak valid")
            
            if(validDate(tanggal) == True):
                break
        
        exit = input("Apakah Anda sudah meminta semua item consumable yang Anda inginkan? (Y/N)")

        if (exit == 'Y'):
            break