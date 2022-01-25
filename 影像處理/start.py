from PIL import ImageGrab
import numpy as np
import cv2
from glob import glob

""""***********黑棋辨識***********"""
def Bgray(img):
    [height, width, channel ] = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = np.sum(gray < 125)
    Bpercent = (float)(a) / (float)(height*width)
    return Bpercent

""""***********白棋辨識***********"""
def Wgray(img):
    [height, width, channel] = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #b=np.sum(gray>235)
    b=np.sum(gray>220)
    Wpercent = (float)(b) / (float)(height*width)
    return Wpercent

""""***********棋盤辨識***********"""
def checkerboard(img):
    image = img.copy()
    w, h, c = img.shape
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([10, 0, 0])
    upper = np.array([40, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    erodeim = cv2.erode(mask, None, iterations=2)  # 腐蝕
    dilateim = cv2.dilate(erodeim, None, iterations=2)#　膨脹

    img = cv2.bitwise_and(img, img, mask=dilateim)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    maxarea = 0
    maxint = 0
    for c in contours:
        if cv2.contourArea(c) > maxarea:
            maxarea = cv2.contourArea(c)
            maxint = i
        i += 1
    # 多邊形擬合
    epsilon = 0.02 * cv2.arcLength(contours[maxint], True)
    approx = cv2.approxPolyDP(contours[maxint], epsilon, True)
    [[x1, y1]] = approx[0]
    [[x2, y2]] = approx[2]
    checkerboard = image[y1:y2, x1:x2]    
    return checkerboard

""""***********棋子位置辨識***********"""
def Ccheckerboard(img):
    #img = cv2.resize(img, (234,276), interpolation=cv2.INTER_AREA)
    img = cv2.resize(img, (234,276), interpolation=cv2.INTER_AREA)
    #變量定義
    small_length=38  #每個小格寬高
    chessman_length=38 #棋子直徑
    list = [[0 for i in range(6)] for j in range(7)]
    #print(list)
    for i in range(6):
        for j in range(7):

            ai = i
            bj = j

            Tp_x = small_length * ai
            Tp_y = small_length * bj
            Tp_width = chessman_length
            Tp_height = chessman_length

            img_temp=img[Tp_y:Tp_y+Tp_height, Tp_x:Tp_x+Tp_width]#參數含義分別是：y、y+h、x、x+w

            bgray=Bgray(img_temp)
            if bgray > 0.35:
                list[bj][ai] = 2 #黑色
                print("第", i+1, "列，第", j+1, "行棋子為黑色")
                
            else:
                wgray = Wgray(img_temp)
                if wgray > 0.15:
                    list[bj][ai] = 1  # 白色
                    print("第", i+1, "列，第",j+1 , "行棋子為白色")
                   
                else:
                    list[bj][ai] = 0  # 無棋子        
    return  list

if __name__ =="__main__":
    list = [[0 for i in range(6)] for j in range(7)]
    list_finall = []
    """"***********影像攝取***********"""
    cap = cv2.VideoCapture(0)
    while(1):
    # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):#如果按下q 就截圖儲存並退出
            cv2.imwrite("C://Users//acer//Desktop//412413//screen//test.jpg", frame)   #儲存路徑
            cv2.imwrite("C://Users//acer//Desktop//test412413//screen//test.jpg", frame)   #儲存路徑
            break
    cap.release()
    cv2.destroyAllWindows()
    img = cv2.imread("C://Users//acer//Desktop//412413//screen//test.jpg")   
    img1=checkerboard(img)
    list=Ccheckerboard(img1)
    print(list)

   
   




