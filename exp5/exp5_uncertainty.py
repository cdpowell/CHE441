import sympy as sp
from math import log


if __name__ == '__main__':

    solutions = [[9.27, 0.364], [9.56, 0.305], [9.73, 0.3256]]

    for sol in solutions:

        pH = sp.Symbol('pH')
        Aj = sp.Symbol('Aj')
        A1 = sp.Symbol('A1')
        A5 = sp.Symbol('A5')

        syms = [pH, A1, A5, Aj]
        vals = {
            pH: sol[0],
            Aj: sol[1],
            A1: 0.6019,
            A5: 0.7166,
        }
        unc = {
            pH: 0.05,
            Aj: 0.002,
            A1: 0.002,
            A5: 0.002,
        }

        eq1 = sp.log((Aj - A1) / (A5 - Aj))
        eq2 = pH - eq1

        sum = 0
        for sym in syms:
            dif = eq1.diff(sym)
            print(sym, dif)
            subbed_dif = dif.subs(vals)
            sum += (subbed_dif ** 2) * (unc[sym] ** 2)

        print(log(float(eq.subs(vals)), 10))
        print(sum)
