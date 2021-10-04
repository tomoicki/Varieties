from PIL import Image
import statistics
import matplotlib.pyplot as plt

with Image.open('original.jpg', 'r') as im:
    pix_val = list(im.getdata())

#print(im.size)
#print(pix_val)
pix = [list(elem) for elem in pix_val]
#print(pix)
for i in range(len(pix)):
    for j in range(3):
        if pix[i][j] <= 132:
            pix[i][j] = 0
        else:
            pix[i][j] = 1
#print(pix)
pix2 = [tuple(elem) for elem in pix]
im2 = Image.new('RGB',im.size)
im2.putdata(pix_val)
im2.save('czarobialy.jpg')
#print(pix)
Image.open('original.jpg', 'r').convert('L').save('xyz_greyscale.jpg')
points = []
No = []

for pixel in pix_val:
    points.append(pixel[0])
for i in range(256):
    No.append(points.count(i))

N = len(points)
print(N)
print(points)
max_t = []
#print(statistics.mean(points))

for j in range(256):
    threshold = j

    No_minus = []
    for i in range(threshold):
        No_minus.append(points.count(i))
    No0 = sum(No_minus)
    if No0 != 0:
        P0 = No0 / N
        P1 = 1 - P0

        ms_minus = []
        for i in range(threshold):
            ms_minus.append(i * points.count(i))
        ms0 = sum(ms_minus) / No0

        ms_plus = []
        for i in range(threshold,256):
            ms_plus.append(i * points.count(i))
        ms1 = sum(ms_plus) / (N - No0)
        #print(j,ms0,ms1,P0,P1)
        max_t.append(P0 * P1 * (ms0 - ms1)**2)
        print(j)

print(max_t)

plt.hist(points,bins=255)
#plt.show()
