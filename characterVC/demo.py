# coding=utf-8

# 测试案例
from ocr_api_vc import ocr_vc_en_num

if __name__ == '__main__':
    # 图片路径
    img_path = 'imgs/2.png'
    # 调用识别方法
    result = ocr_vc_en_num(img_path)
    # 打印识别结果 ====>识别结果 3561
    print("====>识别结果", result)
