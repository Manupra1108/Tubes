from read_csv import read_csv
from fungsi import length

#def length(list):
#    index = 0

#    for i in list :
#        index += 1 
#    return index 
    
def login(data):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    index = 0
    cek = False
    for i in range(1, length(data)):
        if data[i][1]==username and data[i][3]==password:
            cek = True
            index = i
    
    if cek == True:
        print(f"Halo {data[index][2]}! Selamat datang di “Binomo”.")
        id = data[index][0]
        return (id)
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return

if __name__ == "__main__":
    data_user_csv = read_csv('user.csv')
    login(data_user_csv)