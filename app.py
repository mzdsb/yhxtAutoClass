from flask import Flask,request, jsonify
import ddddocr
from flask_cors import CORS  # 导入CORS


app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": ["https://zswxy.yinghuaonline.com","https://swxygyxy.gongyixy.com","https://swxyzxshixun.canghuikeji.com"]}}) # 启用CORS
# 定义验证码识别函数
def recognize_captcha(image_bytes):
    ocr = ddddocr.DdddOcr()
    result = ocr.classification(image_bytes)
    return result

@app.route('/upload', methods=['POST'])
# def hello_world():  # put application's code here
#     return 'Hello World!'
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # 读取上传的图片文件为二进制数据
        img_bytes = file.read()

        # 调用验证码识别函数
        captcha_text = recognize_captcha(img_bytes)
        print("验证码为:"+captcha_text)
        # 返回识别的验证码结果
        return jsonify({'captcha': captcha_text}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
