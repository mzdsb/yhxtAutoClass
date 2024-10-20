import ddddocr


def recognize_captcha(image_path):
    # 创建 ddddocr 的识别器对象
    ocr = ddddocr.DdddOcr()

    # 读取图片数据
    with open(image_path, 'rb') as f:
        img_bytes = f.read()

    # 使用 ddddocr 进行识别
    result = ocr.classification(img_bytes)

    # 返回识别结果
    return result


# 调用函数识别验证码
image_path = "C:/Users/42509/Desktop/code.png"  # 替换成你的验证码图片路径
captcha_text = recognize_captcha(image_path)
print("识别出的验证码:", captcha_text)
