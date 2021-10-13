# For encryption process
def ArnoldCatTransform(img, num):
    rows, cols, ch = img.shape
    n = 256
    img_arnold = np.zeros([rows, cols, ch])
    for x in range(0, rows):
        for y in range(0, cols):
            img_arnold[x][y] = img[(2*x+y)%n][(y+x)%n]
    print(img_arnold[x][y]) 
    return img_arnold    
  
def ArnoldCatEncryption(imageName, key):
    img = cv2.imread(imageName)
    for i in range (0,key):
        img = ArnoldCatTransform(img, i)
    cv2.imwrite("jpg_ArnoldcatEnc.png", img)
    return img

# For decryption process 
def ArnoldCatInverseTransform(img, num):
    rows, cols, ch = img.shape
    n = 256
    img_arnold = np.zeros([rows, cols, ch])
    for x in range(0, rows):
        for y in range(0, cols):
            img_arnold[x][y] = img[(x-y)%n][((2*y)-x)%n]
    return img_arnold
  
  def ArnoldCatDecryption(imageName, key):
    img = cv2.imread(imageName)
    for i in range (0,key):
        img = ArnoldCatInverseTransform(img, i)
    cv2.imwrite("jpg_ArnoldcatDec.jpg", img)
    return img
  
