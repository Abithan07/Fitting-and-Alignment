img = cv2.imread('a1images/emma.jpg', cv2.IMREAD_GRAYSCALE)

# Define the intensity transformation function
def intensity_transformation(input_intensity):
    if input_intensity < 100:
        return input_intensity  # Linear with slope 1
    elif input_intensity <= 150:
        return input_intensity*1.55 + 22.5 # Linear with slope 1.55 and intercept at 22.5
    else:
        return input_intensity  # Linear with slope 1

# Applying the intensity transformation to the image
transformed_img = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        transformed_img[i, j] = intensity_transformation(img[i, j])
