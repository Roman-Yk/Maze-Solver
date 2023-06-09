import cv2
import numpy as np
from matplotlib import pyplot as plt
from dfs import Search

DOTS = 0
CALLED = False
START = []
END = []

image = cv2.resize(cv2.imread('maze.jpg'), (800,600))


# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Set the Canny edge detection thresholds
# lower_threshold = 200
# upper_threshold = 255

# # Apply edge detection using Canny edge detector
# edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)

# # Apply morphology operations to enhance edges if needed
# # ...

# # Find contours in the edge image
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter contours based on properties to identify the maze contour
# # ...
# for contour in contours:
#     # Calculate the contour area
#     area = cv2.contourArea(contour)
    
#     # Add additional filters based on the contour area, aspect ratio, etc.
#     # ...

#     # If the contour passes the filters, consider it as the maze contour
#     maze_contour = contour
#     break
# # Extract the bounding box of the maze contour
# x, y, w, h = cv2.boundingRect(maze_contour)

# # Crop the maze region from the original image
# maze = image[y:y+h, x:x+w]

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def draw_circle(event, x, y, flags, param):
    global DOTS
    global START
    global END
    
    if event == cv2.EVENT_LBUTTONDOWN and DOTS < 2:
        DOTS += 1
        if not START:
            START = [y,x]
        else:
            END = [y,x]
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
          
cv2.namedWindow(winname = "Maze Solver")
cv2.setMouseCallback("Maze Solver", draw_circle)

s = Search(img)
s.build()

while True:
    cv2.imshow("Maze Solver", img)

    if DOTS == 2 and not CALLED:
        img = s.has_path(tuple(START), tuple(END))
        CALLED = True
    
    if cv2.waitKey(10) & 0xFF == 27:
        break
          
cv2.destroyAllWindows()
