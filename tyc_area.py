from PIL import Image, ImageDraw
w = 7200
h = 3600
i = 1
j = 0
k = 0
c6 = [(255, 153, 204), (255, 255, 153), (153, 255, 153), (153, 204, 255)]
black = (0, 0, 0)
white = (255, 255, 255)
im = Image.new('RGB', (w, h), white)
draw = ImageDraw.Draw(im)
r = open('index_src.dat', 'r')
src = r.read()
r.close
src = src.replace(' ', '')
rows = src.split('\n')
for row in rows:
    d = row.split('|')
    if len(d) == 6:
        if len(d[2]) > 0 and len(d[3]) > 0 and len(d[4]) > 0 and len(d[5]) > 0:
            ra0 = int((360 - float(d[2])) * 20)
            ra1 = int((360 - float(d[3])) * 20)
            ra2 = int((ra0 + ra1) / 2)
            de0 = int((90 - float(d[4])) * 20)
            de1 = int((90 - float(d[5])) * 20)
            de2 = int((de0 + de1) / 2)
            if i > 4662:
                if de2 < k - 3:
                    j = 0 if j > 2 else (j + 1)
            else:
                if de2 > k + 3:
                    j = 0 if j > 2 else (j + 1)
            draw.rectangle((ra0, de0, ra1, de1), fill=c6[j], outline=black)
            draw.text((ra2, de2), str(i), fill=black)
            k = de2
            i = i + 1
im.save('tyc_area.png')