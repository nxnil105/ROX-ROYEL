import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://www.facebook.com/Captain.TaRikuL.420')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from Sun-ROX.py import Subscraption
 
        Subscraption()
 
 
 
elif bit == "32bit":
 
        from Sun-ROX.py import Subscraption
 
 
        Subscraption()
