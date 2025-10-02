import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [â€¢] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/F3IhtLI7duf4pMkhhXJSfd?mode=ems_copy_t')
tokyo=platform.architecture()[0]
if tokyo=="32bit":
    os.system('clear')
    print('\033[91;1m [â€¢] 32 Bit Device Not Working')
elif tokyo=="64bit":
    __import__("absmystery")