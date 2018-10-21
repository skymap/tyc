r = open('tyc_src.tsv', 'r')
src = r.read()
r.close
w = open('tyc_basic.dat', 'w+b')
src = src.replace(' ', '')
rows = src.split('\n')
dst = bytearray()
for row in rows:
    d = row.split('|')
    if len(d[0]) > 0 and len(d[1]) > 0 and len(d[2]) > 0 and len(d[3]) > 0 and len(d[4]) > 0 and len(d[5]) > 0 and len(d[6]) > 0 and len(d[7]) > 0 and len(d[8]) > 0 and len(d[9]) > 0 and len(d[10]) == 0:
        tyc1 = int(d[0])
        tyc2 = int(d[1])
        tyc3 = int(d[2])
        tyc12 = tyc2 * 10000 + tyc1
        ra = float(d[3])
        de = float(d[4])
        des = -1 if de < 0 else 1
        de = abs(de)
        rai = int(ra)
        dei = int(de)
        rad = round((ra - rai) * 16383)
        ded = round((de - dei) * 16383)
        rd = (89 - dei) if des < 0 else (dei + 90)
        rd = rd + rai * 180
        bt = float(d[7])
        vt = float(d[8])
        bv = bt - vt
        mag = int(vt - 0.090 * bv)
        b = 0.850 * bv
        if b < -0.3:
            sp = 0
        elif b >= -0.3 and b < 0.0:
            sp = 1
        elif b >= 0.0 and b < 0.3:
            sp = 2
        elif b >= 0.3 and b < 0.6:
            sp = 3
        elif b >= 0.6 and b < 0.9:
            sp = 4
        elif b >= 0.9 and b < 1.5:
            sp = 5
        elif b >= 1.5 and b < 2.1:
            sp = 6
        else:
            sp = 7
        dst.append(255 & (tyc12 >> 19))
        dst.append(255 & (tyc12 >> 11))
        dst.append(255 & (tyc12 >> 3))
        dst.append(224 & (tyc12 << 5) | 24 & (tyc3 << 3) | 7 & sp)
        dst.append(240 & (mag << 4) | 15 & (rd >> 12))
        dst.append(255 & (rd >> 4))
        dst.append(240 & (rd << 4) | 15 & (rad >> 10))
        dst.append(255 & (rad >> 2))
        dst.append(192 & (rad << 6) | 63 & (ded >> 8))
        dst.append(255 & ded)
w.write(dst)
w.close