from PIL import Image
import os


def IsValidImage(img_path):
    """
    判断文件是否为有效（完整）的图片
    :param img_path:图片路径
    :return:True：有效 False：无效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except Exception as e:
        print(e)
        bValid = False
    return bValid


def tranImg(img_path):
    """
    转换图片格式
    :param img_path:图片路径
    :return: True：成功 False：失败
    """
    if IsValidImage(img_path):
        try:
            output_img_path = img_path.rsplit(".", 1)[0] + ".png"
            im = Image.open(img_path)
            im.save(output_img_path)
            os.remove(img_path)
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False


if __name__ == '__main__':
    for file in os.listdir("../web/img/temp/"):
        print(tranImg("../web/img/temp/" + file))
