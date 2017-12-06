#!/usr/bin/python3
#
# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#
# iphone5 分辨率: 1136*640

# 使用 Image thumbnail 就可以完成
# https://pillow.readthedocs.io/en/4.3.x/reference/Image.html?highlight=size#create-thumbnails


from PIL import Image

x = 640
y = 1136


image_file = 'cloud.jpg'
image_file = 'yourname.jpg'
image_file = 'yourname_v.jpg'
file, ext = image_file.split('.')


def resize(image_file):

    im = Image.open(image_file)

    # print(im.size)
    # print(type(im.size))

    im_x, im_y = im.size
    # 判断图片是横竖屏
    if im_x > im_y:
        # 横
        im.thumbnail((y, x))
    else:
        # 竖
        im.thumbnail((x, y))

    # im.thumbnail((x, y))
    im.save(file + '.thumbnail.' + ext)


if __name__ == "__main__":
    resize(image_file)
