import time

import tkinter as tk

from MachineURL import *
from StatusFetcher import *


def repeatCheck(url):
    counter = 0
    while True:
        status = getStatus(url)
        available = status[0]
        if available:
            #弹出窗口可以洗衣
            root = tk.Tk()
            root.title('洗衣机')
            root.geometry('300x200')
            tk.Label(root, text='可以洗衣').pack()
            tk.Button(root, text='确定', command=root.quit).pack()
            root.mainloop()
            print('可以洗衣')
            break
        else:
            counter += 1
            print("尝试次数:"+str(counter)+" "+str(status[0]))
        time.sleep(5)


repeatCheck(D19_ZhaoJi_Floor_2)
