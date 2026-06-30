import cv2 as cv
import numpy as np

# Turn on the live camera (or replace with 'filename.mp4')
camera = cv.VideoCapture(0)

# Window names saved as variables to avoid typos
win_laplacian = 'Laplacian'
win_canny = 'Canny'

while True:
    _, frame = camera.read()

    # Applying Laplacian filter
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow(win_laplacian, laplacian)

    # Applying Canny filter
    edge = cv.Canny(frame, 100, 100)
    cv.imshow(win_canny, edge)

    # 1. Check if 'x' key is pressed
    if cv.waitKey(5) == ord('x'):
        break
        
    # 2. Check if either window's "X" close button was clicked
    # If a window is closed, its 'VISIBLE' property drops below 1
    if cv.getWindowProperty(win_laplacian, cv.WND_PROP_VISIBLE) < 1 or \
       cv.getWindowProperty(win_canny, cv.WND_PROP_VISIBLE) < 1:
        break

# End statements
camera.release()
cv.destroyAllWindows()