# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw
from sys import argv

name,opeI,outI,kk,ll=argv

image = Image.open(opeI)
draw = ImageDraw.Draw(image)  
width = image.size[0]  
height = image.size[1]
kk=int(kk)
ll=int(ll)
w=width//kk
h=height//ll
pix = image.load()

for k in range(kk):
    for l in range(ll):
        w_step = w * random.randint(0, kk - 1) - k
        h_step = h * random.randint(0, ll - 1) - l
        # Убедимся, что w_step и h_step находятся в пределах допустимого диапазона
        w_step = max(-k*w, min((kk - 1 - k)*w, w_step))
        h_step = max(-l*h, min((ll - 1 - l)*h, h_step))
        for i in range(w*k, w*(k+1)):
            for j in range(h*l, h*(l+1)):
                target_i = i + w_step
                target_j = j + h_step
                if 0 <= target_i < width and 0 <= target_j < height:
                    pix[i, j], pix[target_i, target_j] = pix[target_i, target_j], pix[i, j]


# for k in range(kk):
# 	for l in range(ll):
# 		w_step = w * random.randint(0, kk - 1) - k
# 		h_step = h * random.randint(0, ll - 1) - l
# 		for i in range(w*k,w*(k+1)):
# 			for j in range(h*l,h*(l+1)):
# 				a = pix[i, j]
# 				pix[i, j]=pix[i+w_step,j+h_step]
# 				pix[i+w_step,j+h_step]=a
				# b = pix[i, j][1]
				# c = pix[i, j][2]
				# if a1==0 and b1==0 and c1==0:
				# 	draw.point((i, j), (a1, b1, c1))
				# else:
				# 	 draw.point((i, j), (a, b, c))
image.save(outI, "BMP")
del draw
