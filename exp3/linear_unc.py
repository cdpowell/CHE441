import sympy as sp


if __name__ == '__main__':

    T = sp.Symbol('T')
    a = sp.Symbol('a')
    b = sp.Symbol('b')
    n = sp.Symbol('n')
    F = sp.Symbol('F')
    Q = sp.Symbol('Q')
    R = sp.Symbol('R')

    vals = {
        T: 298, a: 1.603124917, b: -0.00144609,
        n: 2, F: 96485.3415,
        Q: 0.0435 * 0.692**2 / 0.758**2, R: 8.314472,
    }
    unc = {
        T: 0.03, a: 0.007989274, b: 2.55732e-05,
        F: 0.0039,
        R: 0.000015,
    }

    """Energy (E) Equation - Linear"""
    E = sp.Symbol('E')
    eq1 = a + b * T
    eq1_syms = [T, a, b]

    sum = 0
    for sym in eq1_syms:
        dif = eq1.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    vals[E] = eq1.subs(vals)
    unc[E] = sp.sqrt(sum)

    print('E:   ', vals[E])
    print('unE: ', unc[E])
    print()

    """Gibbs Free Energy (G) Equation - Linear"""
    G = sp.Symbol('G')
    eq2 = -n * F * E
    eq2_syms = [F, E]

    sum = 0
    for sym in eq2_syms:
        dif = eq2.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    vals[G] = eq2.subs(vals)
    unc[G] = sp.sqrt(sum)

    print('G:   ', vals[G])
    print('unG: ', unc[G])
    print()

    """Entropy (S) Equation - Linear"""
    S = sp.Symbol('S')
    eq3 = n * F * b
    eq3_syms = [F, b]

    sum = 0
    for sym in eq3_syms:
        dif = eq3.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    vals[S] = eq3.subs(vals)
    unc[S] = sp.sqrt(sum)

    print('S:   ', vals[S])
    print('unS: ', unc[S])
    print()

    """Enthalpy (H) Equation - Linear"""
    eq4 = G + T * S
    eq4_syms = [G, T, S]

    sum = 0
    for sym in eq4_syms:
        dif = eq4.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    eq4_val = eq4.subs(vals)
    eq4_unc = sp.sqrt(sum)

    print('H:   ', eq4_val)
    print('unH: ', eq4_unc)
    print()

    """Energy Not (E0) Equation - Linear"""
    E0 = sp.Symbol('E0')
    eq5 = E + (R * T * sp.ln(Q) / (n * F))
    eq5_syms = [E, R, T, F]

    sum = 0
    for sym in eq5_syms:
        dif = eq5.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    vals[E0] = eq5.subs(vals)
    unc[E0] = sp.sqrt(sum)

    print('E0:   ', vals[E0])
    print('unE0: ', unc[E0])
    print()

    """Gibbs Free Energy Not (G0) Equation - Linear"""
    eq6 = -n * F * E0
    eq6_syms = [F, E0]

    sum = 0
    for sym in eq6_syms:
        dif = eq6.diff(sym)
        subbed_dif = dif.subs(vals)
        sum += (subbed_dif ** 2) * (unc[sym] ** 2)

    eq6_val = eq6.subs(vals)
    eq6_unc = sp.sqrt(sum)

    print('G0:   ', eq6_val)
    print('unG0: ', eq6_unc)
    print()
