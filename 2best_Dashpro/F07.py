from fungsi import length

data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], 
            ['G010', 'Journey', 'Adventure', '2020', '120000', '3'], 
            ['G007', 'Hitman 3', 'Action', '2021', '370000', '5'], 
            ['G099', 'Skyrim', 'RPG', '2011', '200000', '1'],
            ['G100', 'Sekiro', 'Action', '2019', '250000', '0'], 
            ['G009', 'Forza Horizon 5', 'Racing', '2021', '550000', '9']]

def sort_asc(atribut,data1):
    if atribut == 'tahun':
        kolom = 3
    elif atribut == 'harga':
        kolom = 4
    elif atribut == '':
        kolom = 0
    i = 1
    kondisi = False
    while not(kondisi):
        Pass = i
        imin = Pass
        while(Pass<=length(data1)-1):
            if (data1[Pass][kolom]) < (data1[imin][kolom]):
                imin = Pass
                Pass +=1
            else:
                Pass +=1
        temp = data1[i]
        data1[i] = data1[imin]
        data1[imin] = temp
        i +=1
        if i == length(data1):
            kondisi = True
    return(data1)
    

def sort_desc(atribut,data1):
    if atribut == 'tahun':
        kolom = 3
    elif atribut == 'harga':
        kolom = 4
    i = 1
    kondisi = False
    while not(kondisi):
        Pass = i
        imax = Pass
        while(Pass<=length(data1)-1):
            if (data1[Pass][kolom]) > (data1[imax][kolom]):
                imax = Pass
                Pass +=1
            else:
                Pass +=1
        temp = data1[i]
        data1[i] = data1[imax]
        data1[imax] = temp
        i +=1
        if i == length(data1):
            kondisi = True
    return(data1)
        
def list_game_toko(data):
    cek = True
    skemasorting = input("Skema sorting : ")
    urutan = ''
    atribut = ''
    for i in skemasorting:
        if not(i=="+" or i=="-"):
            atribut+=i
        else:
            urutan +=i
    data_game_listed = data
    if atribut == 'tahun':
        if urutan == '-':
            sort_desc(atribut,data_game_listed)
        elif urutan == '+':
            sort_asc(atribut,data_game_listed)
    elif atribut == 'harga':
        if urutan == '-':
            sort_desc(atribut,data_game_listed)
        elif urutan == '+':
            sort_asc(atribut,data_game_listed)
    elif atribut == '':
        sort_asc(atribut,data_game_listed)
    else:
        print('Skema sorting tidak valid!')
        cek = False
    if cek == True:
        for i in range(1,length(data_game_listed)):
                    for j in range(5):
                        print(data_game_listed[i][j],end = "|")
                    for j in range(5,6):
                        print(data_game_listed[i][j])
        return data_game_listed
    
if __name__ == '__main__':
    print(sort_asc('',data_game))
    list_game_toko(data_game)   