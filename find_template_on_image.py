import cv2
import numpy as np
# import matplotlib.pyplot as plt


img1 = cv2.imread("tmp.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("main.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

matchesMask = [[0, 0] for i in range(len(matches))]

for i, (m, n) in enumerate(matches):
	if m.distance < 0.7 * n.distance:
		matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0),
						matchesMask=matchesMask, flags=cv2.DrawMatchesFlags_DEFAULT)

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
img3 = cv2.resize(img3, (640, 480))
cv2.imshow('tes', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
# BFMatcher with default params
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio best
# good = []
# for m, n in matches:
#	if m.distance < 0.75 * n.distance:
#		good.append([m])

#  cv2.drawMatchesKnn expects list of lists as matches
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, 
#								flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# plt.imshow(img3), plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()