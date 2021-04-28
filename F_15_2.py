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
        write_csv("gadget.csv",gadget,csv_header("gadget.csv",6),nama_folder)                      # nama arraynya blom sesuai masih sementara
        write_csv("consumable.csv",consumable,csv_header("consumable.csv",5),nama_folder)          # nama arraynya blom sesuai masih sementara

        print()
        print("Saving...")
        print("Data telah disimpan pada folder", nama_folder)

    else:
        os.mkdir(nama_folder)
        write_csv("gadget.csv",gadget,csv_header("gadget.csv",6),nama_folder)                      # nama arraynya blom sesuai masih sementara
        write_csv("consumable.csv",consumable,csv_header("consumable.csv",5),nama_folder)          # nama arraynya blom sesuai masih sementara
        # file lainnya blom dimasukkan

        print()
        print("Saving...")
        print("Data telah disimpan pada folder", nama_folder)