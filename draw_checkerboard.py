import os
import cv2
import numpy as np 
import scipy.io 

# 5 Cameras
for a in range(1,6):
    #Count number of frames to draw on
    dir_path = r'checkerboard/C'+ str(a)+'_keypoints'
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    for i in range (1,count):
        print("Image " + str(i) + "....")
        img = cv2.imread("checkerboard/C" + str(a) + "_undistort/" + str(i) + ".jpg")
        mat = scipy.io.loadmat("checkerboard/C" + str(a) + "_keypoints/" + str(i) + ".mat")
        mat = mat['imagePoints']
        if mat.size == 0: 
            cv2.imwrite("checkerboard/C" + str(a) + "_drawCheckerboard/" +str(i) + ".jpg", img)
        for j in range (mat.shape[0]):
            if np.isnan(mat[j][0]) or np.isnan(mat[j][1]) :
                continue
            check = cv2.circle(img, (int(mat[j][0]), int(mat[j][1])), 3, (0,0,255),3)
            cv2.imwrite("checkerboard/C" + str(a) + "_drawCheckerboard/" +str(i) + ".jpg", check)


    
