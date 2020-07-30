import cv2
import numpy as np

def matchImg(imgPath1,imgPath2):

    imgs = []

    # 原始图像，用于展示
    sou_img1 = cv2.imread(imgPath1)
    sou_img2 = cv2.imread(imgPath2)

    # 原始图像，灰度
    # 最小阈值100,最大阈值500
    img1 = cv2.imread(imgPath1, 0)
    blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
    canny1 = cv2.Canny(blur1, 100, 500)
    cv2.imwrite('temp1.png', canny1)

    img2 = cv2.imread(imgPath2, 0)
    blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
    canny2 = cv2.Canny(blur2, 100, 500)
    cv2.imwrite('temp2.png', canny2)

    target = cv2.imread('temp1.png')
    template = cv2.imread('temp2.png')

    # 调整显示大小
    target_temp = cv2.resize(sou_img1, (350, 200))
    target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    template_temp = cv2.resize(sou_img2, (200, 200))
    template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp)
    imgs.append(template_temp)

    theight, twidth = template.shape[:2]

    # 匹配拼图
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    # 归一化
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 匹配后结果画圈
    cv2.rectangle(target,max_loc,(max_loc[0]+twidth,max_loc[1]+theight),(0,0,255),2)


    target_temp_n = cv2.resize(target, (350, 200))
    target_temp_n = cv2.copyMakeBorder(target_temp_n, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp_n)

    imstack = np.hstack(imgs)

    cv2.imshow('stack'+str(max_loc), imstack)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

matchImg('vcode_data/out_'+str(1)+'.png','vcode_data/in_'+str(1)+'.png')