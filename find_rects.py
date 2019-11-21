import cv2

# Function written by Stackoverflow-User David Tran
def DED(grayImg):                           #Edge Detection, returns image array

    minInt, maxInt, minLoc, maxLoc = cv2.minMaxLoc(grayImg) #Grayscale: MinIntensity, Max, and locations
    beam = cv2.mean(grayImg)    #Find the mean intensity in the img pls.
    mean = float(beam[0])
    CannyOfTuna = cv2.Canny(grayImg, (mean + minInt)/2, (mean + maxInt)/2)  #Finds edges using thresholding and the Canny Edge process.

    return CannyOfTuna


def getrect(path_to_img):
    img = cv2.imread(path_to_img)
    #img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)
    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # do some edge detection
    canny = DED(gray)

    # find the contours
    contours, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # detect only shapes with 4 lines
    new_contours = []
    for i in range(len(contours)):
        if len(contours[i]) == 4:
            new_contours.append(contours[i])

    return new_contours

def vectors_to_coords(*args):
    # returns x1, y1, x2, y2
    coords = []
    for vectors in args:
        for vector in vectors:
            coords.append([vector[0][0][0], vector[0][0][1], vector[2][0][0], vector[1][0][1]])

    return coords

def update_flask():
    pathone = r"./ressources/rects1.png"
    pathtwo = r"./ressources/rects2.png"

    one = getrect(pathone)
    two = getrect(pathtwo)
    coords = vectors_to_coords(one, two)

    return coords


# just for testing
if __name__ == "__main__":
    pathone = r"./ressources/rects1.png"
    pathtwo = r"./ressources/rects2.png"

    one = getrect(pathone)
    two = getrect(pathtwo)
    coords = vectors_to_coords(one, two)
    print(len(coords))
    # # uncomment, if you want to write and display the rectangles
    # image = cv2.imread(r"./ressources/board.png")

    # cv2.drawContours(image, one, -1, (0,255,0), 3)
    # cv2.drawContours(image, two, -1, (0,255,0), 3)
    # cv2.imwrite(r"./ressources/markedrects.png", image)

    # while True:
    #     smaller = cv2.resize(image, (0,0), fx=0.3, fy=0.3)

    #     cv2.imshow("Rectangles", smaller)


    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break
