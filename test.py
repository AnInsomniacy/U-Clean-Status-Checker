import time

import tkinter as tk

from MachineURL import *
from StatusFetcher import *


def repeatCheck(url):

    while True:
        status = getStatus(url)
        available = status[0]
        if available:
            root = tk.Tk()
            root.title('可以洗衣')
            print('可以洗衣')
        else:
            print(status[0])
        time.sleep(1)


repeatCheck(D19_ZhaoJi_Floor_1)
