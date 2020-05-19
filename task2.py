import glob
import os
import shutil


def get_image_pd(img_root):
    """
    :param img_root: 图片根目录
    :return: 图片路径列表
    """
    img_list = glob.glob(img_root + "/*/*/*.jpg")
    return img_list


def save_single_image(img_path, target, new_name):
    """
    :param img_path: 单个图片路径
            new_name:保存的名字
            target: 保存的路径
    """
    # print(img_path)
    shutil.copyfile(img_path, target + '/' + new_name)


def main():
    img_root = "D:\Code\Python\Machine_study\医学图像识别实战\数据\任务2测试数据\Ear-disease"
    target = 'D:\Code\Python\Machine_study\医学图像识别实战\数据\任务2测试数据\专业2班XX14'
    if not os.path.exists(target):  # 目录不存在则创建
        os.mkdir(target)
        print("成功创建目录")

    for i in range(1, 6, 1):  # 创建1-5文件夹
        if not os.path.exists(target + "/" + str(i)):
            os.mkdir(target + "/" + str(i))
            print("成功创建文件夹", end=" ")

    img_list = get_image_pd(img_root)  # 图像路径列表
    print("共有图片{}张".format(len(img_list)))
    count = 0
    for i in range(len(img_list)):
        imgname = img_list[i].split("\\")[-1]  # 提取图片名字
        classification = imgname[0]  # 提取图片第一个字符，判断图片放入哪个文件夹
        num_newname = len(os.listdir(target + '/' + classification))
        # print(num_newname)
        try:
            save_single_image(img_list[i], target + '/' + classification,
                              str(int(classification) * 10000 + 1 + num_newname) + ".jpg")  # 100001,100002,200001命名
            count += 1
        except:
            pass
        # print(str(int(classification)*10000 + num_newname) + ".jpg")
    print("提取图片完成，成功保存图片{}张".format(count))

if __name__ == '__main__':
    main()
    print("运行结束。")
