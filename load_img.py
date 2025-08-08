import cv2
image_path = "/home/divya/cv_projects/images/test_img.jpg"
image = cv2.imread(image_path)
if image is None:
   print(f"Error:{image_path}")
else:
   height, width, channels = image.shape
   print(f"Dimensions:{width}, wide by:{height}, channels: {channels}")
   grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   cv2.imshow("Original image", image)
   cv2.imshow("Grayscale image", grayscale)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
