f = open("gadget.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def convert_array_data_to_real_values (array_of_data):
    array_copy = array_of_data [:]
    for i in range (6) :
        if (i == 0):
            array_copy[i] = int(array_of_data[i])
        return array_copy

def convert_line_to_data (line) :
    raw_array_of_data = []
    tmp = ''
    for i in line :
        if i == ';':
            raw_array_of_data.append(tmp)
            tmp = ''
        else :
            tmp += i
    if tmp :
        raw_array_of_data.append (tmp)
    
    array_of_data = [data.strip() for data in raw_array_of_data]

    return array_of_data

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)
#print (header)

datas = []
for line in lines :
    array_of_data = convert_line_to_data (line)
    real_values = convert_array_data_to_real_values(array_of_data)
    datas.append (real_values)
#print(datas)

def convert_datas_to_string():
    string_data = ";".join(header) + "\n"
    for arr_data in datas :
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def carirarity() :
    Rare = str(input("Masukkan rarity = "))
    Found = False
    print ("Hasil Pencarian \n")
    for data in datas :
        if Rare == data[4]:
            Found = True
            print ("Nama            : " , data[1])
            print ("Deskripsi       : " , data[2])
            print ("Jumlah          : " , data[3], "buah")
            print ("Rarity          : " , data[4])
            print ("Tahun Ditemukan : " , data[5], "\n")    
    if Found == False :
        print ("Barang Tidak Ditemukan \n")    

Program = str(input("\n>>>"))
if Program == 'carirarity':
    carirarity()