import baoxian
import win32api
import win32con
import time
while True:
    if (win32api.GetAsyncKeyState(win32con.VK_F1) < 0):
        baoxian.run()
    time.sleep(2)
        ##监听循环
        