print('creating file...')
r = open('tyc_basic.dat', 'r+b')
v = r.read()
r.close
n = int(len(v) / 10)
w = open('tyc_basic.csv', 'w')
for i in range(n):
    j = i * 10
    tyc12 = 133693440 & (v[j] << 19) | 522240 & (v[j + 1] << 11) | 2040 & (v[j + 2] << 3) | 7 & (v[j + 3] >> 5)
    tyc2 = int(tyc12 / 10000)
    tyc1 = tyc12 - tyc2 * 10000
    tyc3 = 3 & (v[j + 3] >> 3)
    sp = 7 & v[j + 3]
    mag = 15 & (v[j + 4] >> 4)
    rd = 61440 & (v[j + 4] << 12) | 4080 & (v[j + 5] << 4) | 15 & (v[j + 6] >> 4)
    rai = int(rd / 180)
    dei = rd - rai * 180
    rad = 15360 & (v[j + 6] << 10) | 1020 & (v[j + 7] << 2) | 3 & (v[j + 8] >> 6)
    ded = 16128 & (v[j + 8] << 8) | 255 & v[j + 9]
    ra = rai + rad / 16383
    ded = ded / 16383
    de = (dei - ded - 89) if dei < 90 else (dei + ded - 90)
    dst = str(tyc1) + ',' + str(tyc2) + ',' + str(tyc3) + ',' + '{:.4f}'.format(round(ra, 4)) + ',' + '{:.4f}'.format(round(de, 4)) + ',' + str(mag) + ',' + str(sp)
    if i < (n - 1):dst += '\n'
    w.write(dst)
w.close