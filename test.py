import cv2
from numpy.linalg import norm

def brightness(img):
    if len(img.shape) == 3:
        # Colored RGB or BGR (*Do Not* use HSV images with this function)
        # create brightness with euclidean norm
        return np.average(norm(img, axis=2)) / np.sqrt(3)
    else:
        # Grayscale
        return np.average(img)
# if (you have only 1 webcam){ set device = 0} else{ chose your favorite webcam setting device = 1, 2 ,3 ... }
cap = cv2.VideoCapture(0)
while True:
  # Getting our image by webcam and converting it into a gray image scale
    _, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # show the gray image
    cv2.imshow("Output", image)

    print(brightness(image))
    
    #key to give up the app.
    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 27 is the ascii ord for esc
        break
cv2.destroyAllWindows()
cap.release()
