import os
import cv2

Main_folder = 'Images'
MyFolders = os.listdir(Main_folder)
print(MyFolders) 
i = 0
for folder in MyFolders:
    path = Main_folder + '/' + folder
    img = []
    imglist = os.listdir(path)

    for imgname in imglist:
        curImg = cv2.imread(f'{path}/{imgname}')
        curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        img.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(img)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imwrite('test'+str(i)+'.jpg', result)
        cv2.imshow(folder,result)
        cv2.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')
    i = i+1
cv2.waitKey(0)
print("done")