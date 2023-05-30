stockGudang = [
                {'kode barang' : '001', 'kategori' : 'Minuman', 'nama barang' : 'kopi susu', 'jumlah barang' : 10 , 'harga barang' : 6000},
                {'kode barang' : '002', 'kategori' : 'Minuman', 'nama barang' : 'kopi latte', 'jumlah barang' : 5, 'harga barang' : 8000},
                {'kode barang' : '003' ,'kategori' : 'makanan', 'nama barang' : 'chitato', 'jumlah barang' : 6, 'harga barang' : 5000}
                ]

def menu_Stock_gudang():
    print('''
    |============================================|
    |Selamat datang di menu program stock gudang |
    |============================================|
    |Daftar pilihan menu stock gudang:           |
    |1. Menampilkan stock gudang                 |
    |2. Menambah daftar stock gudang             |
    |3. Mengupdate stock gudang                  |
    |4. Menghapus daftar stock gudang            |
    |5. Exit program                             |
    |============================================|\n''')


def read_menu():
    while True:
        print('''
    |===============================================================|
    |                           Menu 1                              |
    |===============================================================|
    |Menampilkan stock gudang:                                      |
    |1. Menampilkan semua data stock gudang                         |
    |2. Menampilkan data tertentu                                   |
    |3. Menampilkan semua data diurutkan berdasarkan jumlah terkecil|
    |4. Menampilkan semua data diurutkan berdasarkan jumlah terbesar|
    |5. Kembali ke menu utama                                       |
    |===============================================================|''')


        pilihan = input('masukkan sub menu read yang akan dijalankan: ')
        if pilihan == '1':
            if len(stockGudang) == 0:
                print('data tidak ada')
            else:
                print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
                for dict_stock in stockGudang:
                    print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values()))
        elif pilihan == '2':
            if len(stockGudang) == 0:
                print('data tidak ada')
            else:
                primary_key = input('masukkan kode stock: ')
                for i,dict_stock in enumerate (stockGudang):
                    if primary_key == stockGudang[i]['kode barang']:
                        print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
                        print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values()))
                        break
                    else:
                        continue                
                else:
                    print('data tidak ada')
        elif pilihan == '3':
            list_jumlahBarang_asc = sorted(stockGudang, key=lambda d: d['jumlah barang']) 
            print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
            for dict_stock in list_jumlahBarang_asc:
                print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values()))
        elif pilihan == '4':
            list_jumlahBarang_asc = sorted(stockGudang, key=lambda d: d['jumlah barang'], reverse= True) 
            print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
            for dict_stock in list_jumlahBarang_asc:
                print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values()))
        elif pilihan == '5':
            print('menu utama')
            break
        else:
            print('pilihan sub menu salah')

def create_menu():
    while True:
        print('''
    |==============================|
    |Menu 2                        |
    |==============================|
    |Menampilkan stock gudang:     |
    |1. Menambah data              |
    |2. Kembali ke menu utama      |
    |==============================|''')
        pilihan = input('masukkan sub menu create yang dijalankan: ')
        if pilihan == '1':
            if len(stockGudang) == 0:
                print('data tidak ada')
            else:
                baruGd = input('masukkan kode stock barang: ')
                count = 0
                while count < len(stockGudang):
                    if baruGd == stockGudang[count]['kode barang']:
                        print('Data sudah ada, masukkan data lain')
                        break
                    else:
                        count += 1  
                        continue 

                else:
                    dictBaru = {}
                    kategori = input('Masukkan kategori: ')
                    nama_barang = input('Masukkan nama barang: ')
                    jumlahBarang = int(input('Masukkan Jumlah Barang: '))
                    hargaBarang = int(input('Masukkan harga barang: '))
                    dictBaru= {'kode barang' : baruGd, 'kategori' : kategori, 'nama barang' : nama_barang, 'jumlah barang' : jumlahBarang, 'harga barang' : hargaBarang}
                    dataSimpan = input('apakah data baru akan disimpan(y/t): ').upper()
                    if dataSimpan == 'Y':
                        stockGudang.append(dictBaru)
                        print('data telah disimpan')
                    elif dataSimpan == 'T':
                        print('kembali ke menu utama')
                    else:
                        print('input salah')
        elif pilihan == '2':
            print('program exit')
            break
        else:
            print('pilihan sub menu salah')
    
def update_menu():
    while True:
        print('''
    |================================|
    |Menu 3                          |
    |================================|
    |Menampilkan stock gudang:       |
    |1. Mengupdate data stock barang |
    |2. Kembali ke menu utama        |
    |================================|''')
        pilihan = input('masukkan sub menu update yang dijalankan: ')
        if pilihan == '1':
            if len(stockGudang) == 0:
                print('data tidak ada')
            else:
                upMenu = input('masukkan kode stock barang yang ingin diupdate: ')
                count = 0
            while count < len(stockGudang):
                if upMenu == stockGudang[count]['kode barang']:
                    print('kode barang :',stockGudang[count]['kode barang'],'|', 'kategori :', stockGudang[count]['kategori'],'|','nama barang :',stockGudang[count]['nama barang'],'|','jumlah barang :', stockGudang[count]['jumlah barang'],'|', 'harga barang :', stockGudang[count]['harga barang'])   
                    dataSimpan_1 = input('Apakah yakin ingin mengupdate (y/t) ? ').upper()
                    if dataSimpan_1 == 'Y' :
                        jumlahBarang = int(input('Masukkan jumlah barang yang ingin diubah: '))
                        dataSimpan_2 = input(f'Apakah anda yakin ingin merubah jumlah barang dari kode stock {upMenu} (y/t) ?').upper()
                        if dataSimpan_2 == 'Y' :
                            print('Data telah berhasil diupdate: ')
                            stockGudang[count]['jumlah barang'] = jumlahBarang
                            print('kode barang :',stockGudang[count]['kode barang'],'|', 'kategori :', stockGudang[count]['kategori'],'|','nama barang :',stockGudang[count]['nama barang'],'|','jumlah barang :', stockGudang[count]['jumlah barang'],'|', 'harga barang :', stockGudang[count]['harga barang'])
                            break
                        else :
                            print('Data tidak jadi diupdate')
                            
                    else :
                        print('Data tidak jadi diupdate')
                        break
                else:
                    count += 1  
                    continue 
            else:
                print('Data belum ada, masukkan data yang sudah ada untuk diupdate')
               
        elif pilihan == '2':
            print('program exit')
            break
        else:
            print('pilihan sub menu salah')

def delete_menu():
    while True:
        print('''
    |================================|
    |Menu 4                          |
    |================================|
    |Menampilkan stock gudang:       |
    |1. Mengdelete data stock barang |
    |2. Kembali ke menu utama        |
    |================================|''')
        pilihan = input('masukkan sub menu delete yang dijalankan: ')
        if pilihan == '1':
            if len(stockGudang) == 0:
                print('data tidak ada')
            else:
                print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
                for dict_stock in stockGudang:
                   print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values())) 
                upMenu = input('masukkan kode stock barang yang ingin didelete: ')
                count = 0
                while count < len(stockGudang):        
                    if upMenu == stockGudang[count]['kode barang']:
                        print('kode barang :',stockGudang[count]['kode barang'],'|', 'kategori :', stockGudang[count]['kategori'],'|','nama barang :',stockGudang[count]['nama barang'],'|','jumlah barang :', stockGudang[count]['jumlah barang'],'|', 'harga barang :', stockGudang[count]['harga barang'])   
                        dataSimpan_1 = input('Apakah yakin ingin mendelete (y/t) ? ').upper()
                        if dataSimpan_1 == 'Y' :
                            stockGudang.pop(count)
                            print('Data telah berhasil didelete')
                            print(''' 
|====================================================================================|
|Kode barang   | kategori barang  | nama barang      | jumlah barang   | harga barang|
|====================================================================================|''')
                            for dict_stock in stockGudang:
                                print('| {:<12} | {:<16} | {:<16} | {:<15} | {:<11} |'.format(*dict_stock.values()))    
                        else :
                            print('Data tidak jadi didelete')
                        break
                    
                    else:
                        count += 1  
                        continue 
                else:
                    print('Data belum ada, masukkan data yang sudah ada untuk didelete')
                    
        elif pilihan == '2':
            print('program exit')
            break
        else:
            print('pilihan sub menu salah')

def main_menu():
    while True:
        menu_Stock_gudang()
        pilihan = input('masukkan menu program yang akan dijalankan: ')
        if pilihan == '1':
            read_menu()
        elif pilihan == '2':
            create_menu()
        elif pilihan == '3':
            update_menu()
        elif pilihan =='4':
            delete_menu()
        elif pilihan == '5':
            print('exit program')
            break
        else:
            print('menu yang anda masukkan salah')

main_menu()

