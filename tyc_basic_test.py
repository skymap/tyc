ra0 = {}
de0 = {}
ra1 = []
de1 = []
r = open('tyc_src.tsv', 'r')
src = r.read()
r.close
src = src.replace(' ', '')
rows = src.split('\n')
dst = bytearray()
for row in rows:
    d = row.split('|')
    if len(d[0]) > 0 and len(d[1]) > 0 and len(d[2]) > 0 and len(d[3]) > 0 and len(d[4]) > 0 and len(d[5]) > 0 and len(d[6]) > 0 and len(d[7]) > 0 and len(d[8]) > 0 and len(d[9]) > 0 and len(d[10]) == 0:
        k = d[0] + '-' + d[1] + '-' + d[2]
        ra0[k] = float(d[3])
        de0[k] = float(d[4])
        if ra0[k] < 0:print(k)
        if ra0[k] >= 360:print(k)
        if de0[k] <= -90:print(k)
        if de0[k] >= 90:print(k)
r = open('tyc_basic.dat', 'r+b')
v = r.read()
r.close
for i in range(2311831):
    j = i * 10
    tyc12 = 133693440 & (v[j] << 19) | 522240 & (v[j + 1] << 11) | 2040 & (v[j + 2] << 3) | 7 & (v[j + 3] >> 5)
    tyc2 = int(tyc12 / 10000)
    tyc1 = tyc12 - tyc2 * 10000
    tyc3 = 3 & (v[j + 3] >> 3)
    k = str(tyc1) + '-' + str(tyc2) + '-' + str(tyc3)
    rd = 61440 & (v[j + 4] << 12) | 4080 & (v[j + 5] << 4) | 15 & (v[j + 6] >> 4)
    rai = int(rd / 180)
    dei = rd - rai * 180
    rad = 15360 & (v[j + 6] << 10) | 1020 & (v[j + 7] << 2) | 3 & (v[j + 8] >> 6)
    ded = 16128 & (v[j + 8] << 8) | 255 & v[j + 9]
    ra = rai + rad / 16383
    ded = ded / 16383
    de = (dei - ded - 89) if dei < 90 else (dei + ded - 90)
    ra1.append(abs(ra - ra0[k]))
    de1.append(abs(de - de0[k]))
print('{:.9f}'.format(max(ra1)) + ',' + '{:.9f}'.format(max(de1)))