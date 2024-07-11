import requests
import time
import os

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('[ KhoaTool ] </> [1] Aviso (Quảng Cáo + Youtube) [ Ổn Định ]')
        chon = int(input('Nhập Lựa Chọn : '))
        if chon == 1:
            os.system("cls" if os.name == "nt" else "clear")
            exec(requests.get('https://raw.githubusercontent.com/khoa1209208/Sources/main/DemoAviso.py').text)
        if chon == 2:
            os.system("cls" if os.name == "nt" else "clear")
            exec(requests.get('https://raw.githubusercontent.com/khoa1209208/Sources/main/enc_pepe.py').text)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print('Vui Lòng Chọn Những Lựa Chọn Trên !!!')
            time.sleep(2)
            continue
except:
    pass
