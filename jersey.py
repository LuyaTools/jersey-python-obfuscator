import os
import sys
import base64
from base64 import *
from colorama import init, Fore, Style
init()
from datetime import datetime
import time
from time import sleep
import platform
from pathlib import Path
import marshal, zlib, base64, lzma
r = Fore.GREEN
w = Fore.WHITE
ti = f"""{r}
                                 ▄▄▄██▀▀▀▓█████  ██▀███    ██████ ▓█████▓██   ██▓
                                   ▒██   ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ ▒██  ██▒   {w}┌─┐┌┐ ┌─┐┬ ┬┌─┐┌─┐┌─┐┌┬┐┌─┐┬─┐{r}
                                   ░██   ▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███    ▒██ ██░   {w}│ │├┴┐├┤ │ │└─┐│  ├─┤ │ │ │├┬┘{r}
    {w}Best Python Obfuscator{r}      ▓██▄██▓  ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄  ░ ▐██▓░   {w}└─┘└─┘└  └─┘└─┘└─┘┴ ┴ ┴ └─┘┴└─{r}
                                 ▓███▒   ░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒ ░ ██▒▓░                       V1.0
                                 ▒▓▒▒░   ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░  ██▒▒▒     
                                 ▒ ░▒░    ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░▓██ ░▒░    
                                 ░ ░ ░      ░     ░░   ░ ░  ░  ░     ░   ▒ ▒ ░░      
                                 ░   ░      ░  ░   ░           ░     ░  ░░ ░     
                                                                         ░ ░     {w}
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{r}    https://blizz.cf/    {w}https://discord.gg/ma3vc6ZysW    {r}https://github.com/LuyaTools/    {w}https://t.me/bladetools
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
osn = platform.system()


if osn == "Windows":
    pass
else:
    print(f"[{r}!{w}] Error: {r}Unsupported OS:{w} {osn}")
    time.sleep(3)
    sys.exit()
os.system("cls")
os.system("title JERSEY PY-OBFUSCATOR [https://blizz.cf/]")
print("credits to Vesper#0003\nMade it to a console-only script!")
time.sleep(2)
os.system("cls")
print(ti)
input(f"{w}                                                [{r}JERSEY{w}] Press Enter > ")
def pyobf():
    os.system("cls")
    print(ti)
    src = input(f"{w}[{r}JERSEY{w}] Python-File-Location: ")
    path = Path(src)
    if path.is_file():
        print(f"{w}[{r}JERSEY{w}] SUCCESS: Found file! Checking...")
    else:
        print(f"{w}[{r}JERSEY{w}] ERROR: File not found!")
        time.sleep(5)
        sys.exit()
    with open(src, 'r',errors='ignore') as f:
        if src.endswith('.py'):
            print(f"{w}[{r}JERSEY{w}] SUCCESS: File is a Python-File! Starting Obfuscation...")
        else:
            print(f"{w}[{r}JERSEY{w}] ERROR: Not a Python file!")
            time.sleep(5)
            sys.exit()
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode7 = lzma.compress(encode2)
    encode3 = base64.b64encode(encode7)
    encode6 = base64.b85encode(encode3)
    symbol = '__JERSEY_WALL' *75
    with open(src, 'r',errors='ignore') as e:
        MONKEYHAHA = e.read()
    with open(src, 'w') as f:
        f.write(symbol+f"='{symbol}'\n")
        f.write("import base64, marshal, zlib, lzma\n")
        f.write(symbol+f"='{symbol}'\n")
        f.write("\n"+symbol+f"='{symbol}'\n")
        f.write("\n"+MONKEYHAHA)
        f.write("\n"+symbol+f"='{symbol}'\n")
    b64 = lambda _monkay : base64.b64encode(_monkay)
    mar = lambda _monkay : marshal.dumps(compile(_monkay,'<x>','exec'))
    zlb = lambda _monkay : zlib.compress(_monkay)
    OFFSET = 100
    symbol = '__JERSEY_JERSEY' * 50
    with open(src, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{symbol} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) +1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{symbol} += "{_str}"\n'
        index += OFFSET
    code2 =  f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({symbol}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    for x in range(5):
        method = repr(b64(zlb(mar(code2.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    marsrc = compile(beforemarsh, 'coduter', 'exec')
    obfmarsh = marshal.dumps(marsrc)
    print(f"{w}┌───[{r}JERSEY{w}] Starting...")
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added Marshal..")
    obfzlib = zlib.compress(obfmarsh)
    time.sleep(0.2)
    now2 = datetime.now()
    ct = now2.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added zlib..")
    obflzma = lzma.compress(obfzlib)
    now3 = datetime.now()
    ct = now3.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added lzma..")
    obfbase64 = base64.b64encode(obflzma)
    time.sleep(0.1)
    now4 = datetime.now()
    ct = now4.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added base64..")
    obfbase16 = base64.b16encode(obfbase64)
    now5 = datetime.now()
    ct = now5.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added base16..")
    obfbase32 = base64.b32encode(obfbase16)
    time.sleep(0.5)
    now6 = datetime.now()
    ct = now6.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added base32..")
    obfbase85 = base64.b85encode(obfbase32)
    now7 = datetime.now()
    ct = now7.strftime("%H:%M:%S")
    print(f"{w}│ [{r}JERSEY{w}] [{r}{ct}{w}] {r}Added base85..")
    code += f'exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b16decode(base64.b32decode(base64.b85decode({obfbase85}))))))))'
    with open(src, 'w+',errors='ignore') as f:
        f.write("import marshal, zlib, base64, lzma\n")
        f.write(code)
        f.write(f"\n{symbol} = '{symbol}'")
    print(f"{w}└───[{r}JERSEY{w}] SUCCESS: Successfully updated your file. Encryption & Walls Added")
    time.sleep(10)
    os.system("cls")
    pyobf()
pyobf()