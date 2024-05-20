import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def get_percentile(val, bucket_number): 
    percentiles=[0.0]
    for i in range(bucket_number - 1):
        percentiles.append(np.percentile(val,(100//bucket_number)*(i+1)))
    return percentiles

def get_percentile_number(value, percentiles): 
    for i in range(len(percentiles)):
        if percentiles[i] > value:
            return i-1
    return len(percentiles)-1

def value_equalization(value, percentiles): 
    idx = get_percentile_number(value, percentiles)
    new_value = (idx)/(len(percentiles))
    return new_value

def values_equalization(val, percentiles): 
    newval=val.copy()

    for i in range(len(val)):
        newval[i]=value_equalization(val[i], percentiles)
    return newval


def equalize_histogram_uniform(channel):
    channel_normalized = (channel * 255).astype(np.uint8)
    sorted_indices = np.argsort(channel_normalized)
    uniform_values = np.linspace(0, 1, len(channel_normalized))
    equalized_channel = np.zeros_like(channel_normalized, dtype=float)
    equalized_channel[sorted_indices] = uniform_values
    return equalized_channel

def equalize_histogram_opencv(image):

    image_cv = np.array(image)

    r, g, b = cv2.split(image_cv)

    r_eq = cv2.equalizeHist(r)
    g_eq = cv2.equalizeHist(g)
    b_eq = cv2.equalizeHist(b)

    image_eq = cv2.merge((r_eq, g_eq, b_eq))

    image_eq_pil = Image.fromarray(image_eq)

    return image_eq_pil




name="Bush.bmp"
img = Image.open(name)
draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]
r = np.zeros((height* width), dtype=float)
g = np.zeros((height* width), dtype=float)
b = np.zeros((height* width), dtype=float)
px = np.array(img) / 255.

r = px[..., 0].reshape((height * width,)) 
g = px[..., 1].reshape((height * width,))
b = px[..., 2].reshape((height * width,))

plt.figure(figsize=(15, 10))
plt.subplot(4, 3, 1)
plt.hist(r, color='red', alpha=0.5)
plt.title('Red Channel Before')

plt.subplot(4, 3, 2)
plt.hist(g, color='green', alpha=0.5)
plt.title('Green Channel Before')

plt.subplot(4, 3, 3)
plt.hist(b, color='blue', alpha=0.5)
plt.title('Blue Channel Before')


perr=get_percentile(r,100)
perg=get_percentile(g,100)
perb=get_percentile(b,100)

newr=values_equalization(r, perr)
newg=values_equalization(g, perg)
newb=values_equalization(b, perb)


plt.subplot(4, 3, 4)
plt.hist(newr, color='red', alpha=0.5)
plt.title('Red Channel After')

plt.subplot(4, 3, 5)
plt.hist(newg, color='green', alpha=0.5)
plt.title('Green Channel After')

plt.subplot(4, 3, 6)
plt.hist(newb, color='blue', alpha=0.5)
plt.title('Blue Channel After')


r_eq = equalize_histogram_uniform(r)
g_eq = equalize_histogram_uniform(g)
b_eq = equalize_histogram_uniform(b)


plt.subplot(4, 3, 7)
plt.hist(r_eq, color='red', alpha=0.5)
plt.title('Red Channel After uniform')

plt.subplot(4, 3, 8)
plt.hist(g_eq, color='green', alpha=0.5)
plt.title('Green Channel After uniform')

plt.subplot(4, 3, 9)
plt.hist(b_eq, color='blue', alpha=0.5)
plt.title('Blue Channel After uniform')


img_eq = equalize_histogram_opencv(img)
px_eq = np.array(img_eq) / 255.0

r_eqcv = px_eq[..., 0].reshape((-1,))
g_eqcv = px_eq[..., 1].reshape((-1,))
b_eqcv = px_eq[..., 2].reshape((-1,))


plt.subplot(4, 3, 10)
plt.hist(r_eqcv, color='red', alpha=0.5)
plt.title('Red Channel After cv2')

plt.subplot(4, 3, 11)
plt.hist(g_eqcv, color='green', alpha=0.5)
plt.title('Green Channel After cv2')

plt.subplot(4, 3, 12)
plt.hist(b_eqcv, color='blue', alpha=0.5)
plt.title('Blue Channel After cv2')

r_eq=np.reshape(r_eq,(height,width))
g_eq=np.reshape(g_eq,(height,width))
b_eq=np.reshape(b_eq,(height,width))
new_img = np.zeros_like(px)
new_img[..., 0] = r_eq
new_img[..., 1] = g_eq
new_img[..., 2] = b_eq

i = Image.fromarray(np.uint8(new_img * 255))
i.save(name[:-4]+"_eq.jpg")

r_eqcv=np.reshape(r_eqcv,(height,width))
g_eqcv=np.reshape(g_eqcv,(height,width))
b_eqcv=np.reshape(b_eqcv,(height,width))
new_img = np.zeros_like(px)
new_img[..., 0] = r_eqcv
new_img[..., 1] = g_eqcv
new_img[..., 2] = b_eqcv

i = Image.fromarray(np.uint8(new_img * 255))
i.save(name[:-4]+"_cv2.jpg")

newr=np.reshape(newr,(height,width))
newg=np.reshape(newg,(height,width))
newb=np.reshape(newb,(height,width))
new_img = np.zeros_like(px)
new_img[..., 0] = newr
new_img[..., 1] = newg
new_img[..., 2] = newb

i = Image.fromarray(np.uint8(new_img * 255))
i.save(name[:-4]+"_ans.jpg")

plt.suptitle(name,fontsize=16)
plt.tight_layout()
plt.show()