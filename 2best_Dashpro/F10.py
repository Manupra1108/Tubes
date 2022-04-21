from fungsi import length,konso

def search_my_game(data_kepemilikan,data_game,id):
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    # inisialisasi awal
    data_id = []
    data_tahun = []
    data_final = []
    # data_id, tahun, dan final nantinya akan digunakan untuk mengumpulkan id_game yang sesuai dengan kriteria
    id_game_isi = False
    
    if id_game != '':
        # id game diisi
        id_game_isi = True
        for i in range(1,length(data_kepemilikan)):
            for j in range(1,2):
                if data_kepemilikan[i][j] == id:
                    if data_kepemilikan[i][0] == id_game:
                        # user_id sesuai serta id_game ditemukkan sehingga id_game dimasukkan ke dalam list data_id
                        konso(data_id,data_kepemilikan[i][0])
    # memasukkan data_id ke dalam data final
    data_final = data_id
    
    if tahun_rilis != '':
        if id_game_isi == True:
            if data_id == []:
                # id_game diisi tapi data_id kosong sehingga data_tahun kosong
                data_tahun == []
            else:
                # id_game diisi dan tidak kosong sehingga data_tahun diisi menggunakan data_id
                count = 0
                i = 0
                while (count<length(data_id)):
                # Melakukan pengulangan sampai count == length(data_id)
                    if data_id[count] == data_game[i][0]:
                        if data_game[i][3] == tahun_rilis:
                            # datagame[i][0] dimasukkan ke dalam list data_tahun
                            konso(data_tahun,data_game[i][0])
                            count +=1
                            i = 0
                            # penambahan count +=1 untuk mengecek data_id pada element berikutnya
                            # inisalisasi ulang i = 0
                        else:
                            # data_game[i][3] != tahun_rilis sehingga data_game[i][3] tidak dimasukkan kedalam list data_tahun
                            count +=1
                            i = 0
                            # penambahan count +=1 untuk mengecek data_id pada element berikutnya
                            # inisalisasi ulang i = 0
                    else:
                        i += 1
                        # penambahan i +=1 untuk mengecek data_game pada baris berikutnya
    
        else:
            data_tahun_temp = []
            for i in range(1,length(data_kepemilikan)):
                for j in range(1,2):
                    if data_kepemilikan[i][j] == id:
                        # user_id sesuai sehingga data_kepemilikan[i][0] dimasukkan ke list data_tahun_temp
                        konso(data_tahun_temp,data_kepemilikan[i][0])
            count = 0
            i = 0
            while (count<length(data_tahun_temp)):
                # Melakukan pengulangan sampai count == length(data_tahun_temp)
                    if data_tahun_temp[count] == data_game[i][0]:
                        if data_game[i][3] == tahun_rilis:
                            # datagame[i][0] dimasukkan ke dalam list data_tahun
                            konso(data_tahun,data_game[i][0])
                            count +=1
                            i = 0
                            # penambahan count +=1 untuk mengecek data_id pada element berikutnya
                            # inisalisasi ulang i = 0
                        else:
                            # data_game[i][3] != tahun_rilis sehingga data_game[i][3] tidak dimasukkan kedalam list data_tahun
                            count +=1
                            i = 0
                            # penambahan count +=1 untuk mengecek data_id pada element berikutnya
                            # inisalisasi ulang i = 0
                    else:
                        i += 1
                        # penambahan i +=1 untuk mengecek data_game pada baris berikutnya
        
        # Mengganti isi dari data_final menjadi data_tahun
        data_final = data_tahun
    
    if data_final == []:
        # Tidak ditemukan game yang memenuhi kriteria
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        count = 0
        i = 0
        while(count<length(data_final)):
            if data_final[count] == data_game[i][0]:
                print(data_game[i][0]," | ",data_game[i][1]," | ",data_game[i][4]," | ", data_game[i][2], " | ", data_game[i][3])
                i = 0
                count +=1
                # penambahan count +=1 untuk mengecek data_final pada element berikutnya
                # inisalisasi ulang i = 0
            else:
                i += 1
    return         