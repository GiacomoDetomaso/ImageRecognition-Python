import cv2 as cv

# paths of the images
pathOriginal = "Assets/original.jpg"
pathDuplicate = "Assets/duplicate.jpg"

# image reading
original = cv.imread(pathOriginal)
duplicate = cv.imread(pathDuplicate)

if original.shape == duplicate.shape:
    print("The images have the same size and channels")
    diff_image = cv.subtract(original, duplicate)  # subtraction between the images

    r, g, b = cv.split(diff_image)  # split the output of the subtraction into his three main channel

    if cv.countNonZero(r) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(b) == 0:
        print("The images are equals")

else:
    print("The images are different")