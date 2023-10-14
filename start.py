import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich import print as cetak

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
bul = '••••••••••••••••••••••••••••••••••••••'
os.system('clear')
print(f"""
{xxx}Hello {hijo} Ardiyanta Saputro{xxx},Wellcome In
{bira}╔════╦═╗╔═╦═══╦═══╗ 
╚══╗═╠╗╚╝╔╣╔══╣╔═╗║
──╔╝╔╝╚╗╔╝║╚══╣║─╚╝
{hijo}─╔╝╔╝─╔╝╚╗║╔══╣║─╔╗
╔╝═╚═╦╝╔╗╚╣║──║╚═╝║
╚════╩═╝╚═╩╝──╚═══╝
   {xxx} Aungthor By : {hijo}༶•┈┈⛧┈♛ {xxx}𝑍𝑒𝑛𝑖𝑥𝑥77{hijo} ♛┈⛧┈┈•༶ """)
print(f"""{hijo}{bul}{xxx}
1. crack friendlist  ({hijo} wajib public {xxx})      
2. crack followers ({hijo} crack pengikut{xxx} )
ketik {mer}logout {xxx}untuk menghapus cookie
{hijo}{bul}""")
ap = input(f'{hijo} question{xxx} : ')                              