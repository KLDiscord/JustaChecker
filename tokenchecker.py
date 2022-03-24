import os, time, sys 

try : 
    import requests
except ModuleNotFoundError:
    print("Can't find requests module.\n Installing in 3 secs...")
    time.sleep(3)
    os.system("pip install requests")
    os.system("cls")
    import requests
    
l = ""
try :  
    f = open("beforetokens.txt","r")
except :
    print("Can't find beforetokens.txt.\nPlease check again.")
    time.sleep(3)
    sys.exit()

print("JustaChecker v.1.0 by kldiscord in github\n\n")

r = f.readlines()
w = 0
v = 0
n = len(r)
for i in range(1,n):
    rr = r[i]
    headers={ 
        'Authorization': rr[:-1]
    }
    src = requests.get('https://discordapp.com/api/v8/auth/login', headers=headers) 
    if src.status_code == 200:
        w += 1
        print(f"Token works | token : {rr[:-1]}")
        os.system(f"title JustaChecker - Tokens [{i}] Worked [{w}] Invalid[{v}]")
        l += rr[:-1] + "\n"
    else:
        v += 1
        print(f"Token dosen't works | token : {rr[:-1]}")
        os.system(f"title JustaChecker - Tokens [{i}] Worked [{w}] Invalid[{v}]")
        
f = open("Token_Worked.txt","w")
f.writelines(str(l)[1:-1])
input("\nWorking Tokens saved at Token_Worked.txt\nPress enter to close")
