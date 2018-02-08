from PIL import Image, ImageDraw, ImageChops
import os
from pretreat_image import pretreat_image
from cut_all_char import *


# 生成存放样本的文件夹
def new_char_folder():
    # 0-9
    for k in range(48, 58):
        try:
            os.mkdir('captcha_char/%c' % k)
        except:
            pass

    # A-Z
    for k in range(65, 91):
        try:
            os.mkdir('captcha_char/%c' % k)
        except:
            pass


# 生成样本字符,然后手动将对应字符移动到上面生成的文件夹中
# 每个文件夹手动移动10个以上
def new_char_example():
    new_char_folder()
    for s in range(300):
        images = Image.open('captcha_example/%d.jpg' % s)
        image = pretreat_image(images)
        image.save('captcha_char/%d.png' % s)
        image_char_list = cut_all_char(image)
        for k in range(4):
            image_char_list[k].save('captcha_char/%d_%d.png' % (s, k))


if __name__ == '__main__':
    new_char_example()