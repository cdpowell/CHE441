import sympy as sp


if __name__ == '__main__':

    k1 = sp.Symbol('k1')
    k2 = sp.Symbol('k2')
    t1 = sp.Symbol('T1')
    t2 = sp.Symbol('T2')

    symbols = [k1, k2, t1, t2]
    vals = {k1: 4.188537306, k2: 4.598215646, t1: (22.5+273.15), t2: (28.6+273.15)}
    unc = [0.0002178644192, 0.0003606964056, 0.02, 0.02]

    Ea = -sp.log(k1/k2) * 0.008314 / ((1/t1) - (1/t2))

    sums = 0
    for x in range(4):
        dif = Ea.diff(symbols[x])
        blah = dif.subs(vals)
        sums += (blah ** 2) * (unc[x] ** 2)

    print(sp.sqrt(sums))
