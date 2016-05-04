import cv2
import sys
import glob

#Read test image from user
img = cv2.imread(sys.argv[1])
#Resize the image to 100 * 100
img_ori = cv2.resize(img,(100,100))
#Set the threshold as 0.65
threshold = 0.65
#Set default max match value
max1 = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0

#For loop to check very image in data
for j in range(1,6):
    if j == 1:
        #Find the number of image files in the Smile folder
        files = glob.glob('01/*.*')
        number = len(files)
        #Check every image in 'Smile'
        for i in range(1, number + 1):
            if i == 1:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                #Set the template image
                temp = cv2.imread('01/01.png', 0)
                #Resize the template
                template=cv2.resize(temp,(100,100))
            elif i > 1 and i < 10:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('01/0' + str(i) + '.jpg', 0)
                template = cv2.resize(temp,(100, 100))
            else:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('01/' + str(i) + '.jpg', 0)
                template = cv2.resize(temp,(100, 100))

            #Check how much image match with template in Smile
            match = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            #Find the max value of match which greater than threshold
            if match > threshold and match > max1:
                max1 = match

    elif j == 2:
        # Find the number of image files in the Hat folder
        files = glob.glob('02/*.*')
        number = len(files)
        # Check every image in 'Hat'
        for i in range(1, number + 1):
            if i < 10:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('02/0'+str(i)+'.jpg',0)
                template = cv2.resize(temp, (100, 100))
            else:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('02/'+ str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))

            # Check how much image match with template in Hat
            match = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            if match > threshold and match > max2:
                max2 = match

    elif j == 3:
        # Find the number of image files in the Hash folder
        files = glob.glob('03/*.*')
        number = len(files)
        # Check every image in 'Hash'
        for i in range(1, number + 1):
            if i < 10:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('03/0' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))
            else:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('03/' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))

            # Check how much image match with template in Hash
            match = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            if match > threshold and match > max3:
                max3 = match

    elif j == 4:
        # Find the number of image files in the Heart folder
        files = glob.glob('04/*.*')
        number = len(files)
        # Check every image in 'Heart'
        for i in range(1, number + 1):
            if i < 10:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('04/0' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))
            else:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp= cv2.imread('04/' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))

            # Check how much image match with template in Heart
            match = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            if match > threshold and match > max4:
                max4 = match

    elif j == 5:
        # Find the number of image files in the Dollar folder
        files = glob.glob('05/*.*')
        number = len(files)
        # Check every image in 'Dollar'
        for i in range(1, number + 1):
            if i < 10:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('05/0' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))
            else:
                img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
                temp = cv2.imread('05/' + str(i) + '.jpg', 0)
                template = cv2.resize(temp, (100, 100))

            # Check how much image match with template in Dollar
            match = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            if match > threshold and match > max5:
                max5 = match

#Find the max value of match in five class and determine the class by the class of the highest match value
if max(max1,max2,max3,max4,max5) == max1:
    print('Smile')
elif max(max1,max2,max3,max4,max5) == max2:
    print('Hat')
elif max(max1,max2,max3,max4,max5) == max3:
    print('Hash')
elif max(max1,max2,max3,max4,max5) == max4:
    print('Heart')
elif max(max1,max2,max3,max4,max5) == max5:
    print('Dollar')