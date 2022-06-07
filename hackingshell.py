import os 

banner = '''
██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝  ██████╔╝██║░░██║███████╗███████╗███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝'''
print(banner)
print("linux only")

def menu():
    print('''
    1 nmap scan 
    2 arp poisoning 
    3 wire shark''')
menu()
cho = input("    ")

if cho == "1":
    print('''
    1 full net scan 
    2 port scan 
    3 vulnerability scan ''')
s = input("    ")

ip = input("enter ip ")
if s == "1":
    os.system("nmap -sn "+ip+"")
elif s == "2":
    os.system("nmap -sC -sV "+ip+"")

elif s == "3":
    print("be patien this may take long ")
    os.system("nmap --script vuln"+ip+"")

if cho == "2":
    os.system("python3 arppoison.py")    

if cho == "3":
    os.system("wireshark")










