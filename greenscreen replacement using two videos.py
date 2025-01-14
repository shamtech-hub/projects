import cv2
import numpy as np

# Open the two video files
video = cv2.VideoCapture("small.mp4")
video1 = cv2.VideoCapture("skyvid.mp4")

def nothing():
    pass

# Create a window for the trackbars
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 300, 300)

# Add trackbars for HSV range
cv2.createTrackbar('L-H', "Trackbars", 32, 179, nothing)
cv2.createTrackbar('L-S', "Trackbars", 94, 255, nothing)
cv2.createTrackbar('L-V', "Trackbars", 132, 255, nothing)
cv2.createTrackbar('U-H', "Trackbars", 179, 179, nothing)
cv2.createTrackbar('U-S', "Trackbars", 255, 255, nothing)
cv2.createTrackbar('U-V', "Trackbars", 255, 255, nothing)

while True:
    # Read frames from both videos
    ret, frame = video.read()
    ret1, frame1 = video1.read()

    # Break the loop if either video ends
    if not ret or not ret1:
        print("One of the videos ended. Exiting...")
        break

    # Resize both frames to match dimensions
    frame = cv2.resize(frame, (640, 480))
    frame1 = cv2.resize(frame1, (640, 480))

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV values from the trackbars
    l_h = cv2.getTrackbarPos('L-H', "Trackbars")
    l_s = cv2.getTrackbarPos('L-S', "Trackbars")
    l_v = cv2.getTrackbarPos('L-V', "Trackbars")
    u_h = cv2.getTrackbarPos('U-H', "Trackbars")
    u_s = cv2.getTrackbarPos('U-S', "Trackbars")
    u_v = cv2.getTrackbarPos('U-V', "Trackbars")

    # Define HSV range for masking
    l_green = np.array([l_h, l_s, l_v])
    u_green = np.array([u_h, u_s, u_v])

    # Create a mask for the green color
    mask = cv2.inRange(hsv, l_green, u_green)

    # Invert the mask for the non-green areas
    mask_inv = cv2.bitwise_not(mask)

    # Extract the green screen and the replacement video areas
    res1 = cv2.bitwise_and(frame1, frame1, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the two results
    combined = cv2.add(res1, res2)

    # Display the results
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Green Screen Output", combined)

    # Break the loop on 'm' key press
    if cv2.waitKey(5) & 0xFF == ord('m'):
        break

# Release video resources and close windows
video.release()
video1.release()
cv2.destroyAllWindows()
