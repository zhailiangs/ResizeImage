import os
import cv2

destination_w = 400
destination_h = 300

def resize(image):
    if int(h/destination_h) < int(w/destination_w):
        new_h = destination_h
        new_w = int(w/int(h/destination_h))
        resize_img = cv2.resize(image,(new_w,new_h),interpolation=cv2.INTER_AREA)
        left = int((new_w - destination_w) / 2)
        right = left + destination_w
        return resize_img[0:destination_h,left:right]

    elif int(h/destination_h) == int(w/destination_w):
        return cv2.resize(image,(destination_w,destination_h),interpolation=cv2.INTER_AREA)
    else:
        new_w = destination_w
        new_h = int(h/int(w/destination_w))
        print(new_w,new_h)
        resize_img = cv2.resize(image,(new_w,new_h),interpolation=cv2.INTER_AREA)
        print('resize_img',resize_img.shape)
        bottom = int((new_h - destination_h) / 2)
        top = bottom + destination_h
        return resize_img[bottom:top,0:destination_w]


if __name__ == '__main__':
    # 输入原始图像存在的文件夹
    datadir = "zhengli"
    # 设置保存路径
    save_path = 'new'

    if not os.path.exists(save_path):#如果路径不存在
        os.makedirs(save_path)
    path = os.path.join(datadir)

    img_list = os.listdir(path)
    i = 1
    for img in img_list:
        image_source = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)  # 读取图片
        h,w = image_source.shape[0],image_source.shape[1]

        #跳过高度大于宽度的图
        if h > w:
            continue
            
        #跳过小于目标尺寸的图
        if h < destination_h or w < destination_w:
            continue
        image = resize(image_source)

        if image.shape[0] > 0 and image.shape[1]>0:
            file_save_path = os.path.join(save_path, str(i)+'.jpg') # 保存的图片与原始图片同名
            cv2.imwrite(file_save_path, image)
            i = i + 1
            print(i,' 处理完毕')
        else:
            print(os.path.join(path, img))