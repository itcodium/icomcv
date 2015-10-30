from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

	
def get_dif_images(imageA, imageB):
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	return s
	
def compare_images(imageA, imageB, title):
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	print m,s
	
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
 
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
 
	plt.show()
	
#compare_images(original, shopped, "Original vs. Photoshopped")

GrupoImagenes = []
Resultados = []

for x in range(2, 17):
	GrupoImagenes.append("test/g1/%d.jpg" % (x))

strFotoBase="test/g1/1.jpg"
base = cv2.imread(strFotoBase)
base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)

 
print strFotoBase,strFotoBase,get_dif_images(base,base)	
	
for foto in GrupoImagenes:
	print 
	iFoto = cv2.imread(foto)
	iFoto = cv2.cvtColor(iFoto, cv2.COLOR_BGR2GRAY)
	print strFotoBase,foto,get_dif_images(base,iFoto)	