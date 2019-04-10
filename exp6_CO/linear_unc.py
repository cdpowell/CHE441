import math
import sympy as sp


if __name__ == '__main__':

    Be = sp.Symbol('Be')

    symbols = [Be]
    vals = {Be: 1.931637316}
    unc = [0.0004178364948]

    f = 6.62607004e-34 / (Be * 8 * (math.pi**2) * 299792458)
    # f = B1 + (1.5 * ae)
    print(f.subs(vals))

    sums = 0
    for x in range(len(symbols)):
        dif = f.diff(symbols[x])
        blah = dif.subs(vals)
        sums += (blah ** 2) * (unc[x] ** 2)

    print(sp.sqrt(sums))
