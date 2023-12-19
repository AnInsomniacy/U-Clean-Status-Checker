import time
import tkinter as tk
from MachineURL import *
from StatusFetcher import *


def create_window():
    root = tk.Tk()
    root.title('洗衣机')

    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口大小
    window_width = 300
    window_height = 200

    # 计算窗口位置
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # 设置窗口位置
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, position_right, position_top))

    tk.Label(root, text='可以洗衣').pack()
    tk.Button(root, text='确定', command=root.quit).pack()
    root.mainloop()


def check_status(url1, url2):
    counter = 0
    flag = True
    while True:
        url = url1 if flag else url2
        status = getStatus(url)
        available = status[0]
        if available:
            print('可以洗衣')
            create_window()
            break
        else:
            # 翻转flag
            flag = not flag
            counter += 1
            print("尝试次数:" + str(counter) + " " + str(status[0]))
        time.sleep(5)


def repeat_check():
    url1 = D19_ZhaoJi_Floor_3
    url2 = D19_ZhaoJi_Floor_2
    check_status(url1, url2)


repeat_check()
