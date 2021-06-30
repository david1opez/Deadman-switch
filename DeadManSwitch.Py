import time, pyAesCrypt, requests, os

url = "https://github.com/david1opez/Game-of-Life/blob/79286dc44dc71c8da986d83d362474c631480f05/wall.aes?raw=true"
r = requests.get(url, allow_redirects=True)
open('wall.aes', 'wb').write(r.content)

i = 3

def decrypt(i):
    while i > 0:
        print(i, "attempts left")
        i -= 1
        password = input("5 digit password to unencrypt files:")

        try:
            pyAesCrypt.decryptFile("wall.aes", "index.html", password, (64 * 1024))
            print("\033[92m[CONGRATULATIONS] Password accepted\033[0m")
            os.remove("wall.aes")
            exit()
        except:
            print("\033[91mWrong password, please try again\033[0m")
            decrypt(i)
    
    print("Deleting files...")
    os.remove("DeadManSwitch.py")
    os.remove("wall.aes")
    exit()

decrypt(i)
