# coding=utf-8

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


def get_api(json_data):
    cookies = {
        'Hm_lvt_89be97848720f62fa00a07b1e0d83ae6': '1671067653',
        'Hm_lpvt_89be97848720f62fa00a07b1e0d83ae6': '1671067653',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Hm_lvt_89be97848720f62fa00a07b1e0d83ae6=1671067653; Hm_lpvt_89be97848720f62fa00a07b1e0d83ae6=1671067653',
        'Origin': 'https://www.paddlepaddle.org.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://www.paddlepaddle.org.cn/hub/scene/ocr',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        'https://www.paddlepaddle.org.cn/paddlehub-api/image_classification/chinese_ocr_db_crnn_mobile',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    # print("====>接口响应状态码", response.status_code)
    # print("====>接口响应时间", response.elapsed.total_seconds())
    rep_dict = response.json()
    hit = rep_dict["result"]
    # print("baidu ocr result >>>>>>", hit)
    return hit


# if __name__ == '__main__':
#     png = '../captcha.png'
#     result = ocr_img(png)
#     print("result===>", result)
