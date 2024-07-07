from bs4 import BeautifulSoup
from datetime import datetime
import requests
import random
import time
import sys
import os
import re



yellow = "\033[0;33m"
maufullxduong = "\033[1;47;34m"
maufulldo = "\033[1;47;31m"
end = "\033[0m"
whiteb = "\033[1;37m"
ress = "\033[0;32m"
res = "\033[0;33m"
red = "\033[0;31m"
green = "\033[0;37m"
yellow = "\033[0;33m"
white = "\033[0;33m"
Bxnhac = "\033[1;96m"
den = "\033[1;90m"
do = "\033[1;91m"
luc = "\033[1;92m"
vang = "\033[1;93m"
xduong = "\033[1;94m"
hong = "\033[1;95m"
trang = "\033[1;97m"
nenden = "\033[40m"
xanhd = "\033[0;36m"
nendo = "\033[41m"
nenxanh = "\033[42m"
nenvang = "\033[43m"
nenblue = "\033[44m"
nenPurpe = "\033[45m"
nenCyan = "\033[46m"
nentrang = "\033[47m"
UGreen = "\033[4;32m"
BGreen = "\033[1;32m"
maufullluc = "\033[1;47;32m"
maufullxnhac = "\033[1;47;36m"
maufullden = "\033[1;47;30m"
maufullvang = "\033[1;47;33m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = "\033[1;35m"
xnhac = "\033[1;36m"
trang = "\033[1;37m"
hong = "\033[1;95m"
trang = "\033[1;97m"
ress = "\033[0;32m"
res = "\033[0;33m"
red = "\033[0;31m"
green = "\033[0;37m"
nau = "\033[38;5;94m"
white = "\033[0;33m"
res = "\033[0m"
red = "\033[1;31m"
white = "\033[1;37m"
whiteb = "\033[1;37m"
redb = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cam = "\033[1;33m"
test = "\033[1;33m"
greenb = "\033[1;32m"
lam = "\033[1;34m"
tmi = "\033[1;34m"
hong = "\033[1;35m"
imt = "\033[1;35m"
cyan = "\033[1;36m"
syan = "\033[1;36m"
xnhac = "\033[1;96m"
den = "\033[1;90m"
do = "\033[1;91m"
luc = "\033[1;92m"
vang = "\033[1;93m"
xduong = "\033[1;94m"
hong = "\033[1;95m"
trang = "\033[1;97m"
vang = "\033[1;93m"
do = "\033[1;91m"
BBlack = "\033[1;30m"
BRed = "\033[1;31m"
BGreen = "\033[1;32m"
BYellow = "\033[1;33m"
BBlue = "\033[1;34m"
BPurple = "\033[1;35m"
BCyan = "\033[1;36m"
BWhite = "\033[1;37m"
lime = "\033[1;32m"
red = "\033[1;31m"
xanh = "\033[1;32m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
turquoise = "\033[1;34m"
maugi = "\033[1;35m"
white = "\033[1;37m"
BCyan = "\033[1;36m"
trang = "\033[1;37m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
luc = "\033[1;92m"
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"



class Aviso:
    def __init__(self, COOKIE, DELEY) -> None:
        self.s = requests.session()
        self.COOKIE = COOKIE
        self.DELEY = DELEY
        self.DEMJOBLOI = 0
        self.POINT = 0
        self.DEM = 0

    def checkUser(self):
        try:
            while True:
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.COOKIE,
                    'priority': 'u=0, i',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                }

                self.s.headers.update(headers)

                USER = self.s.get('https://aviso.bz/', stream=True).text

                if 'Войти' in USER:
                    print('Nhập Sai Cookie Vui Lòng Nhập Lại', end='\r')
                    print(' '*50, end='\r')
                    self.COOKIE = input('Nhập Lại Cookie : ')
                    continue

                USERID = USER.split('user-block-info-userid">')[1].split('</')[0]
                USERNAME = USER.split('user-block-info-username">')[1].split('</')[0]
                RUB = USER.split('new-money-ballans">')[1].split(' руб.')[0]
                self.POINT += float(RUB)

                print(f'{green}Tên Tài Khoản {do}: {trang}{USERNAME}')
                print(f'{green}ID Tài khoản {do}: {trang}{USERID}')
                print(f'{green}Bạn Đang Có {do}: {trang}{RUB} Rub')
                print()
                print(f'{xduong}-{hong}-{trang}-{do}-'*15, '\n')

                return USERNAME

        except:
            pass



    def XemQuangCao(self, USERNAME):
        try:
            while True:
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'cookie': self.COOKIE,
                    'priority': 'u=0, i',
                    'referer': 'https://aviso.bz/logout',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                }

                self.s.headers.update(headers)

                HOME = self.s.get('https://aviso.bz/work-serf', stream=True).text

                # Cho HTML Về Đạng Lưu Trữ bs4
                SOUP = BeautifulSoup(HOME, 'html.parser')

                # print(SOUP)

                # Tìm Tất Cả Elements HTML
                HTML = SOUP.find_all('div', id=re.compile(r'start-serf-\d+'))

                if not HTML:
                    for _ in range(15):
                        print(' '*50, end='\r')
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '     ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.    ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '..   ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '...  ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.... ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.....', end='\r'); time.sleep(1)

                    continue

                # Lất Value ID - HASH
                ID_HASH_TIME = []
                for DIV in HTML:
                    TAG = DIV.find('a', onclick=True)

                    if not TAG:
                        continue

                    ONCLICK = TAG['onclick']
                    MATCH = re.search(r"funcjs\['go-serf'\]\('(\d+)','([a-f0-9]+)'\);", ONCLICK)

                    if not MATCH:
                        continue

                    IDJOB = MATCH.group(1)
                    HASHJOB = MATCH.group(2)

                    # Lấy TIME Nếu Giá Trị Dúng
                    TIME_DIV = DIV.find_next('div', id=re.compile(r'serf-id-\d+'))

                    if not TIME_DIV:
                        continue

                    TIME_SPAN = TIME_DIV.find(string=re.compile(r'Таймер:'))

                    if not TIME_SPAN:
                        continue

                    TIME = TIME_SPAN.find_next('b').text
                    ID_HASH_TIME.append((IDJOB, HASHJOB, TIME))

                # Lấy ID - HASH - TIME
                for IDJOB, HASHJOB, TIME in ID_HASH_TIME:

                    # IDJOB = HOME.split('id="serf-link-')[1].split('"')[0]
                    # HASHJOB = HOME.split("('" + IDJOB + "','")[1].split("')")[0]
                    # TIME = HOME.split('Таймер: <b>')[1].split('</')[0]

                    headers1 = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'cookie': self.COOKIE,
                        'origin': 'https://aviso.bz',
                        'priority': 'u=1, i',
                        'referer': 'https://aviso.bz/work-serf',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                        'x-requested-with': 'XMLHttpRequest',
                    }

                    self.s.headers.update(headers1)

                    data = {
                        'id': IDJOB,
                        'hash': HASHJOB,
                        'func': 'go-serf',
                    }

                    CHECK1 = self.s.post('https://aviso.bz/ajax/earnings/ajax-serf.php', data=data, stream=True).json()

                    if 'html' not in CHECK1:
                        continue

                    elif 'start-error-serf' in CHECK1['html']:
                        self.DEMJOBLOI += 1

                        if self.DEMJOBLOI == 2:
                            self.DEMJOBLOI = 1
                            print(' '*50, end='\r')
                            for __ in range(17):
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '     ', end='\r'); time.sleep(1)
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '.    ', end='\r'); time.sleep(1)
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '..   ', end='\r'); time.sleep(1)
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '...  ', end='\r'); time.sleep(1)
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '.... ', end='\r'); time.sleep(1)
                                print(f'{vang}Nhiệm Vụ Lỗi Chờ Nhiệm Vụ Mới' + '.....', end='\r'); time.sleep(1)
                            continue

                        for ___ in range(3):
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '     ', end='\r'); time.sleep(1)
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '.    ', end='\r'); time.sleep(1)
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '..   ', end='\r'); time.sleep(1)
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '...  ', end='\r'); time.sleep(1)
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '.... ', end='\r'); time.sleep(1)
                            print(f'{vang}Nhiệm Vụ Lỗi Đang Bỏ Qua' + '.....', end='\r'); time.sleep(1)
                        continue


                    LINK = CHECK1['html'].split("open('")[1].split(':')[0]

                    if 'http' in LINK:
                        URL1 = CHECK1['html'].split('?sid=')[1].split('&id')[0]
                        URLID1 = CHECK1['html'].split('&id=')[1].split("')")[0]
                    elif 'https' in LINK:
                        URL1 = CHECK1['html'].split('?sid=')[1].split('&id')[0]
                        URLID1 = CHECK1['html'].split('&id=')[1].split("')")[0]
                    else:
                        continue

                    headers2 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cache-control': 'max-age=0',
                        'priority': 'u=0, i',
                        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    }

                    self.s.headers.update(headers2)

                    CHECK2 = self.s.get(f'https://twiron.com/view_surfing?sid={URL1}&id={URLID1}', stream=True).text

                    if '?sid=' not in CHECK2:
                        self.DEMJOBLOI = 1
                        continue

                    URL2 = CHECK2.split('?sid=')[1].split('"')[0]

                    if not URL2:
                        continue

                    headers3 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'priority': 'u=0, i',
                        'referer': f'https://twiron.com/view_surfing?sid={URL1}&id={URLID1}',
                        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'frame',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    }

                    self.s.headers.update(headers3)

                    CHECK3 = self.s.get(f'https://twiron.com/vlss?sid={URL2}', stream=True).text

                    if 'sid=' not in CHECK3:
                        self.DEMJOBLOI = 1
                        continue
                    
                    URL3 = CHECK3.split('sid=')[1].split('")')[0]

                    if not URL3:
                        continue

                    print(' '*50, end='\r')
                    for ____ in range(2, -1, -1):
                        print(f'{green}Đang Tìm Kiếm Nhiệm Vụ {do}: {trang}Quang Cao\r', end='', flush=True)
                        time.sleep(1.1)

                    print(f"{green}Tên Của Bạn Là {do}: {trang}{USERNAME}")
                    time.sleep(1)
                    print(f'{green}Hiện Đang Làm Nhiệm Vụ {do}: {trang}Quảng Cáo')
                    time.sleep(1)
                    for ne in range(int(TIME) + 5, -1, -1):
                        print(f'{green}Đang Xem Quảng Cáo {do}: {trang}{ne} \r', end='', flush=True)
                        time.sleep(1)

                    headers4 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'priority': 'u=0, i',
                        'referer': f'https://twiron.com/vlss?sid={URL3}',
                        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'frame',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    }

                    self.s.headers.update(headers4)

                    CHECK4 = self.s.get(f'https://twiron.com/vlss?view=ok&sid={URL3}', stream=True).text
                    URL4 = CHECK4.split('sid=')[1].split('"')[0]

                    if not URL4:
                        continue

                    headers5 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'priority': 'u=0, i',
                        'referer': f'https://twiron.com/vlss?view=ok&sid={URL4}',
                        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'frame',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    }

                    self.s.headers.update(headers5)

                    CHECK5 = self.s.get(f'https://twiron.com/vlss?view=ok&ds=clicked&sid={URL4}', stream=True).text
                    CLAIM = CHECK5.split('начислено ')[1].split(' руб')[0]
                    self.POINT += float(CLAIM)
                    LAMTRON = round(self.POINT, 3)

                    print(f"{green}Nhận {do}: {trang}{CLAIM} Rub {do}| {green}Đang Có{do} : {trang}{LAMTRON} Rub {do}|")
                    time.sleep(1)
                    print(f'{xduong}-{hong}-{trang}-{do}-'*10, '\r')

                    time.sleep(0.5)
                    for DELEY in range(self.DELEY, 0, -1):
                        print(f'Đang Nghỉ : {DELEY} giây ', end='\r')
                        time.sleep(1.5)

                    self.DEMJOBLOI = 0

        except:
            pass



    def XemYoutube(self, USERNAME):
        try:
            while True:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': self.COOKIE,
                    'priority': 'u=1, i',
                    'referer': 'https://aviso.bz/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                    'x-requested-with': 'XMLHttpRequest',
                }

                self.s.headers.update(headers)

                HOME = self.s.get('https://aviso.bz/work-youtube', stream=True).text
                # print(HOME)

                # Cho HTML Về Đạng Lưu Trữ bs4
                SOUP = BeautifulSoup(HOME, 'html.parser')

                # print(SOUP)

                # Tìm Div ID Và Hash
                HTML = SOUP.find_all('a', onclick=True)

                if not HTML:
                    for _ in range(15):
                        print(' '*50, end='\r')
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '     ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.    ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '..   ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '...  ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.... ', end='\r'); time.sleep(1)
                        print(f'{vang}Hết Job Vui Lòng Chờ' + '.....', end='\r'); time.sleep(1)
                    continue

                # Tìm Giá Trị ID và Hash
                ID_HASH = []
                for DIV in HTML:
                    ONCLICK = DIV['onclick']
                    MATCH = re.search(r'id=(\d+)&type=ads&hash=([a-f0-9]+)', ONCLICK.replace('&amp;', '&'))

                    if MATCH:
                        IDJOB = MATCH.group(1)
                        HASHJOB = MATCH.group(2)
                        ID_HASH.append((IDJOB, HASHJOB))

                for IDJOB, HASHJOB in ID_HASH:

                    headers1 = {
                        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'cookie': self.COOKIE,
                        'origin': 'https://aviso.bz',
                        'priority': 'u=1, i',
                        'referer': 'https://aviso.bz/work-youtube',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                        'x-requested-with': 'XMLHttpRequest',
                    }

                    self.s.headers.update(headers1)

                    data1 = {
                        'id': IDJOB,
                        'hash': HASHJOB,
                        'func': 'ads-start',
                        'user_response': '',
                        'count_captcha_subscribe': '',
                        'checkStepOneCaptchaSubscribe': False
                    }

                    CHECK1 = self.s.post('https://aviso.bz/ajax/earnings/ajax-youtube.php', data=data1, stream=True).json()
                    # print(CHECK1)

                    if 'html' not in CHECK1:
                        continue

                    elif 'HASH сумма не совпадает' in CHECK1['html']:
                        print('Lỗi Lấy Hash')
                        continue

                    VIDDEO = CHECK1['html'].split('?video_id=')[1].split('&')[0]
                    TIME = CHECK1['html'].split('&timer=')[1].split('&')[0]
                    REPORT = CHECK1['html'].split('&report_id=')[1].split('&')[0]
                    TASK = CHECK1['html'].split('&task_id=')[1].split('&')[0]
                    HASH = CHECK1['html'].split('&hash=')[1].split('"')[0]

                    if not VIDDEO and TIME and REPORT and TASK and HASH:
                        print(CHECK1)
                        continue

                    print(' '*50, end='\r')
                    for __ in range(2):
                        print(f'{green}Đang Tìm Kiếm Nhiệm Vụ {do}: {trang}Youtube\r', end='', flush=True)
                        time.sleep(1)
                    # print(f"VIDEO: {VIDDEO}")
                    # print(f"TIME: {TIME}")
                    # print(f"REPORT: {REPORT}")
                    # print(f"TASK: {TASK}")
                    # print(f"HASH: {HASH}")

                    headers2 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cache-control': 'max-age=0',
                        # 'if-modified-since': 'Thu, 27 Jun 2024 14:05:59 GMT',
                        # 'if-none-match': 'W/"a6c3d346a4fe75bc21f6a0cbcf6d87d49db8c9e97047e85d8024f7f20a02a3a1"',
                        'priority': 'u=0, i',
                        'referer': 'https://aviso.bz/',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'cross-site',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                    }

                    self.s.headers.update(headers2)


                    CHECK2 = self.s.get(f'https://premiumvideoblog.blogspot.com/?video_id={VIDDEO}&timer={TIME}&report_id={REPORT}&task_id={TASK}&hash={HASH}&m=1', stream=True).text

                    print(f"{green}Tên Của Bạn Là {do}: {trang}{USERNAME}")
                    time.sleep(1)
                    print(f'{green}Hiện Đang Làm Nhiệm Vụ {do}: {trang}Youtube')
                    time.sleep(1)
                    for ne in range(int(TIME), -1, -1):
                        print(f'{green}Đang Xem Video Đợi {do}: {trang}{ne} giây \r', end='', flush=True)
                        time.sleep(1.15)
                    
                    headers3 = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'origin': 'https://premiumvideoblog.blogspot.com',
                        'priority': 'u=1, i',
                        'referer': 'https://premiumvideoblog.blogspot.com/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                    }

                    self.s.headers.update(headers3)

                    data2 = {
                        'hash': HASH,
                        'report_id': REPORT,
                        'task_id': TASK,
                        'timer': TIME,
                        'player_time': float(TIME) + 0.896152908447266,
                        'video_id': VIDDEO,
                        'stage': '1',
                        'player_state': '1',
                    }

                    CHECK3 = self.s.post('https://aviso.bz/ajax/earnings/ajax-youtube-external.php', data=data2, stream=True).json()

                    if 'premiumvideoblog' in CHECK3['code']:
                        continue

                    CLAIM = CHECK3['html'].split('<b>')[1].split('</b>')[0]
                    self.POINT += float(CLAIM)
                    LAMTRON = round(self.POINT, 3)

                    print(f"{green}Nhận {do}: {trang}{CLAIM} Rub {do}| {green}Đang Có{do} : {trang}{LAMTRON} Rub {do}|")
                    time.sleep(1)
                    print(f'{xduong}-{hong}-{trang}-{do}-'*10, '\r')

                    time.sleep(0.5)
                    for DELEY in range(self.DELEY, 0, -1):
                        print(f'{green}Đang Nghỉ {do}: {trang}{DELEY} giây ', end='\r')
                        time.sleep(1.5)

        except:
            pass



def main():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        COOKIE = input(f'{green}Nhập Cookie : {trang}')
        DELEY = int(input(f'{green}Nhập Deley : {trang}'))
        os.system("cls" if os.name == "nt" else "clear")
        Api = Aviso(COOKIE, DELEY)
        USERNAME = Api.checkUser()
        Api.XemQuangCao(USERNAME)
        Api.XemYoutube(USERNAME)

    except:
        pass



if __name__=='__main__':
    try:
        main()
    except:
        pass