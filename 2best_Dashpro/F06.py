from read_csv import read_csv
from fungsi import length

data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], 
            ['GAME001', 'Journey', 'Adventure', '2020', '120000', '3'], 
            ['GAME002', 'Hitman 3', 'Action', '2021', '370000', '5'], 
            ['GAME003', 'Skyrim', 'RPG', '2011', '200000', '1'], 
            ['GAME004', 'Forza Horizon 5', 'Racing', '2021', '550000', '9'], 
            ['GAME005', 'Sekiro', 'Action', '2019', '250000', '0']]

#def length(list):
#    index = 0
#    for i in list :
#        index += 1 
#    return index 

def search(input_data,data,column):
    x = 0
    for i in range (length(data)):
        if input_data != data[i][column]:
            x += 1
        elif input_data == data[i][column]:
            break
    return x

def ubah_stok(data):
    id = input("Masukan ID game: ")
    jumlah = input("Masukan jumlah: ")
    if 0 < search(id,data,0) < length(data):
        isValidJumlah = True
        if jumlah == '':
            isValidJumlah = False
        else:
            for i in jumlah:
                if not(i>='0' and i<='9' or i == '-') or i =='':
                    isValidJumlah = False
                    break
        if not(isValidJumlah):
            print("Masukan tidak valid")
        else:
            if int(jumlah) < 0:
                if -int(jumlah) > int(data[search(id,data,0)][5]):
                    print(f"Stok game {data[search(id,data,0)][1]} gagal dikurangi karena stok kurang. Stok sekarang: {data[search(id,data,0)][5]} (<{int(-jumlah)})")
                else:
                    stok = int(data[search(id,data,0)][5]) + int(jumlah)
                    print(f"Stok game {data[search(id,data,0)][1]} berhasil dikurangi. Stok sekarang: {stok}")
                    data[search(id,data,0)][5] = str(stok)
            else:
                stok = int(data[search(id,data,0)][5]) + int(jumlah)
                print(f"Stok game {data[search(id,data,0)][1]} berhasil ditambahkan. Stok sekarang: {stok}")
                data[search(id,data,0)][5] = str(stok)
    else:
        print("Tidak ada game dengan ID tersebut!")
    
    return data
