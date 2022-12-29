# coding=utf-8

from req_demo import get_api
import requests
import base64



def ocr_img(img):
    # 读取图片，并转换为base64编码
    with open(img, 'rb') as f:
        img = base64.b64encode(f.read())
        # 转换维字符串
        img = str(img, 'utf-8')
        json_data = {
            'image': img,
        }
        # print(json_data)
        results = get_api(json_data)
        end_str = ""
        # 拼接识别结果，通过正则获取到时间
        for one_result in results:
            # print(one_result)
            data = one_result['data']
            for one_data in data:
                end_str += one_data['text']
    return end_str



