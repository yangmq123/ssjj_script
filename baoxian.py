import pyautogui
import time
import match
import win32api
import win32con

def run():
    def f(a,b,c,d):
        return (a,b,c-a,d-b)#转换为区域坐标
    def g(x):
        if x == 0:
            return ["A",65]
        elif x == 1:
            return ["D",68]
        elif x == 2:
            return ["S",83]
        elif x == 3:
            return ["W",87]
    list1 = [(688,616,750,681),(767,616,832,681),(849,616,911,681),(928,618,990,682),(1008,617,1072,682),(1085,616,1152,685),(1164,616,1233,685)]
    list2 = [f(*item) for item in list1]#区域坐标列表
    result = []
    model = ["./model/A.png","./model/D.png","./model/S.png","./model/W.png"]

    for i in range(len(list2)):
        screenshot = pyautogui.screenshot(region=list2[i])
        screenshot.save(f"./screen/area_{i}.png")
    for i in range(7):
        for j in range(4):
            if(match.match_bool(model[j],f"./screen/area_{i}.png",0.9)):
                result.append(g(j))
    for item in result:
        print(f"{item[0]}",end="")
    print("\n开始执行按键")
    for item in result:
        val = item[1]
        
        win32api.keybd_event(val, 0, 0, 0)
        time.sleep(0.03)
        win32api.keybd_event(val, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.03)
