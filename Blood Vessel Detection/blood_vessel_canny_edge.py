from PIL import Image
import cv2
import numpy as np
import os
cwd = os.getcwd()
cwd_green_channel = cwd + '\\Green Channel\\'
cwd_blood_vessel = cwd + '\\Blood Vessel\\'
cwd_data = cwd + '\\Data\\'
for i in range(21, 41):
    path = str(i)+'_training.tif'
    im = Image.open(cwd_data+path,'r')#.convert('LA')
    pix_val = list(im.getdata())
    green_channel = [(0, x, 0) for a, x, b in pix_val]
    im2 = Image.new(im.mode, im.size)
    im2.putdata(green_channel)
    save_path = cwd_green_channel + str(i) + '.tif'
    im2.save(save_path)
    def canny(image): # 4- Wrapping the below 3 lines into a function
        global i
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # 1- converts the RGB 2 Gray scale
        blur = cv2.GaussianBlur(gray, (5, 5), 1.4) # 2- We are using 5 by 5 kernel with deviation 0
        canny = cv2.Canny(image, 30, 150) # 3- Gradient image is constructed
        return canny
    image = cv2.imread(save_path) 
    eye_image = np.copy(image) # 1- Making a copy of original image
    canny = canny(eye_image)
    cv2.imwrite(cwd_blood_vessel+str(i)+'.tif', canny)
print('Please Check the Green Channel and Blood Vessel folder for results')
x = input('Press Enter to continue')