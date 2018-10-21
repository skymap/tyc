from PIL import Image, ImageDraw
w = 9000
h = 4500
im = Image.new('RGB', (w, h), (0, 0, 0))
draw = ImageDraw.Draw(im)
c8 = [[136, 204, 255], [187, 238, 255], [238, 255, 255], [255, 255, 255], [255, 255, 238], [255, 238, 187], [255, 204, 136], [255, 153, 85]]
r = open('tyc_basic.csv', 'r')
src = r.read()
r.close
rows = src.split('\n')
dst = bytearray()
for row in rows:
    d = row.split(',')
    if len(d[0]) > 0:
        x = int(w * (360 - float(d[3])) / 360)
        y = int(h * (90 - float(d[4])) / 180)
        m = int(d[5]) * 8
        c = c8[int(d[6])]
        draw.point((x, y), (c[0] - m, c[1] - m, c[2] - m))
im.save('tyc_basic.png')