from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def get_check_code_info():
    # 随机码 默认长度=1
    def random_code():
        s = '1234567890qwertyuiopasdfghjkklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        check_codes = ''
        for _ in range(4):
            check_code = random.choice(s)
            check_codes += check_code
        return check_codes

    # 随机颜色 默认颜色范围【1，255】
    def random_color(s=1, e=255):
        return (random.randint(s, e), random.randint(s, e), random.randint(s, e))

    # 生成验证码图片
    # length 验证码长度
    # width 图片宽度
    # height 图片高度
    # 返回验证码和图片
    def check_code(lenght=4, width=80, height=38):
        # 创建Image对象
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建Font对象
        font = ImageFont.truetype('./static/Admin/font/fonts/Arial.ttf', size=28)
        # 创建Draw对象
        draw = ImageDraw.Draw(image)
        # 随机颜色填充每个像素
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=random_color(64, 255))
        # 验证码
        code = random_code()
        # 随机颜色验证码写到图片上
        for t in range(lenght):
            draw.text((20 * t + 5, 5), code[t], font=font, fill=random_color(32, 127))
        return code, image

    f = BytesIO()
    code, image = check_code()
    image = image.save(f, 'jpeg')
    return code, image