import cv2
import pyautogui
import numpy as np

def match_bool(model_path, image_path, threshold):  #返回匹配结果真假
    
    model_img = cv2.imread(model_path, cv2.IMREAD_GRAYSCALE)
    large_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if model_img is None or large_img is None:
        raise ValueError("无法加载图像，请检查路径是否正确")

    # 执行模板匹配
    result = cv2.matchTemplate(large_img, model_img, cv2.TM_CCOEFF_NORMED)
    # 获取最大匹配值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 判断最大相似度是否大于最低要求
    if max_val >= threshold:
        return True
    else:
        return False
def find_photo(small_image_path,threshold): #寻找图片，返回真假
    pyautogui.screenshot().save("./screen/screen.png")
    large_image_path="./screen/screen.png"
    return match_bool(small_image_path, large_image_path, threshold)
def get_xy(small_image_path): #获取图片坐标，返回坐标元组
    
    large_image_path="./screen/map.png"
    
    model_img = cv2.imread(small_image_path, cv2.IMREAD_GRAYSCALE)
    large_img = cv2.imread(large_image_path, cv2.IMREAD_GRAYSCALE)

    if model_img is None or large_img is None:
        raise ValueError("无法加载图像，请检查路径是否正确")

    # 执行模板匹配
    result = cv2.matchTemplate(large_img, model_img, cv2.TM_CCOEFF_NORMED)
    # 获取最大匹配值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    centre = (max_loc[0] + int(model_img.shape[1]/2), max_loc[1] + int(model_img.shape[0]/2))

    # 返回坐标元组
    return (centre[0], centre[1])
