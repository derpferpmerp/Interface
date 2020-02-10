#-------------------------------------------------------------#
#------------------------Variables----------------------------#
#-------------------------------------------------------------#
cmdlist = ['scan', 'probe', 'crack', 'exit', '^C', '^c']
BSSIDS = []
BSSID = 0
OpenPort = 0
CH = 8
Pass = 0
#-------------------------------------------------------------#
#-------------------------Modules-----------------------------#
#-------------------------------------------------------------#
import time
import random
from tqdm import tqdm
import sys
from termcolor import cprint
#-------------------------------------------------------------#
#------------------------Functions----------------------------#
#-------------------------------------------------------------#
def displayhacked():
    for i in ['H', 'A', 'C', 'K', 'I', 'N', 'G']:
        # print 4 lines
        print(str(i))
        time.sleep(0.25)
        sys.stdout.write("\033[0A")  # go up 4 lines


def scan():
    global BSSID
    global CH
    with tqdm(
            total=100,
            desc="Scanning: ",
            bar_format="{l_bar}{bar} [ time left: {remaining} ] ") as pbar:
        for i in range(100):
            time.sleep(0.1)
            pbar.update(1)
    BSSID = '68:bc:0c:f8:65:4c'
    CH = 8
    print('Network: ETHS')
    print('BSSID: 68:bc:0c:f8:65:4c')
    print('CH: 8')
    ask()


def probe():
    g=raw_input('probe ' + BSSID + ' ')
    if (g==str(CH)):
      print('Probing for Open Ports from Ports 1-1000')
      global OpenPort
      OpenPort = random.randint(1, 1000)
      with tqdm(
              total=100,
              desc="Probing: ",
              bar_format="{l_bar}{bar} [ time left: {remaining} ] ") as pbar:
          for i in range(100):
              time.sleep(0.1)
              pbar.update(1)
      print('Open port found on ' + str(OpenPort) + '.')
      ask()
    else:
      cprint("The selected channel does not exist", 'green', attrs=['bold'], file=sys.stderr)
      ask()


def crack():
    c = raw_input('crack ' + BSSID + ' ' + str(CH) + ' ')
    if (c == str(OpenPort)):
        print('Scanning all possible passwords for ETHS')
        with tqdm(
                total=100,
                desc="Cracking: ",
                bar_format="{l_bar}{bar} [ time left: {remaining} ] ") as pbar:
            for i in range(100):
                time.sleep(0.1)
                pbar.update(1)
        cprint("Hacked!", 'red', attrs=['bold'], file=sys.stderr)
        displayhacked()
        displayhacked()
        displayhacked()
        displayhacked()
        print('Password: ' + str(Pass))
    else:
        cprint("Selected Port is not Available", 'green', attrs=['bold'], file=sys.stderr)
        ask()


def ask():
    cmd = raw_input('')
    if cmd == 'help':
        print(' --scan: <CH>')
        print(' --probe: <BSSID> <SP> <EP>')
        print(' --crack: <BSSID> <OpenChannel>')
        ask()
    elif cmd == 'scan':
        scan()
    elif 'probe' in cmd:
        probe()
    elif cmd == 'crack':
        crack()
    elif cmd not in cmdlist:
        cprint("Unrecognized Command. Type help for a list of commands.", 'green', attrs=['bold'], file=sys.stderr)
        ask()


def execute():
    print(' --scan: <CH>')
    print(' --probe: <BSSID> <SP> <EP>')
    print(' --crack: <BSSID> <OpenChannel>')
    ask()


execute()