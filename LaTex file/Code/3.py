# Set the number of points to collect
num_points = 4
point_count = 0
image_points = np.empty((num_points, 2))

# Load the architectural image and the flag image
Main_img = cv.imread('images/005.jpg', cv.IMREAD_COLOR)
Wrapping_img = cv.imread('images/flag.png', cv.IMREAD_COLOR)

# Mouse event handler function
def mark_point(event, x, y, flags, parameters):
    global point_count
    points = parameters[0]
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(parameters[1], (x, y), 5, (255, 0, 0), -1)
        points[point_count] = (x, y)
        point_count += 1

# Create a window and set the mouse callback
cv.namedWindow('Image', cv.WINDOW_AUTOSIZE)
params = [image_points, Main_img]
cv.setMouseCallback('Image', mark_point, params)

# Loop to display the image and collect points
while True:
    cv.imshow('Image', Main_img)
    if point_count == num_points:
        break
    if cv.waitKey(20) & 0xFF == 27:  # Escape key to exit
        break

# Define corresponding points on the flag image, forming a rectangle
flag_coordinates = np.array([[0, 0], 
                             [Wrapping_img.shape[1], 0], 
                             [Wrapping_img.shape[1], Wrapping_img.shape[0]], 
                             [0, Wrapping_img.shape[0]]], 
                             dtype=np.float32)

# Calculate the homography matrix
homography, _ = cv.findHomography(flag_coordinates, image_points)

# Apply the homography to warp the flag image onto the architectural image
warped_flag = cv.warpPerspective(Wrapping_img, homography, (Main_img.shape[1], Main_img.shape[0]))

# Blend the architectural image with the warped flag image
result_image = cv.addWeighted(Main_img, 1, warped_flag, 0.7, 0)