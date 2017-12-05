#!/usr/bin/python3
#
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
#
# https://pillow.readthedocs.io/en/4.3.x/reference/ImageDraw.html
#

from PIL import Image, ImageDraw, ImageFont


def add_num(pic_path, num):
    image = Image.open(pic_path)
    x_size, y_size = image.size

    print('x_size={} y_size={}'.format(x_size, y_size))
    font_size = y_size / 4
    position = x_size - font_size

    print('font_size={} position={}'.format(font_size, position))

    # myfont = ImageFont.truetype('Futura.tff', font_size)
    # 注意，font_size 只能是正整数，不能是小数
    myfont = ImageFont.truetype("arial.ttf", int(font_size))

    print('font load success!')

    ImageDraw.Draw(image).text(
        (position, 0), str(num), font=myfont, fill='red')
    image.save('icon_with_num.jpg')

    print('done!')


if __name__ == '__main__':
    add_num('avantar.png', 3)
