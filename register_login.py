f = open("user.csv","r")
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

def register ():
    global convert_datas_to_string
    unique = True
    new_user_idx = datas[-1][0] + 1
    raw_new_user_nama = input("Masukkan nama = ")
    new_user_username = input("Masukkan username = ")
    new_user_password = input("Masukkan password = ")
    new_user_alamat = input("Masukkan alamat = ")
    new_user_role = 'user'

    new_user_nama = raw_new_user_nama.title()

    for data in datas :
        if new_user_username == data[1]:
            unique = False
    
    if unique == True :
        new_user = [new_user_idx, new_user_username, new_user_nama, new_user_alamat, new_user_password, new_user_role]

        datas.append(new_user)

        datas_as_string = convert_datas_to_string()

        f = open ("user copy.csv", "w")
        f.write(datas_as_string)
        f.close()
        return (print ("User " + str(new_user_username) + " telah berhasil register ke dalam Kantong Ajaib"))
        
    elif unique == False :
        print ("Username sudah digunakan. Silahkan input username berbeda")
   

def login() :
    global datas
    Login = False
    fill_username = input("Masukkan username = ")
    fill_password = input("Masukkan password = ")
    for data in datas :
        if fill_username == data[1]:
            if fill_password == data[4]:
                Login = True
                break
            else :
                Login = False
        else :
            Login = False
    if Login == True :
        print ("Halo " + str(fill_username) + "! Selamat datang di Kantong Ajaib" )
    else :
        print ("Username atau Password salah. Silahkan Ulangi")


Program = str(input("\n>>>"))
if Program == 'register':
    register()
elif Program == 'login' :
    login()

