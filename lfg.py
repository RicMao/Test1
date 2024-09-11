from colorthon import Colors
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH
import random
import requests, os, requests_random_user_agent
import time, re, platform


def getClear():
    os.system('cls' if os.name == 'nt' else 'clear')


def ethBal(addr: str):
    url = f"https://ethbook.guarda.co/api/v2/address/{addr}"
    req = requests.get(url)
    if req.status_code == 200:
        ret = int(dict(req.json())['balance'])
        return ret / 1000000000000000000
    else:
        return 0


def getBal(addr):
    rl = f"https://btcbook.guarda.co/api/v2/address/{addr}"
    req = requests.get(rl)
    if req.status_code == 200:
        ret = int(dict(req.json())['balance'])
        return ret / 1000000000
    else:
        return 0
        time.sleep(0.001)


# ------------------------------------------------------------------------

green = Colors.GREEN
red = Colors.RED
white = Colors.WHITE
yellow = Colors.YELLOW
reset = Colors.RESET
getClear()
# ------------------------------------------------------------------------
print('Are You Ready COKK ?!...')
# ------------------------------------------------------------------------
z = 1
ff = 0

while True:
    PRIVATE_KEY = "".join(random.choice("0123456789abcdef") for _ in range(64))
    
    hd_btc: HDWallet = HDWallet(BTC)
    hd_eth: HDWallet = HDWallet(ETH)
    hd_btc.from_private_key(PRIVATE_KEY)
    hd_eth.from_private_key(PRIVATE_KEY)
    ethaddr = hd_eth.p2pkh_address()
    btcaddr1 = hd_btc.p2pkh_address()
    # ------------------------------------------------------------------------
    value1 = getBal(btcaddr1)
    val_et = ethBal(ethaddr)
    # ------------------------------------------------------------------------
    getClear()
    promptPUB = '''
        ************** L F G *************
        *                                *
        *            CREATOR             *
        *         ** Rico-Mao **         *
        *    Jangan Lupa Sawer Cokk      *
        *                                *
        *********** G A S P O L **********
            '''
    print(yellow, promptPUB, reset)
    print(f"{white}[{reset}{white}Scan{reset}:{yellow} {z}{reset} {white}Found{reset}: {green}{ff}{reset}{white}]{reset}")
    print(f"Key | {green}{PRIVATE_KEY}{reset}")
    print(f"BTC | BAL: {yellow}{value1}{reset} |{white}{btcaddr1}{reset}")
    print(f"ETH | BAL: {yellow}{val_et}{reset} |{white}{ethaddr}{reset}")
    
    z += 1
    # ------------------------------------------------------------------------
    if value1 > 0.0001:
        ff += 1
        open('btcWin.txt', 'a').write(f'{btcaddr1}\n{PRIVATE_KEY}\n')
    elif val_et > 0.001:
        ff += 1
        open('btcWin.txt', 'a').write(f'{ethaddr}\n{PRIVATE_KEY}\n')
    else:
        break
 
