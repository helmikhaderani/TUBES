f = open("DaftarCSV/user.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def convert_line_to_data(array, banyak_kategori):
    list = []
    for teks in array:
        for karakter in teks:
            list.append(karakter)
    arraybaru = []
    count = 1
    string = list[0]
    list[0] = ","
    for i in range(banyak_kategori):
        while (list[count] != ",") and (count < len(list) - 1):
            string += list[count]
            list[count] = ","
            count += 1
        if count == len(list) - 1:
            string += list[count]
        arraybaru.append(string)
        string = ""
        count += 1
    return(arraybaru)

def convert_array_data_to_real_value(array, panjang_array):
    temp_array = array
    for i in range(panjang_array):
        if i == 0:
            temp_array[i] = int(temp_array[i])
    return(temp_array)

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header,6)
print(header)

datas = []
for line in lines:
    array_of_data = convert_line_to_data(line,6)
    real_value = convert_array_data_to_real_value(array_of_data,6)
    datas.append(real_value)
print(datas)

def modify_datas(nama_csv, idx, col, value):
    nama_csv[idx][col] = value