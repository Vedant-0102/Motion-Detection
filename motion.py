import cv2 as cv

video = cv.VideoCapture('car.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(history=50)

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        key = cv.waitKey(5) & 0xFF  
        if key == ord('x') or key == ord('X'): 
            break
    else:
        video = cv.VideoCapture('car.mp4')

cv.destroyAllWindows()
video.release()