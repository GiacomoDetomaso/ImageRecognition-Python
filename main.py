import cv2 as cv


def calculateSimilar(mat, valueMatch=40, takenVal=20):
    sum_values = 0
    for m in mat[:takenVal]:
        sum_values = sum_values + m
    match_medium = sum_values / takenVal
    if match_medium > valueMatch:
        print("Non valido")
    else:
        print("Valido")


original = cv.imread("original.jpg", cv.IMREAD_GRAYSCALE)  # read the original image
similar = cv.imread("similar.jpg", cv.IMREAD_GRAYSCALE)  # read the similar image

# check first if the two images are equals or not
if not original is None and not similar is None:
    if original.shape == similar.shape:
        print("The image have same size and channels")
        difference = cv.subtract(original, similar)
        if cv.countNonZero(difference) == 0 :
            print("The images are equals")
            flag = False  # the image are exactly the same
    else:
        print("The images are different")
        flag = True  # the images are different so you need to check if thery are similar or not

# check if there are some similarities between these image
# noinspection PyUnboundLocalVariable
if flag:
    orb = cv.ORB.create()  # create the orb detector
    kp1, des1 = orb.detectAndCompute(original, None)
    kp2, des2 = orb.detectAndCompute(similar, None)

    # comparing using brute-force comparing each descriptor
    bruteForce = cv.BFMatcher(cv.NORM_HAMMING, True)
    matches = bruteForce.match(des1, des2)  # match the two descriptors

    distances = []  # array of distances
    for i in matches:
        distances.append(i.distance)

    distances = sorted(distances)
    print("Numero match", len(matches))

    # matching = cv.drawMatches(original, kp1, similar, kp2, matches[:20], None)

    calculateSimilar(distances, 30, 20)  # calculate the similarity

    for i in distances:
        print(i)

    # cv.imshow("Match",matching)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
