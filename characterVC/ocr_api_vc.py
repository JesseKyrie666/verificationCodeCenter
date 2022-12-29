# coding=utf-8

from tools_ocr.fast_run import ocr_img
import re


# 匹配数字英文字母验证码
def ocr_vc_en_num(img):
    # 输入验证码图片路径，返回识别结果
    result_ori = ocr_img(img)

    # print("====>识别结果", result)
    # 识别情况以及解决方案
    ## 1. 识别结果有包含其他特殊字符【.4 :d 21】，使用正则提取数字英文字母
    regex_type_1 = r"[a-zA-Z0-9]+"
    results_1 = re.findall(regex_type_1, result_ori)
    result_str = "".join(results_1)
    # print("====>识别结果", result_str)

    return result_str
